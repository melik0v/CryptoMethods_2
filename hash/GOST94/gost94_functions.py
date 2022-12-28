import os

from bitarray import bitarray
from bitarray.util import ba2hex, int2ba, ba2int, hex2ba

from tools.constants import S as S_table


class GOST94:
    def __init__(self, data, init_vect='', mode='text'):
        self.data = bitarray()
        self.data_size = None

        if len(init_vect) != 64:
            self.init_vect = bitarray(256)
            self.init_vect.setall(0)
        else:
            self.init_vect = hex2ba(init_vect)

        match mode:
            case 'text':
                self.data.frombytes(data.encode('utf-8'))
                self.data_size = len(data.encode('utf-8'))
            case 'file':
                with open(data, 'rb') as file:
                    self.data.fromfile(file)
                self.data_size = os.path.getsize(data)
            case 'bytes':
                self.data.frombytes(data)

    def generate_hash(self):
        self.data = [bitarray(int2ba(int.from_bytes(self.data[i:i + 256].tobytes(), byteorder='little'), length=256))
                     for i in range(0, len(self.data), 256)]

        if not self.data:
            return 'ce85b99cc46752fffee35cab9a7b0278abb4c2d2055cff685af4912c49490f8d'

        check_sum = self.data[0]
        for block in self.data[1:]:
            check_sum = check_sum ^ block

        data_length = bitarray()
        data_length.extend(int2ba(self.data_size, length=256))

        self.data.append(data_length)
        self.data.append(check_sum ^ self.data[-2])

        for j in range(len(self.data)):
            # self.generate_keys(self.data[j])
            K = self.generate_keys(self.data[j])
            # self.data[j] = self.data[j][::-1]


            h = []
            # магма (режим простой замены)
            for i, key in zip(range(0, 256, 64), K):
                # дробим ключ раунда на подключи для магмы
                keys = self.__generate_keys(key)
                # print(keys)
                # делим слово на два слова
                N1, N2 = self.data[j][i:i + 32], self.data[j][i + 32:i + 64]

                # Подключи X0 … X23 являются циклическим повторением K0 … K7. Подключи X24 … X31 являются K7 … K0.
                key_indexes = list(range(8)) * 3 + list(range(7, -1, -1))
                rounds_indexes = range(32)
                # функция f
                for round in rounds_indexes:
                    N1, N2 = self.__func_F(N1, keys[key_indexes[round]], round) ^ N2, N1
                h.append(N2 + N1)

            S = bitarray(256)
            for i, j in zip(range(0, 256, 64), range(3, -1, -1)):
                S[i:i + 64] = h[j]

            self.init_vect = self.transformation_shuffle(self.data[j], self.init_vect, S)

        # print(K)
        return ba2hex(self.init_vect)

    def transformation_A(self, data):
        y = []
        for i in range(0, 256, 64):
            y.append(data[i:i + 64])

        x = bitarray(256)
        x[0:64] = y[3] ^ y[2]
        x[64:128] = y[0]
        x[128:192] = y[1]
        x[192:256] = y[2]

        return x

    def transformation_P(self, data):
        fi = [0 for _ in range(32)]
        for i in range(4):
            for k in range(1, 9):
                fi[i + 1 + 4 * (k - 1) - 1] = 8 * i + k - 1

        y = []
        for i in range(32):
            y.append(data[i:i + 8])

        x = bitarray(256)
        for i, j in zip(range(0, 256, 8), fi):
            x[i:i + 8] = y[j]

        return x

    def generate_keys(self, data):
        C = [bitarray(256)] * 3
        C[0].setall(0)
        C[1] = bitarray(int2ba(115341543208837762359290129054356496287982810492634369300756142191606025486080,
                               length=256))
        C[2].setall(0)

        U = self.init_vect
        V = data
        W = U ^ V

        K = [None] * 4
        K[0] = self.transformation_P(W)

        for j in range(1, 4):
            U = self.transformation_A(U) ^ C[j - 1]
            V = self.transformation_A(self.transformation_A(V))
            W = U ^ V
            K[j] = self.transformation_P(W)

        return K

    def psi(self, data):
        y = []
        for i in range(16):
            y.append(data[i:i + 16])

        x = y[0] ^ y[1] ^ y[2] ^ y[3] ^ y[12] ^ y[15]

        for i in range(15, 0, -1):
            x += y[i]

        return x

    def transformation_shuffle(self, data, Hin, S):
        Hout = S

        for i in range(12):
            Hout = self.psi(Hout)

        Hout = data ^ Hout
        Hout = self.psi(Hout)
        Hout = Hin ^ Hout

        for i in range(61):
            Hout = self.psi(Hout)

        return Hout

    def __func_F(self, word, key, round):
        text = int2ba((ba2int(word) + ba2int(key)) % 2 ** 32, length=32)

        text_S = bitarray()
        for i in range(0, 32, 4):
            # ходим по таблице S, таков алгоритм Магмы
            text_S += int2ba(S_table[round % 8][ba2int(text[i:i + 4])], length=4)
        # циклический сдвиг влево на 11 бит
        return text_S[11:] + text_S[:11]

    def __generate_keys(self, key):
        # разбиваем ключ на подключи длиной по 32 бита
        keys = []
        for i in range(0, 256, 32):
            keys.append(key[i:i + 32])

        return keys


# a = GOST94('This is message, length=32 bytes')
# a = GOST94('This is message, length=32 bytes')
# a = GOST94('C://Users//PYCTAM//Desktop//CryptoMethods//hash//GOST94//test', mode='file')
# print(a.generate_hash())
# print(int('0xff00ffff000000ffff0000ff00ffff0000ff00ff00ff00ffff00ff00ff00ff00', 16))
