from digital_signature.el_gamal import ElGamalSignature
from gui.eg_signature.eg_signature_ui import Ui_MainWindow

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
        self.post_btn.clicked.connect(self._post_btn_clicked)
        self.InputFile_btn.clicked.connect(self._input_file_btn_clicked)
        self.sign_btn.clicked.connect(self._sign_btn_clicked)
        self.calc_hash_btn.clicked.connect(self._hash_btn_clicked)
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
            self.obj = ElGamalSignature(data)

        else:
            data = self.input_file_path
            self.obj = ElGamalSignature(data, "file")

        self.sign = self.obj.sign()
        self.signed_checkBox.setChecked(True)
        self.y_lineEdit.setText(str(self.obj.keys.public.y))

    def _check_sign_btn_clicked(self):
        self.obj.keys.public.y = int(self.y_lineEdit.text())
        result = self.obj.check_sign(self.sign, self.obj.keys.public)
        if result:
            QMessageBox.warning(self.widget, "Notification", "Correct!")
        else:
            QMessageBox.warning(self.widget, "Notification", "Incorrect!")

    def _post_btn_clicked(self):
        self.msg_textEdit.setPlainText(str(self.sign))

    def _hash_btn_clicked(self):
        if self.msg_textEdit.toPlainText():
            self.new_hash.setPlainText(self.obj.get_hash(self.sign))
        else:
            QMessageBox.warning(self.widget, "Error", "No message received!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
