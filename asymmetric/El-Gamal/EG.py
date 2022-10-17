from tools.utils import (
    gen_prime_num,
    is_prime,
    primitive_root
)
from os import path
from PyQt6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog
)

from ElGamal_functions import ElGamal
from EG_ui import Ui_MainWindow


class Make(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.alice = ElGamal()
        self.bob = ElGamal()
        self.input_file_path = ""
        self.widget = QWidget()
        self.functions()

    def functions(self):
        self.p_gen_btn.clicked.connect(self._gen_p_btn_clicked)
        self.gen_btn.clicked.connect(self._gen_keys_btn_clicked)
        self.encrypt_btn.clicked.connect(self._encrypt_btn_clicked)
        self.decrypt_btn.clicked.connect(self._decrypt_btn_clicked)
        self.input_file_btn.clicked.connect(self._input_file_btn_clicked)

    def _input_file_btn_clicked(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not file:
            self.input_path.setText("NO INPUT FILE")
        else:
            self.input_path.setText(path.basename(file))
            self.input_file_path = file

    def _gen_keys_btn_clicked(self):
        try:
            p = int(self.lineEdit_p.text())
            if not (is_prime(p, 100)):
                QMessageBox.warning(self.widget, "Warning", "P must be a prime number")
                return
        except ValueError:
            QMessageBox.warning(self.widget, "Warning", "P must be a prime number")
            return
        keys_alice = self.alice.keys_gen(p=p)
        keys_bob = self.bob.keys_gen(p=p)
        self.alice = ElGamal(*keys_alice)
        self.bob = ElGamal(*keys_bob)

        self.lineEdit_public_key.setText(str(self.alice.public_key.y))
        self.lineEdit_private_key.setText(str(self.alice.private_key.x))
        self.lineEdit_session_key.setText(str(self.alice.session_key.key))

        self.lineEdit_public_key_2.setText(str(self.bob.public_key.y))
        self.lineEdit_private_key_2.setText(str(self.bob.private_key.x))
        self.lineEdit_session_key_2.setText(str(self.bob.session_key.key))

    def _gen_p_btn_clicked(self):
        size = self.key_size_spinBox.value()
        if size % 8 != 0:
            QMessageBox.warning(self.widget, "Warning", "Key length must be multiple of 8")
            return
        p = gen_prime_num(size)
        g = primitive_root(p)
        self.lineEdit_p.setText(str(p))
        self.lineEdit_g.setText(str(g))

    def _encrypt_btn_clicked(self):
        if not (self.bob.public_key and self.alice.public_key):
            QMessageBox.warning(self.widget, "Warning", "Keys are undefined!")
            return
        if self.input_file_path:
            with open(self.input_file_path, "rb") as file:
                data = file.read()
                filename = path.basename(self.input_file_path)
                filename, extension = path.splitext(filename)

            encrypted_data = self.alice.encrypt(data, self.bob.public_key)

            with open(self.input_file_path.replace(filename, "Encrypted"), "wb") as file:
                file.write(encrypted_data)

        elif self.text_edit.toPlainText():
            data = self.text_edit.toPlainText()
            data = bytes(data, "ANSI")
            encrypted_data = self.alice.encrypt(data, self.bob.public_key)
            self.text_browser.setText(encrypted_data.decode("ANSI"))

        QMessageBox.warning(self.widget, "Notification", "Encrypted!")

    def _decrypt_btn_clicked(self):
        if self.input_file_path:
            with open(self.input_file_path, "rb") as file:
                data = file.read()
                filename = path.basename(self.input_file_path)
                filename, extension = path.splitext(filename)

            decrypted_data = self.bob.decrypt(data)

            with open(self.input_file_path.replace(filename, "Decrypted"), "wb") as file:
                file.write(decrypted_data)

        elif self.text_edit.toPlainText():
            data = self.text_edit.toPlainText()
            data = bytes(data, "ANSI")
            encrypted_data = self.bob.decrypt(data)
            self.text_browser.setText(encrypted_data.decode("ANSI"))

        QMessageBox.warning(self.widget, "Notification", "Decrypted!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
