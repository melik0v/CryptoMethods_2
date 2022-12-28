import random

from hash.GOST94.gost94_functions import GOST94
from dataclasses import dataclass
from typing import NamedTuple
from tools.utils import (
    gen_prime_num,
    mod_inv,
    is_prime
)
from random import randint


class SignatureError(Exception):
    pass


@dataclass(frozen=False)
class Params:
    p: int
    q: int
    a: int


class Keys(NamedTuple):
    public: any
    private: any


class GOSTSignature:
    def __init__(self, params, data: str or bytes, mode: str = 'text'):
        match mode:
            case 'text':
                self.data = bytes(data, encoding="UTF-8")
            case 'file':
                with open(data, 'rb') as file:
                    self.data = file.read()
            case 'bytes':
                self.data = data
            case _:
                raise SignatureError("Wrong mode! Only available 'text' and 'file' modes.")

        self.a = GOST94(self.data, mode)
        self.params = params
        self.keys = self.gen_keys()

    @staticmethod
    def gen_public_params():
        """
        Generate public parameters for users

        :return: Tuple of parameters
        """
        p = gen_prime_num(512)
        while True:
            q = gen_prime_num(256)
            # p = 2 ** 256 * q + 1
            if (p - 1) % q == 0:
            # if is_prime(p):
                while True:
                    a = randint(1, 10**100)
                    if pow(a, q, p) == 1:
                        break

                return Params(p, q, a)

    def gen_keys(self):
        x = randint(1, self.params.q)
        y = pow(self.params.a, x, self.params.p)
        return Keys(y, x)

    def sign(self):
        digest = int.from_bytes(bytes(self.a.generate_hash(), encoding="UTF-8"), "little")
        length = (self.params.p.bit_length() >> 3) + 1
        while True:
            k = randint(1, self.params.q)
            r = pow(self.params.a, k, self.params.p)
            if r != 0:
                break
        s = (k * digest + self.keys.private * r) % self.params.q
        return self.data, r.to_bytes(length, "little") + s.to_bytes(length, "little")

    def _get_values(self, received_data):
        """
        Get r, s and hash from received message
        :return: (r, s, hash)
        """
        length = (self.params.p.bit_length() >> 3) + 1
        r = int.from_bytes(received_data[-(length * 2):-length], "little")
        s = int.from_bytes(received_data[-length:], "little")
        new_hash = int.from_bytes(bytes(self.get_hash(received_data), encoding="UTF-8"), "little")
        msg = int.from_bytes(received_data[:-(2 * length)], 'little')
        return msg, r, s, new_hash

    def get_hash(self, received_data):
        """
            Get hash from received signed message
        """
        length = (self.params.p.bit_length() >> 3) + 1
        return GOST94(received_data[:-(2 * length)], "bytes").generate_hash()

    def check_sign(self, received_data, public_key):
        msg, r, s, new_hash = self._get_values(received_data)
        if r > self.params.q or s > self.params.q:
            return False
        u1 = (s * mod_inv(new_hash, self.params.q))
        u2 = -msg * mod_inv(new_hash, self.params.q)
        v = (pow(self.params.a, u1, self.params.p) * pow(public_key, u1, self.params.p)) % self.params.q
        if v == r:
            return True
        return False


if __name__ == "__main__":
    msg = "C:\\Users\\PYCTAM\\Desktop\\CryptoMethods\\gui\\eg_signature\\eg_signature_ui.ui"
    print(msg)
    params = GOSTSignature.gen_public_params()
    obj = GOSTSignature(params, msg, 'file')
    sent_msg = obj.sign()
    print(sent_msg)
    print(obj.check_sign(sent_msg, obj.keys.public))
