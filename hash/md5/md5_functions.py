from bitarray import bitarray
from bitarray.util import int2ba
from tools.constants import ABCD, T, K, S_md5


class MD5:

    def __init__(self, data, mode='text'):
        self.data = bitarray()
        match mode:
            case 'text':
                self.data.frombytes(data.encode('utf-8'))
            case 'file':
                with open(data, 'rb') as file:
                    self.data.fromfile(file)
            case 'bytes':
                self.data.frombytes(data)

    def generate_hash(self):
        self.__append_padding()
        self.data = [int.from_bytes(self.data[i:i + 32].tobytes(), byteorder='little')
                     for i in range(0, len(self.data), 32)]
        a0, b0, c0, d0 = ABCD

        def f_f(x, y, z):
            return (x & y) | (~x & z)

        def f_g(x, y, z):
            return (x & z) | (~z & y)

        def f_h(x, y, z):
            return x ^ y ^ z

        def f_i(x, y, z):
            return y ^ (~z | x)

        modulo = pow(2, 32)

        for _ in range(len(self.data) // 16):
            a, b, c, d = a0, b0, c0, d0
            for n, f in enumerate((f_f, f_g, f_h, f_i)):
                for i in range(16):
                    tmp = f(b, c, d) % modulo
                    tmp = (tmp + self.data[K[n][i]]) % modulo
                    tmp = (tmp + T[n * 16 + i]) % modulo
                    tmp = (tmp + a) % modulo
                    tmp = (tmp << S_md5[n][i % 4]) | (tmp >> (32 - S_md5[n][i % 4]))
                    tmp = (tmp + b) % modulo

                    a, b, c, d = d, tmp, b, c

            self.data = self.data[16:]

            a0 = (a + a0) % modulo
            b0 = (b + b0) % modulo
            c0 = (c + c0) % modulo
            d0 = (d + d0) % modulo

        md5_hash = []
        for block in (a0, b0, c0, d0):
            md5_hash += hex(int.from_bytes(int2ba(block, length=32).tobytes(), byteorder='little'))[2:]

        return ''.join(md5_hash)

    def __append_padding(self):
        """
        Add missing bit. The message is supplemented in such a way that its length becomes equal to 448 modulo 512.
        Also add length of message (64-bit representation).
        msg = msg + padding + length
        """
        length = len(self.data)
        length_bits = bitarray(int2ba(length, 64))
        length_bits = int2ba(int.from_bytes(length_bits.tobytes(), byteorder='little'), 64)
        self.data += bitarray('1') + (448 - 1 - length % 512) * bitarray('0') + length_bits


if __name__ == "__main__":
    msg = "Привет"
    obj = MD5(msg)
    print(obj.generate_hash())

    # obj = MD5("C://Users//PYCTAM//Desktop//CryptoMethods//gui//rsa//РД АС.pdf", mode="file")
    # print(obj.generate_hash())
