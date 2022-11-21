from asymmetric.rsa.rsa_functions import RSA
from hash.sha1.sha1_functions import SHA1


class SignatureError(Exception):
    pass


class RSASignature:
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
                raise SignatureError("Wrong mode! Only available 'text' and 'file' modes.")

        self.hash = SHA1(data, mode).generate_hash()
        self.keys = RSA.key_gen(160)
        self.obj = RSA(*self.keys)
        self.new_hash = None

    def sign(self):
        signature = self.obj.encrypt(bytes(self.hash, encoding="UTF-8"))
        return self.data + signature + len(signature).to_bytes(4, byteorder="little")

    def get_hash(self, received_data: bytes):
        """
        Get hash from received signed message
        """
        sign_len = int.from_bytes(received_data[-4:], "little")
        received_data = received_data[:-4]
        sign = received_data[-sign_len:]
        return self.obj.decrypt(sign).decode("UTF-8")

    def check_sign(self, received_data: bytes):
        sign_len = int.from_bytes(received_data[-4:], "little")
        received_hash = self.get_hash(received_data)
        received_data = received_data[:-4]
        self.new_hash = SHA1(received_data[:-sign_len], mode="bytes").generate_hash()
        return self.new_hash == received_hash


if __name__ == "__main__":
    # msg = "C://Users//PYCTAM//Desktop//CryptoMethods//gui//rsa//РД АС.pdf"
    msg = ""
    print(msg)
    obj = RSASignature(msg)
    sent_msg = obj.sign()
    print(sent_msg)
    print(obj.check_sign(sent_msg))
