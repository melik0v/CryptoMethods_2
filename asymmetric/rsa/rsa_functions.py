import random
from dataclasses import dataclass
import math
from tools.utils import (
    gcd_ext,
    gen_prime_num,
    pow_mod,
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

    def __init__(self, public_key: PublicKey, private_key: PrivateKey) -> None:
        """
        Implementation of the asymmetric RSA encryption algorithm.
        private_key
            Private key of type RSA.PrivateKey, which contains the number D and the modulus N.
        public_key
            Public key of type RSA.PublicKey, which contains the number E and the modulus N.
        """
        if not (isinstance(public_key, RSA.PublicKey) and isinstance(private_key, RSA.PrivateKey)):
            raise TypeError("Wrong type of arguments (must be RSA.PublicKey and RSA.PrivateKey")

        self.public_key = public_key
        self.private_key = private_key

    def encrypt(self, data: bytes):
        r = self.public_key.n.bit_length() >> 3
        data = split(data, self.public_key.n.bit_length() >> 3)
        result = []
        for unit in data:
            tmp = int.from_bytes(unit, "little")
            a = tmp.bit_length()
            encrypted_data = pow_mod(tmp, self.public_key.e, self.public_key.n)
            b = encrypted_data.bit_length()
            c = math.ceil(encrypted_data.bit_length() / 8)

            # result.append(encrypted_data.to_bytes(math.ceil(encrypted_data.bit_length() / 8), "little"))

            result.append(encrypted_data)
            # result.append(encrypted_data.to_bytes(encrypted_data.bit_length() >> 3, "little"))
            # result += encrypted_data.to_bytes(math.ceil(encrypted_data.bit_length() / 8), "little")
        return result

    def decrypt(self, data: list) -> bytearray:
        # data = split(data, self.public_key.n.bit_length() >> 3)
        result = []
        for unit in data:
            # tmp = int.from_bytes(unit, "little")
            decrypted_data = pow_mod(unit, self.private_key.d, self.private_key.n)
            # a = tmp.bit_length()
            # result = decrypted_data.to_bytes(math.ceil(decrypted_data.bit_length() / 8), "little")
            b = decrypted_data.bit_length()

            # result.append(decrypted_data.to_bytes(math.ceil(decrypted_data.bit_length() / 8), "little"))

            result.append(decrypted_data)
            # result.append(decrypted_data.to_bytes(decrypted_data.bit_length() >> 3, "little"))
        # for substr in result:
        #     substr.replace(b'\x00', b'')
        # return bytearray().join(result)
        return result

    @staticmethod
    def key_gen(key_size: int = 1024, p: int = None, q: int = None):
        """
        Generate public and private keys
        :param key_size: Number of bits to generate P and Q
        :param p: Prime number to generate keys
        :param q: Prime number to generate keys
        :return: Public key and Private key
        """
        if not (p and q):
            p = gen_prime_num(key_size)
            a = p.bit_length()
            q = gen_prime_num(key_size)
            b = q.bit_length()
        n = p * q
        c = n.bit_length()
        phi = (p - 1) * (q - 1)
        while True:
            e = random.randint(2, phi)
            if gcd_ext(e, phi).gcd == 1:
                break

        d = mod_inv(e, phi)

        return RSA.PublicKey(e, n), RSA.PrivateKey(d, n)


msg = "Привет, мир! Как твои дела? Отведай еще этих нежных французских булок да выпей чаю! test strока Мир, привет!"
keys = RSA.key_gen(256)
obj = RSA(*keys)
msg_bytes = bytes(msg, encoding="UTF-8")
print(obj.public_key.n.bit_length() >> 3)
print([int.from_bytes(_, "little").bit_length() for _ in split(msg_bytes, obj.public_key.n.bit_length() >> 3)])
print([int.from_bytes(_, "little") for _ in split(msg_bytes, obj.public_key.n.bit_length() >> 3)])
enc_msg = RSA.encrypt(obj, msg_bytes)

print("msg =", msg)
print(len(msg.encode()))
print("msg_bytes =", msg_bytes)
print("Encrypted")
print(enc_msg)
print("Decrypted")
dec_msg = RSA.decrypt(obj, enc_msg)
print(dec_msg)
print([_.bit_length() for _ in dec_msg])
# dec_msg = dec_msg.decode(encoding="UTF-8", errors="replace")
# print(dec_msg)
