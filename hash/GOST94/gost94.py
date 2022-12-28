from gost94_functions import GOST94
from hash_ui import Ui_MainWindow

from os import path
from PyQt6.QtWidgets import (
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
        self.InputFile_btn_2.clicked.connect(self.__input_file_btn_clicked)
        self.encrypt_btn.clicked.connect(self.__hash_btn_clicked)

    def __input_file_btn_clicked(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        if not file:
            self.input_path.setText("NO INPUT FILE")
        else:
            self.input_path.setText(path.basename(file))
            self.input_file_path = file

    def __hash_btn_clicked(self):
        if not self.input_file_path:
            data = self.lineEdit_msg.text()
            self.lineEdit.setText(str(GOST94(data, mode="text").generate_hash()))
        else:
            data = self.input_file_path
            self.lineEdit.setText(str(GOST94(data, mode="file").generate_hash()))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec())
