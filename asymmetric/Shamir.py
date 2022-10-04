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

    def __init__(self, public_key: PublicKey, private_key: PrivateKey):
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

    def encrypt(self, data):
        match data:
            case bytes():
                data = int.from_bytes(data, "big")
        encrypted_data = pow_mod(data, self.private_key.c, self.public_key.p)
        # result = encrypted_data.to_bytes((encrypted_data.bit_length() >> 3), "little")
        result = encrypted_data
        return result

    def decrypt(self, data):
        match data:
            case bytes():
                data = int.from_bytes(data, "big")
        decrypted_data = pow_mod(data, self.private_key.d, self.public_key.p)
        a = decrypted_data.bit_length()
        b = decrypted_data.bit_length() >> 3
        result = decrypted_data
        result = decrypted_data.to_bytes((decrypted_data.bit_length() >> 3) + 1, "big")
        return result


p = gen_prime_num(1024)
msg = "Привет"
print(msg)
msg = msg.encode("UTF-8")
# msg = int.from_bytes(msg, "little")
print(msg)
a_keys = Shamir.keys_gen(p=p)
b_keys = Shamir.keys_gen(p=p)
A = Shamir(*a_keys)
B = Shamir(*b_keys)
x1 = A.encrypt(msg)
print(x1)
x2 = B.encrypt(x1)
print(x2)
x3 = A.decrypt(x2)
print(x3)
x4 = B.decrypt(x3).strip()
print(x4)
print(x4.decode("UTF-8"))
