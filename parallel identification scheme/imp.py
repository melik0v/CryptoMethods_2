from dataclasses import dataclass
from tools.utils import (
    gen_prime_num,
    sdm,
    sqrt_mod
)
from typing import NamedTuple


class Keys(NamedTuple):
    public: any
    private: any


class Make:
    @dataclass(frozen=True)
    class PublicKey:
        v: tuple[int]
        n: int

    @dataclass(frozen=True)
    class PrivateKey:
        s: tuple[int]

    @staticmethod
    def key_gen(count: int = 10, p: int = None, q: int = None) -> (PublicKey, PrivateKey):
        if not (p and q):
            p = gen_prime_num(16)
            q = gen_prime_num(16)
        n = p * q
        v_list = sdm(n, count)
        s_list = []
        for v in v_list:
            s_list.append(sqrt_mod(v, n))

        return Keys(Make.PublicKey(v_list, n), Make.PrivateKey(tuple(s_list)))


print(Make.key_gen())
