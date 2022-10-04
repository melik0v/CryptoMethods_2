from tools.utils import (
    pow_mod,
    primitive_root,
    gen_prime_num,
    gcd_ext,
    mod_inv
)
from typing import NamedTuple
from random import randint
from dataclasses import dataclass


class CypherText(NamedTuple):
    a: int
    b: int


class Keys(NamedTuple):
    public: any
    private: any


class ElGamal:

    @dataclass(frozen=True)
    class PublicKey:
        y: int
        g: int
        p: int

    @dataclass(frozen=True)
    class PrivateKey:
        x: int

    @dataclass(frozen=True)
    class SessionKey:
        key: int

    @staticmethod
    def keys_gen(size: int = 128, p: int = None):
        if not p:
            p = gen_prime_num(size)
        g = primitive_root(p)
        x = randint(1, p - 1)
        y = pow_mod(g, x, p)
        return Keys(ElGamal.PublicKey(y, g, p), ElGamal.PrivateKey(x))

    def __init__(self, public_key: PublicKey, private_key: PrivateKey):
        self.public_key = public_key
        self.private_key = private_key

    def __str__(self):
        return "Public key = {0}\nPrivate key = {1}".format(self.public_key, self.private_key)

    def gen_session_key(self):
        tmp = self.public_key.p - 1
        while True:
            k = randint(2, tmp)
            if gcd_ext(k, tmp).gcd == 1:
                break
        return ElGamal.SessionKey(k)

    def encrypt(self, data: bytes) -> CypherText:
        session_key = self.gen_session_key()
        a = pow_mod(self.public_key.g, session_key.key, self.public_key.p)
        data = int.from_bytes(data, "little")
        b = (pow_mod(self.public_key.y, session_key.key, self.public_key.p) * data) % self.public_key.p
        # block_size = self.public_key.p.bit_length() >> 3
        return CypherText(a, b)

    def decrypt(self, data: CypherText) -> bytes:
        tmp = mod_inv(pow_mod(data.a, self.private_key.x, self.public_key.p), self.public_key.p)
        decrypted_data = (data.b * tmp) % self.public_key.p
        result = decrypted_data.to_bytes((decrypted_data.bit_length() >> 3) + 1, "little")
        return result


msg = "Привет, мир!"
print(msg)
msg = bytes(msg, encoding="UTF-8")
print(msg)
print(int.from_bytes(msg, "little"))
keys = ElGamal.keys_gen(192)
print(keys)
obj = ElGamal(*keys)
enc_msg = ElGamal.encrypt(obj, msg)
print("Encrypted =", enc_msg)
dec_msg = ElGamal.decrypt(obj, enc_msg)
print("Decrypted =", dec_msg)
print(msg.decode("UTF-8"))
