from dataclasses import dataclass
from tools.utils import (
    gen_prime_num,
    sdm
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
            p = gen_prime_num()
            q = gen_prime_num()
        n = p * q
        v_list = sdm(n, count)

        return Keys(Make.PublicKey(v_list, n), Make.PrivateKey())


print(Make.key_gen())
