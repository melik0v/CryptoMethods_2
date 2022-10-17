import math

from tools.utils import (
    pow_mod,
    primitive_root,
    gen_prime_num,
    gcd_ext,
    mod_inv,
    split
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

    def __init__(self, public_key: PublicKey = None, private_key: PrivateKey = None):

        if not (public_key and private_key):
            public_key = None
            private_key = None

        self.public_key = public_key
        self.private_key = private_key
        if not public_key:
            self.session_key = None
        else:
            self.session_key = self.gen_session_key()

    def __str__(self):
        return "Public key = {0}\nPrivate key = {1}\nSession_key = {2}".format(self.public_key, self.private_key,
                                                                               self.session_key)

    def gen_session_key(self):
        tmp = self.public_key.p - 1
        while True:
            k = randint(2, tmp)
            if gcd_ext(k, tmp).gcd == 1:
                break
        return ElGamal.SessionKey(k)

    def encrypt(self, data: bytes, public_key: PublicKey) -> bytearray:
        self.session_key = self.gen_session_key()
        length = len(data)
        block_size = math.ceil(self.public_key.p.bit_length() / 8)
        data = split(data, block_size - 1)
        result = []
        for block in data:
            block = int.from_bytes(block, "little")

            a = pow_mod(public_key.g, self.session_key.key, public_key.p)
            b = (pow_mod(public_key.y, self.session_key.key, public_key.p) * block) % public_key.p
            encrypted_bytes = a.to_bytes(block_size, "little") + b.to_bytes(block_size, "little")
            result.append(encrypted_bytes)

        return bytearray().join(result) + bytearray(length.to_bytes(8, "little"))

    def decrypt(self, data: bytes) -> bytearray:
        length = int.from_bytes(data[-8:], "little")
        data = data[:-8]
        block_size = math.ceil(self.public_key.p.bit_length() / 8)
        data = split(data, block_size * 2)
        result = []
        for index, block in enumerate(data):
            a = int.from_bytes(block[:block_size], "little")
            b = int.from_bytes(block[block_size:], "little")
            tmp = mod_inv(pow_mod(a, self.private_key.x, self.public_key.p), self.public_key.p)
            decrypted = (b * tmp) % self.public_key.p
            decrypted_bytes = decrypted.to_bytes(block_size, "little")[:-1]

            result.append(decrypted_bytes)
        return bytearray().join(result)[:length]


# with open("Шаблон уведомления.docx", "rb") as file:
#     msg = file.read()
#
# keys = ElGamal.keys_gen(64)
# obj = ElGamal(*keys)
# enc_msg = obj.encrypt(msg, keys.public)
# dec_msg = obj.decrypt(enc_msg)
#
# with open("Decrypted.docx", "wb") as file:
#     file.write(dec_msg)
#
# print(msg[:100])
# print(dec_msg[:100])
#
# for index, (s1, s2) in enumerate(zip(msg, dec_msg)):
#     if s1 != s2:
#         print(index)
#         print(msg[index - 3:index + 3])
#         print(dec_msg[index - 3:index + 3])
#         break


# msg = b"\x00\x00\x00\x00\x00\x00\x00\x01"
# print(msg)
# # msg = bytes(msg, encoding="UTF-8")
# # print(msg)
# # print(int.from_bytes(msg, "little"))
# keys = ElGamal.keys_gen(64)
#
# print(keys)
# obj = ElGamal(*keys)
# enc_msg = ElGamal.encrypt(obj, msg, keys.public)
# print("Encrypted =", enc_msg)
# dec_msg = ElGamal.decrypt(obj, enc_msg)
# print("Decrypted =", dec_msg)
# # print(dec_msg.decode("UTF-8"))
# print(len(msg))
# print(len(enc_msg))
# print(len(dec_msg))
