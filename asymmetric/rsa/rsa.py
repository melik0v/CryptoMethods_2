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

from rsa_functions import RSA
from rsa_ui import Ui_MainWindow


class Make(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.widget = QWidget()
        self.functions()

    def functions(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
