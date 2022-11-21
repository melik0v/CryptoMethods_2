import os.path

from tools.utils import (
    gen_prime_num,
    is_prime
)
from os import path
from PyQt6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog
)

from asymmetric.rsa.rsa_functions import RSA
from rsa_ui import Ui_MainWindow


class Make(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.obj = RSA()
        self.input_file_path = ""
        self.widget = QWidget()
        self.functions()

    def functions(self):
        self.gen_p_q_btn.clicked.connect(self._gen_p_q_btn_clicked)
        self.gen_keys_btn.clicked.connect(self._gen_keys_btn_clicked)
        self.input_file_btn.clicked.connect(self._input_file_btn_clicked)
        self.encrypt_btn.clicked.connect(self._encrypt_btn_clicked)
        self.decrypt_btn.clicked.connect(self._decrypt_btn_clicked)

    def _gen_keys_btn_clicked(self):
        try:
            p = int(self.lineEdit_p.text())
            q = int(self.lineEdit_q.text())
            if not (is_prime(p, 100) and is_prime(q, 100)):
                QMessageBox.warning(self.widget, "Warning", "P must be a prime number")
                return
        except ValueError:
            QMessageBox.warning(self.widget, "Warning", "P must be a prime number")
            return
        keys = self.obj.key_gen(p=p, q=q)
        self.obj = RSA(*keys)
        self.lineEdit_n.setText(str(p * q))
        self.lineEdit_public_key.setText(str(self.obj.public_key.e))
        self.lineEdit_private_key.setText(str(self.obj.private_key.d))

    def _gen_p_q_btn_clicked(self):
        size = self.spinBox_key_len.value()
        p = gen_prime_num(size)
        q = gen_prime_num(size)
        n = p * q
        self.lineEdit_p.setText(str(p))
        self.lineEdit_q.setText(str(q))
        self.lineEdit_n.setText(str(n))

    def _input_file_btn_clicked(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not file:
            self.input_path.setText("NO INPUT FILE")
        else:
            self.input_path.setText(path.basename(file))
            self.input_file_path = file

    def _encrypt_btn_clicked(self):
        if self.input_file_path:
            with open(self.input_file_path, "rb") as file:
                data = file.read()
                filename = path.basename(self.input_file_path)
                filename, extention = os.path.splitext(filename)

            encrypted_data = self.obj.encrypt(data)

            with open(self.input_file_path.replace(filename, "Encrypted"), "wb") as file:
                file.write(encrypted_data)

        elif self.text_edit.toPlainText():
            data = self.text_edit.toPlainText()
            data = bytes(data, "ANSI")
            encrypted_data = self.obj.encrypt(data)
            self.textBrowser_encrypted.setText(encrypted_data.decode("ANSI"))

        QMessageBox.warning(self.widget, "Notification", "Encrypted!")

    def _decrypt_btn_clicked(self):
        if self.input_file_path:
            with open(self.input_file_path, "rb") as file:
                data = file.read()
                filename = path.basename(self.input_file_path)
                filename, extention = os.path.splitext(filename)

            decrypted_data = self.obj.decrypt(data)

            with open(self.input_file_path.replace(filename, "Decrypted"), "wb") as file:
                file.write(decrypted_data)

        elif self.text_edit.toPlainText():
            data = self.text_edit.toPlainText()
            data = bytes(data, "ANSI")
            encrypted_data = self.obj.decrypt(data)
            self.textBrowser_encrypted.setText(encrypted_data.decode("ANSI"))

        QMessageBox.warning(self.widget, "Notification", "Decrypted!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
