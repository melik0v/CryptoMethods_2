import random
from dataclasses import dataclass
import math
from tools.utils import (
    gcd_ext,
    gen_prime_num,
    mod_inv,
    split
)


class RSA:

    @dataclass(frozen=True)
    class PublicKey:
        e: int
        n: int

    @dataclass(frozen=True)
    class PrivateKey:
        d: int
        n: int

    def __init__(self, public_key: PublicKey = None, private_key: PrivateKey = None) -> None:
        """
        Implementation of the asymmetric RSA encryption algorithm.
        private_key
            Private key of type RSA.PrivateKey, which contains the number D and the modulus N.
        public_key
            Public key of type RSA.PublicKey, which contains the number E and the modulus N.
        """
        if not (public_key and private_key):
            public_key = None
            private_key = None
        elif not (isinstance(public_key, RSA.PublicKey) and isinstance(private_key, RSA.PrivateKey)):
            raise TypeError("Wrong type of arguments (must be RSA.PublicKey and RSA.PrivateKey")

        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, data: bytes) -> bytes:
        data = split(data, (self.public_key.n.bit_length() >> 3) - 1)
        result = []
        for index, unit in enumerate(data):
            tmp = int.from_bytes(unit, "big")
            encrypted_data = pow(tmp, self.public_key.e, self.public_key.n)
            encrypted_bytes = encrypted_data.to_bytes(math.ceil(encrypted_data.bit_length() / 8), "big")
            delta = math.ceil(self.public_key.n.bit_length() / 8) - len(encrypted_bytes)
            if delta > 0 or not encrypted_bytes:
                encrypted_bytes = b'\x00' * delta + encrypted_bytes

            result.append(encrypted_bytes)

        return bytes(bytearray().join(result))

    def decrypt(self, data: bytearray or bytes) -> bytes:
        block_len = math.ceil(self.public_key.n.bit_length() / 8)
        length = math.ceil(len(data) / block_len)
        data = split(data, block_len)
        result = []
        for index, unit in enumerate(data):
            tmp = int.from_bytes(unit, "big")
            decrypted_data = pow(tmp, self.private_key.d, self.private_key.n)
            decrypted_bytes = decrypted_data.to_bytes(math.ceil(decrypted_data.bit_length() / 8), "big")
            delta = ((self.public_key.n.bit_length() >> 3) - 1) - len(decrypted_bytes)

            if delta > 0 and index != length - 1:
                decrypted_bytes = b'\x00' * delta + decrypted_bytes
            result.append(decrypted_bytes)

        return bytes(bytearray().join(result))

    @staticmethod
    def key_gen(key_size: int = 1024, p: int = None, q: int = None):
        """
        Generate public and private keys. If both p and q parameters are filled, the "key_size" parameter is ignored,
        otherwise p and q are generated automatically.

        :param key_size: Number of bits to generate P and Q
        :param p: Prime number to generate keys
        :param q: Prime number to generate keys
        :return: Public key and Private key
        """
        if not (p and q):
            p = gen_prime_num(key_size)
            q = gen_prime_num(key_size)
        n = p * q
        if p != q:
            phi = (p - 1) * (q - 1)
        else:
            phi = n - p
        while True:
            e = random.randint(2, phi)
            if gcd_ext(e, phi).gcd == 1:
                break

        d = mod_inv(e, phi)

        return RSA.PublicKey(e, n), RSA.PrivateKey(d, n)


# msg = "Привет, Мир!"
# msg = bytes(msg, "UTF-8")
# print(msg)
# keys = RSA.key_gen(384)
# obj = RSA(*keys)
#
# enc_msg = obj.encrypt(msg)
# print(enc_msg)
# dec_msg = obj.decrypt(enc_msg)
# print(dec_msg)
#
# print(dec_msg.decode("UTF-8"))
