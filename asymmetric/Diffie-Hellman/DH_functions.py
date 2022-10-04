from tools.utils import (
    pow_mod
)
from typing import NamedTuple
from random import randint
from dataclasses import dataclass


class Keys(NamedTuple):
    public: int
    private: int


class DH:

    @dataclass(frozen=True)
    class PublicKey:
        key: int
        p: int
        g: int

    @dataclass(frozen=True)
    class PrivateKey:
        key: int

    @dataclass(frozen=True)
    class SessionKey:
        key: int

        def __str__(self):
            return str(self.key)

    def __init__(self, public_key: PublicKey = None, private_key: PrivateKey = None):
        self.private_key = private_key
        self.public_key = public_key
        self.session_key = None

    def __str__(self):
        return "Public key = {0}\nPrivate key = {1}".format(self.public_key, self.private_key)

    @staticmethod
    def key_gen(p: int, g: int) -> Keys:
        """
        Generate private and public keys for one participant.

        :param p: Prime number
        :param g: The primitive root modulo p
        :return: Tuple (PrivateKey, PublicKey)
        """
        a = randint(1, 10**25)
        return Keys(DH.PublicKey(pow_mod(g, a, p), p, g).key, DH.PrivateKey(a).key)

    def gen_session_key(self, remote_key: int, p: int):
        """
        Generate shared session key.

        :param remote_key: Received public key from another participant.
        :param p: Module
        :return: Shared session key
        """
        self.session_key = DH.SessionKey(pow_mod(remote_key, self.private_key, p))
        return self.session_key


# p = gen_prime_num(96)
# g = primitive_root(p)
# print(g)
#
# alice_keys = DH.key_gen(p, g)
# bob_keys = DH.key_gen(p, g)
#
# Alice = DH(*alice_keys)
# print("Alice\n", Alice)
#
# Bob = DH(*bob_keys)
# print("Bob\n", Bob)
# print()
# print("Alice session key =", Alice.gen_session_key(bob_keys.public, p))
# print("Bob session key =", Bob.gen_session_key(alice_keys.public, p))


