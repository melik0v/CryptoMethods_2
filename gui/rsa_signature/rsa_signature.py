from digital_signature.rsa import RSASignature
from gui.rsa_signature.rsa_signature_ui import Ui_MainWindow

from os import path
from PyQt6.QtWidgets import (
    QMessageBox,
    QApplication,
    QMainWindow,
    QWidget,
    QFileDialog
)


class Make(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.obj = None
        self.input_file_path = ""
        self.widget = QWidget()
        self.functions()

    def functions(self):
        self.InputFile_btn.clicked.connect(self._input_file_btn_clicked)
        self.sign_btn.clicked.connect(self._sign_btn_clicked)
        self.post_btn.clicked.connect(self._post_btn_clicked)
        self.check_sign_btn.clicked.connect(self._check_sign_btn_clicked)

    def _input_file_btn_clicked(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not file:
            self.input_path.setText("NO INPUT FILE")
        else:
            self.input_path.setText(path.basename(file))
            self.input_file_path = file

    def _sign_btn_clicked(self):
        if not self.input_file_path:
            data = self.lineEdit_msg.text()
            self.obj = RSASignature(data)

        else:
            data = self.input_file_path
            self.obj = RSASignature(data, "file")

        self.sign = self.obj.sign()
        self.signed_checkBox.setChecked(True)

    def _check_sign_btn_clicked(self):
        self.obj.check_sign(self.sign)
        self.new_hash.setPlainText(self.obj.new_hash)
        result = self.new_hash.toPlainText() == self.received_hash.text()
        if result:
            QMessageBox.warning(self.widget, "Notification", "Correct!")
        else:
            QMessageBox.warning(self.widget, "Notification", "Incorrect!")

    def _post_btn_clicked(self):
        self.received_hash.setText(self.obj.get_hash(self.sign))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
