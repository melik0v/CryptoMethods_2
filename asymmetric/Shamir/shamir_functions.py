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
from math import ceil


class Keys(NamedTuple):
    public: any
    private: any


class Shamir:

    @dataclass(frozen=True)
    class PublicKey:
        p: int

    @dataclass(frozen=True)
    class PrivateKey:
        c: int
        d: int

    def __init__(self, public_key: PublicKey = None, private_key: PrivateKey = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def keys_gen(size: int = 512, p: int = None):
        if not p:
            p = gen_prime_num(size)
        while True:
            c = randint(3, p - 2)
            if gcd_ext(c, p - 1).gcd == 1:
                break
        d = mod_inv(c, p - 1)
        return Keys(Shamir.PublicKey(p), Shamir.PrivateKey(c, d))

    def encrypt(self, data: bytes, addition: bool = False) -> bytearray:

        if addition:
            block_size_add = 1
        else:
            block_size_add = 0

        block_size = ceil(self.public_key.p.bit_length() // 8) + block_size_add
        data = split(data, block_size - 1)
        result = []
        for index, block in enumerate(data):
            block = int.from_bytes(block, "little")
            encrypted_data = pow_mod(block, self.private_key.c, self.public_key.p)
            encrypted_bytes = encrypted_data.to_bytes(ceil(encrypted_data.bit_length() / 8), "little")
            result.append(encrypted_bytes)
        return bytearray().join(result)

    def decrypt(self, data: bytearray):
        block_size = ceil(self.public_key.p.bit_length() / 8)
        data = split(data, block_size)
        result = []
        for index, block in enumerate(data):
            block = int.from_bytes(block, "little")
            decrypted_data = pow_mod(block, self.private_key.d, self.public_key.p)
            decrypted_bytes = decrypted_data.to_bytes(ceil(decrypted_data.bit_length() / 8), "little")
            result.append(decrypted_bytes)
        return bytearray().join(result)


# p = gen_prime_num(64)
# msg = "Привет, Мир!"
# # print(msg)
# msg = msg.encode("UTF-8")
# # msg = b"\x01\x02"
# print(msg)
# a_keys = Shamir.keys_gen(p=p)
# b_keys = Shamir.keys_gen(p=p)
# print("A", a_keys)
# print("B", b_keys)
# A = Shamir(*a_keys)
# B = Shamir(*b_keys)
#
# x1 = A.encrypt(msg)
# print("x1 =", x1)
# print("x1` =", A.decrypt(x1))
#
# x2 = B.encrypt(x1, 1)
# print("x2 =", x2)
# print("x2` =", B.decrypt(x2))
#
# x3 = A.decrypt(x2)
# print("x3 =", x3)
# print("x3` =", B.encrypt(msg))
#
# x4 = B.decrypt(x3)
# print("x4 =", x4)
# print(x4.decode("UTF-8"))
