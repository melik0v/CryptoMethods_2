from bitarray import bitarray
from bitarray.util import int2ba
from tools.constants import ABCDE


class SHA1:
    def __init__(self, data, mode='text'):
        self.data = bitarray()
        match mode:
            case 'text':
                self.data.frombytes(data.encode('utf-8'))
            case 'file':
                with open(data, 'rb') as file:
                    self.data.fromfile(file)

    def generate_hash(self):
        self.__append_padding()
        self.data = [int.from_bytes(self.data[i:i + 32].tobytes(), byteorder='big')
                     for i in range(0, len(self.data), 32)]
        a0, b0, c0, d0, e0 = ABCDE

        def f_1(x, y, z):
            return (x & y) | (~x & z)

        def f_2(x, y, z):
            return x ^ y ^ z

        def f_3(x, y, z):
            return (x & y) | (x & z) | (y & z)

        modulo = pow(2, 32)

        for _ in range(len(self.data) // 16):
            a, b, c, d, e = a0, b0, c0, d0, e0

            w = self.data[:16]
            w += [None] * 64
            for i in range(16, 80):
                w[i] = (((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) << 1) |
                        ((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]) >> 32 - 1)) % modulo

            for n, (f, k) in enumerate(((f_1, 0x5A827999),
                                        (f_2, 0x6ED9EBA1),
                                        (f_3, 0x8F1BBCDC),
                                        (f_2, 0xCA62C1D6))):
                for i in range(20):
                    tmp = f(b, c, d)
                    tmp = (tmp + ((a << 5) | (a >> 27))) % modulo
                    tmp = (tmp + e) % modulo
                    tmp = (tmp + k) % modulo
                    tmp = (tmp + w[n * 20 + i]) % modulo

                    a, b, c, d, e = tmp, a, (b << 30) | (b >> 2), c, d

            self.data = self.data[16:]

            a0 = (a + a0) % modulo
            b0 = (b + b0) % modulo
            c0 = (c + c0) % modulo
            d0 = (d + d0) % modulo
            e0 = (e + e0) % modulo

        sha1_hash = []
        for block in (a0, b0, c0, d0, e0):
            sha1_hash += hex(int.from_bytes(int2ba(block, length=32).tobytes(), byteorder='big'))[2:].zfill(8)

        return ''.join(sha1_hash)

    def __append_padding(self):
        """
        Adding missing bit. The message is supplemented in such a way that its length becomes equal to 448 modulo 512.
        """
        length = len(self.data)
        length_bits = bitarray(int2ba(length, 64))
        self.data += bitarray('1') + (448 - 1 - length % 512) * bitarray('0') + length_bits


msg = "Hello, world! Привет, Мир!"
a = SHA1(msg)
a = a.generate_hash()
print(a)
print(a == "6243ba8289f18d6186179a9d62ef52c50854d154")
a = SHA1("C://Users//PYCTAM//Desktop//CryptoMethods//asymmetric//rsa//РД АС.pdf", mode="file")
print(a.generate_hash())
