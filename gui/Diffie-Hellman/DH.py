from tools.utils import (
    gen_prime_num,
    primitive_root,
    is_prime
)
from PyQt6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget
)
from asymmetric.Diffie_Hellman.DH_functions import DH
from DH_ui import Ui_MainWindow


class Make(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.bob = DH()
        self.alice = DH()
        self.setupUi(self)
        self.widget = QWidget()
        self.functions()

    def functions(self):
        self.gen_btn.clicked.connect(self._gen_btn_clicked)
        self.post_key_btn.clicked.connect(lambda: self._post_key_btn_clicked())
        self.session_key_btn.clicked.connect(lambda: self._session_key_btn_clicked(self.alice, self.bob))
        self.p_gen_btn.clicked.connect(lambda: self._p_gen_btn_clicked())

    def _gen_btn_clicked(self):
        try:
            p = int(self.lineEdit_p.text())
            g = int(self.lineEdit_g.text())
        except ValueError:
            QMessageBox.warning(self.widget, "Warning", "P and G must be integer numbers")
            return

        # Alice
        alice_keys = DH.key_gen(p, g)
        self.alice = DH(*alice_keys)
        self.lineEdit_private_key.setText(str(alice_keys.private))
        self.lineEdit_public_key.setText(str(alice_keys.public))

        # Bob
        bob_keys = DH.key_gen(p, g)
        self.bob = DH(*bob_keys)
        self.lineEdit_private_key_2.setText(str(bob_keys.private))
        self.lineEdit_public_key_2.setText(str(bob_keys.public))

    def _p_gen_btn_clicked(self):
        p = gen_prime_num(self.key_size_spinBox.value())
        g = primitive_root(p)

        self.lineEdit_p.setText(str(p))
        self.lineEdit_g.setText(str(g))

    def _post_key_btn_clicked(self):
        self.lineEdit_recieved_key.setText(self.lineEdit_public_key_2.text())
        self.lineEdit_recieved_key_2.setText(self.lineEdit_public_key.text())

    def _session_key_btn_clicked(self, participant_1: DH, participant_2: DH):

        try:
            p = int(self.lineEdit_p.text())
        except ValueError:
            QMessageBox.warning(self.widget, "Warning", "The value of P must not be empty")
            return

        if not is_prime(p, 100):
            QMessageBox.warning(self.widget, "Warning", "P must be a prime number")
            return

        try:
            participant_1.gen_session_key(int(self.lineEdit_recieved_key.text()), p)
            participant_2.gen_session_key(int(self.lineEdit_recieved_key_2.text()), p)
        except ValueError:
            QMessageBox.warning(self.widget, "Warning", "Check the correctness of recieved keys")
            return

        if participant_1.session_key != participant_2.session_key:
            QMessageBox.warning(self.widget, "Warning", "Check the correctness of recieved keys")
            return

        if not (self.lineEdit_private_key.text() and self.lineEdit_private_key_2.text()):
            QMessageBox.warning(self.widget, "Warning", "The value of private keys must not be empty")
            return

        self.alice_session_key.setPlainText(str(participant_1.session_key))
        self.bob_session_key.setPlainText(str(participant_2.session_key))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
