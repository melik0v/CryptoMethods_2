import time
import math
import gmpy2
from . import pyecm
import random
from typing import NamedTuple
from typing import Union


class GCDExt(NamedTuple):
    gcd: int
    x: int
    y: int


def gcd_ext(a: int, b: int) -> GCDExt:
    """
    Extended Euclidus algorithm. Used for calculating coefficients of equation x * number_1 + y * number_2 = divider.

    :param a: integer number
    :param b: integer number
    :return: tuple (divider, x, y)
    """
    s0, s1 = 1, 0
    t0, t1 = 0, 1

    is_swapped = False
    if a < b:
        a, b = b, a
        is_swapped = True

    while b:
        q = a // b
        a, b = b, a % b
        s0, s1 = s1, s0 - s1 * q
        t0, t1 = t1, t0 - t1 * q

    if is_swapped:
        result = GCDExt(a, t0, s0)
    else:
        result = GCDExt(a, s0, t0)

    return result


def sdm(modulo: int, count: int) -> tuple:
    """
    Square detection modulo.

    :param modulo: Modulo.
    :param count: Count of square detections.
    :return: List of first count square detections.
    """
    result = []
    for i in range(2, modulo):
        if gcd_ext(i, modulo).gcd == 1 and pow(i, (modulo - 1 // 2)):
            result.append(i)
        if len(result) == count:
            break

    return tuple(result)


def sqrt_mod(element, modulo):
    pass


def split(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def mod_inv(element: int, module: int):
    """
    Inverse element modulo
    """
    gcd, x, y = gcd_ext(element, module)
    if gcd != 1:
        raise ValueError("Unable to find inverse element. The number and module are not relatively prime!")

    return x % module


def pow_mod(base, power, mod) -> int:
    """
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments.

    Some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form.
    """
    if base == 0 and power == 0:
        return 1
    elif base == 0 and power < 0:
        raise ValueError("base is not invertible for the given modulus")

    n = int(abs(math.log(int(power), 2))) + 1
    digits = list(bin(power)[2:])
    digits.reverse()
    tmp = [base, ]
    result = tmp[0] ** int(digits[0])
    for i in range(1, n):
        element = (tmp[i - 1] ** 2) % mod
        tmp.append(element)
        result *= element ** int(digits[i])
    result = result % mod
    return int(result)


def gen_prime_num(size: int = 128, verbose: bool = False) -> int:
    """
        Generation of a prime number of a given dimension (in bits). Diemitko theorem.

        :param size: required number of bits (default 128).
        :param verbose: detailed output of each generation step (True or False).
        :return: prime number of given dimension.
    """

    q = gmpy2.mpz(3)

    t_list = [gmpy2.mpz(size)]
    while True:
        t = gmpy2.mpz(gmpy2.ceil(t_list[-1] / 2))
        if t > q.bit_length():
            t_list.append(t)
        else:
            break

    t_list = t_list[::-1]
    if verbose:
        print(t_list)
        print()

    all_time = 0
    index = 0
    p = None

    while index < len(t_list):
        begin_t = time.time()
        num_bits = gmpy2.mpz(2 ** (t_list[index] - 1))
        # n1 = gmpy2.mpz(gmpy2.ceil(num_bits / q))
        n1 = gmpy2.mpz(gmpy2.div(num_bits, q))
        n2 = gmpy2.mpz(num_bits / q * gmpy2.mpfr(random.random()))
        n = n1 + n2

        if gmpy2.is_odd(n):
            n += 1

        u = gmpy2.mpz(0)
        while True:
            p = q * (n + u) + 1

            if p > 2 ** t_list[index]:
                break

            if gmpy2.powmod(2, p - 1, p) == 1 and gmpy2.powmod(2, n + u, p) != 1:
                index += 1
                end_t = time.time() - begin_t
                all_time += end_t
                if verbose:
                    print("time =", end_t)
                    print("p =", p)
                    print("q =", q)
                    print("p: num digits =", p.num_digits())
                    print("p: num bits =", p.bit_length())
                    print("q: num digits =", q.num_digits())
                    print("q: num bits =", q.bit_length())
                    print("n =", n)
                    print("u =", u)
                    print("r < 4(q+1):", n + u < 4 * (q + 1))
                    print()
                q = p
                break
            u += 2

    if verbose:
        print("all time =", all_time)
        print()

    return int(p)


def is_prime(n: Union[int, gmpy2.mpz], k=10) -> bool:
    """
    The Miller–Rabin primality test is a probabilistic primality test:
    an algorithm which determines whether a given number is likely to be prime, similar to the Fermat
    primality test and the Solovay–Strassen primality test.

    :param n: The number to check with the test.
    :param k: Count of rounds of testing.
    :return: True if number is prime and False otherwise.
    """
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def euler(n: int):
    """
    Euler function phi(n)
    :param n: Natural number
    :return: Count of mutually prime numbers with n
    """
    pass


def primitive_root(module: int) -> int:
    """
    Calculation of the primitive root modulo

    :param module: Prime number > 2
    :return: primitive root
    """
    if not is_prime(module):
        raise ValueError("Modulo must be prime!")
    phi = module - 1
    factor_list = pyecm.factors(phi, False, False, 1, 1)

    powers = []
    for divider in factor_list:
        powers.append(gmpy2.divexact(phi, divider))

    for root in range(2, module):
        flag = True
        if gmpy2.powmod(root, phi // 2, module) == 1:
            continue
        for power in powers:
            if gmpy2.powmod(root, power, module) == 1:
                flag = False
                break

        if flag and gmpy2.gcd(root, module) == 1:
            return root
