from bitarray import bitarray
from bitarray.util import int2ba
from tools.constants import A, Pi, Tau, C


class StribogError(Exception):
    pass

class Stribog:
    def __init__(self, data: bytes, out_len: int = 256):
        self.n = bytearray(0x00 * 64)
        self.sigma = bytearray(0x00 * 64)

        match out_len:
            case 256:
                self.iv = bytearray(0x01 * 64)
            case 512:
                self.iv = bytearray(0x00 * 64)
            case _:
                raise StribogError("Wrong output length! Only allowed 256 or 512 bytes")

    @staticmethod
    def _append_padding(a, b):
        a = bytearray(a)
        b = bytearray(b)
        cb = 0
        result = bytearray(64)
        for i in range(64):
            cb = a[i] + b[i] + (cb >> 8)
            result[i] = cb & 0xff
        return result


    def x_func(self, seq_1, seq_2):
        return seq_1 ^ seq_2

    def s_func(self, seq):
        return [Pi[int.from_bytes(i, "little")] for i in seq.reverse]

    def p_func(self, seq):
        return [Tau[i] for i in enumerate(seq)]

    def l_func(self, seq):
        for i in range(0, 56, 8):
            tmp = seq[i:i + 8]
            tmp = bitarray(tmp)
