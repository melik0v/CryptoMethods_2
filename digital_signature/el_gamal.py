from asymmetric.El_Gamal.ElGamal_functions import ElGamal
from hash.md5.md5_functions import MD5
from tools.utils import (
    mod_inv
)


class EGSignatureError(Exception):
    pass


class ElGamalSignature:
    def __init__(self, data: str or bytes, mode: str = 'text'):
        match mode:
            case 'text':
                self.data = bytes(data, encoding="UTF-8")
            case 'file':
                with open(data, 'rb') as file:
                    self.data = file.read()
            case 'bytes':
                self.data = data
            case _:
                raise EGSignatureError("Wrong mode! Only available 'text' and 'file' modes.")

        self.hash = MD5(data, mode).generate_hash()
        self.keys = ElGamal.keys_gen(32)
        self.obj = ElGamal(*self.keys)

    def sign(self):
        session_key = self.obj.session_key.key
        modulo = self.obj.public_key.p
        length = (modulo.bit_length() >> 3) + 1
        _hash = int.from_bytes(bytes(self.hash, encoding="UTF-8"), "little")
        r = pow(self.obj.public_key.g, session_key,  self.obj.public_key.p)
        s = ((_hash - self.obj.private_key.x * r) * mod_inv(session_key, modulo - 1)) % (modulo - 1)
        return self.data + r.to_bytes(length, "little") + s.to_bytes(length, "little")

    def get_hash(self, received_data):
        """
            Get hash from received signed message
        """
        modulo = self.obj.public_key.p
        length = (modulo.bit_length() >> 3) + 1
        return MD5(received_data[:-(2 * length)], "bytes").generate_hash()

    def _get_values(self, received_data):
        """
        Get r, s and hash from received message
        :return: (r, s, hash)
        """
        length = (self.obj.public_key.p.bit_length() >> 3) + 1

        r = int.from_bytes(received_data[-(length * 2):-length], "little")
        s = int.from_bytes(received_data[-length:], "little")
        new_hash = int.from_bytes(bytes(self.get_hash(received_data), encoding="UTF-8"), "little")
        return r, s, new_hash

    def check_sign(self, received_data: bytes, public_key: ElGamal.PublicKey) -> bool:
        r, s, new_hash = self._get_values(received_data)
        modulo = public_key.p
        if not (0 < r < modulo) or not (0 < s < modulo - 1):
            return False
        result = (pow(public_key.y, r, modulo) * pow(r, s, modulo)) % modulo
        return result == pow(public_key.g, new_hash, modulo)


if __name__ == "__main__":
    msg = "C:\\Users\\PYCTAM\\Desktop\\CryptoMethods\\gui\\eg_signature\\eg_signature_ui.ui"
    print(msg)
    obj = ElGamalSignature(msg, "file")
    sent_msg = obj.sign()
    print(sent_msg)
    print(obj.check_sign(sent_msg, obj.keys.public))
