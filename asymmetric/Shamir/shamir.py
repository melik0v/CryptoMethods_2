from tools.utils import (
    gen_prime_num,
    is_prime,
    primitive_root
)
from PyQt6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget,
)

from shamir_functions import Shamir
from shamir_ui import Ui_MainWindow


class Make(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.alice = Shamir()
        self.bob = Shamir()
        self.input_file_path = ""
        self.widget = QWidget()
        self.functions()

    def functions(self):
        self.p_gen_btn.clicked.connect(self._gen_p_btn_clicked)
        self.gen_btn.clicked.connect(self._gen_keys_btn_clicked)
        self.post_btn.clicked.connect(self._post_btn_clicked)

    def _gen_p_btn_clicked(self):
        size = self.key_size_spinBox.value()
        p = gen_prime_num(size)
        self.lineEdit_p.setText(str(p))

    def _gen_keys_btn_clicked(self):
        p = int(self.lineEdit_p.text())
        a_keys = Shamir.keys_gen(p=p)
        b_keys = Shamir.keys_gen(p=p)
        self.alice = Shamir(*a_keys)
        self.bob = Shamir(*b_keys)

        self.lineEdit_public_key.setText(str(self.alice.private_key.c))
        self.lineEdit_private_key.setText(str(self.alice.private_key.d))

        self.lineEdit_public_key_2.setText(str(self.bob.private_key.c))
        self.lineEdit_private_key_2.setText(str(self.bob.private_key.d))

    def _post_btn_clicked(self):
        msg = bytes(self.text_edit.toPlainText(), "UTF-8")

        if not self.alice.public_key:
            return

        x1 = self.alice.encrypt(msg)
        self.lineEdit_x1.setText(str(x1))
        x2 = self.bob.encrypt(x1, True)
        self.lineEdit_x2.setText(str(x2))
        x3 = self.alice.decrypt(x2)
        self.lineEdit_x3.setText(str(x3))
        x4 = self.bob.decrypt(x3)
        self.lineEdit_x4.setText(str(x4))
        self.text_browser.setPlainText(str(x4.decode("UTF-8")))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
