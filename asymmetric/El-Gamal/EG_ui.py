# Form implementation generated from reading ui file '.\asymmetric\El-Gamal\EG_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(685, 520))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #000")
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 50, 41, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;")
        self.label_9.setObjectName("label_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 41))
        self.frame.setStyleSheet("background-color: rgb(49, 80, 78)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1001, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setStyleSheet("color: white;\n"
"font: 18pt \"Century Gothic\";\n"
"font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(220, 50, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;")
        self.label_8.setObjectName("label_8")
        self.text_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_browser.setGeometry(QtCore.QRect(690, 80, 290, 120))
        self.text_browser.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.text_browser.setObjectName("text_browser")
        self.text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(200, 80, 290, 120))
        self.text_edit.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border: 1px solid gray;\n"
"border-radius: 10px;\n"
"color: white;\n"
"")
        self.text_edit.setReadOnly(False)
        self.text_edit.setObjectName("text_edit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 300, 961, 154))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_public_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_public_key.setFont(font)
        self.label_public_key.setStyleSheet("color: white;")
        self.label_public_key.setObjectName("label_public_key")
        self.verticalLayout_2.addWidget(self.label_public_key)
        self.label_private_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_private_key.setFont(font)
        self.label_private_key.setStyleSheet("color: white;")
        self.label_private_key.setObjectName("label_private_key")
        self.verticalLayout_2.addWidget(self.label_private_key)
        self.label_session_key = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_session_key.setFont(font)
        self.label_session_key.setStyleSheet("color: white;")
        self.label_session_key.setObjectName("label_session_key")
        self.verticalLayout_2.addWidget(self.label_session_key)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_public_key = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_public_key.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_public_key.setFont(font)
        self.lineEdit_public_key.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_public_key.setObjectName("lineEdit_public_key")
        self.verticalLayout_3.addWidget(self.lineEdit_public_key)
        self.lineEdit_private_key = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_private_key.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_private_key.setFont(font)
        self.lineEdit_private_key.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_private_key.setObjectName("lineEdit_private_key")
        self.verticalLayout_3.addWidget(self.lineEdit_private_key)
        self.lineEdit_session_key = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_session_key.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_session_key.setFont(font)
        self.lineEdit_session_key.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_session_key.setObjectName("lineEdit_session_key")
        self.verticalLayout_3.addWidget(self.lineEdit_session_key)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_public_key_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_public_key_2.setFont(font)
        self.label_public_key_2.setStyleSheet("color: white;")
        self.label_public_key_2.setObjectName("label_public_key_2")
        self.verticalLayout_4.addWidget(self.label_public_key_2)
        self.label_private_key_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_private_key_2.setFont(font)
        self.label_private_key_2.setStyleSheet("color: white;")
        self.label_private_key_2.setObjectName("label_private_key_2")
        self.verticalLayout_4.addWidget(self.label_private_key_2)
        self.label_session_key_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_session_key_2.setFont(font)
        self.label_session_key_2.setStyleSheet("color: white;")
        self.label_session_key_2.setObjectName("label_session_key_2")
        self.verticalLayout_4.addWidget(self.label_session_key_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_public_key_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_public_key_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_public_key_2.setFont(font)
        self.lineEdit_public_key_2.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_public_key_2.setObjectName("lineEdit_public_key_2")
        self.verticalLayout_5.addWidget(self.lineEdit_public_key_2)
        self.lineEdit_private_key_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_private_key_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_private_key_2.setFont(font)
        self.lineEdit_private_key_2.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_private_key_2.setObjectName("lineEdit_private_key_2")
        self.verticalLayout_5.addWidget(self.lineEdit_private_key_2)
        self.lineEdit_session_key_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_session_key_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_session_key_2.setFont(font)
        self.lineEdit_session_key_2.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_session_key_2.setObjectName("lineEdit_session_key_2")
        self.verticalLayout_5.addWidget(self.lineEdit_session_key_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.gen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gen_btn.setGeometry(QtCore.QRect(20, 470, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.gen_btn.setFont(font)
        self.gen_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.gen_btn.setObjectName("gen_btn")
        self.encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_btn.setGeometry(QtCore.QRect(30, 100, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.encrypt_btn.setFont(font)
        self.encrypt_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.label_key_size = QtWidgets.QLabel(self.centralwidget)
        self.label_key_size.setGeometry(QtCore.QRect(190, 470, 178, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_key_size.setFont(font)
        self.label_key_size.setStyleSheet("color: white;")
        self.label_key_size.setObjectName("label_key_size")
        self.key_size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.key_size_spinBox.setGeometry(QtCore.QRect(370, 470, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.key_size_spinBox.setFont(font)
        self.key_size_spinBox.setStyleSheet("color: white;")
        self.key_size_spinBox.setMinimum(16)
        self.key_size_spinBox.setObjectName("key_size_spinBox")
        self.lineEdit_g = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_g.setEnabled(True)
        self.lineEdit_g.setGeometry(QtCore.QRect(190, 262, 651, 24))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_g.setFont(font)
        self.lineEdit_g.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_g.setObjectName("lineEdit_g")
        self.label_g = QtWidgets.QLabel(self.centralwidget)
        self.label_g.setGeometry(QtCore.QRect(150, 253, 21, 37))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_g.setFont(font)
        self.label_g.setStyleSheet("color: white;")
        self.label_g.setObjectName("label_g")
        self.lineEdit_p = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_p.setEnabled(True)
        self.lineEdit_p.setGeometry(QtCore.QRect(190, 220, 651, 24))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEdit_p.setFont(font)
        self.lineEdit_p.setStyleSheet("border: 1px solid #ccc;\n"
"color: white;")
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.label_p = QtWidgets.QLabel(self.centralwidget)
        self.label_p.setGeometry(QtCore.QRect(150, 210, 21, 37))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_p.setFont(font)
        self.label_p.setStyleSheet("color: white;")
        self.label_p.setObjectName("label_p")
        self.p_gen_btn = QtWidgets.QPushButton(self.centralwidget)
        self.p_gen_btn.setGeometry(QtCore.QRect(20, 230, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.p_gen_btn.setFont(font)
        self.p_gen_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.p_gen_btn.setObjectName("p_gen_btn")
        self.decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_btn.setGeometry(QtCore.QRect(30, 150, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.decrypt_btn.setFont(font)
        self.decrypt_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.input_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_file_btn.setGeometry(QtCore.QRect(480, 470, 111, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.input_file_btn.setFont(font)
        self.input_file_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.input_file_btn.setObjectName("input_file_btn")
        self.input_path = QtWidgets.QLabel(self.centralwidget)
        self.input_path.setGeometry(QtCore.QRect(604, 472, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_path.setFont(font)
        self.input_path.setStyleSheet("color: white;")
        self.input_path.setObjectName("input_path")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElGamal"))
        self.label_9.setText(_translate("MainWindow", "Боб"))
        self.label_4.setText(_translate("MainWindow", "Эль-Гамаль"))
        self.label_8.setText(_translate("MainWindow", "Алиса"))
        self.label_public_key.setText(_translate("MainWindow", "Открытый ключ"))
        self.label_private_key.setText(_translate("MainWindow", "Секретный ключ"))
        self.label_session_key.setText(_translate("MainWindow", "Сессионный ключ"))
        self.label_public_key_2.setText(_translate("MainWindow", "Открытый ключ"))
        self.label_private_key_2.setText(_translate("MainWindow", "Секретный ключ"))
        self.label_session_key_2.setText(_translate("MainWindow", "Сессионный ключ"))
        self.gen_btn.setText(_translate("MainWindow", "Сгенерировать ключи"))
        self.encrypt_btn.setText(_translate("MainWindow", "Зашифровать"))
        self.label_key_size.setText(_translate("MainWindow", "Размер ключа"))
        self.label_g.setText(_translate("MainWindow", "G"))
        self.label_p.setText(_translate("MainWindow", "P"))
        self.p_gen_btn.setText(_translate("MainWindow", "Сгенерировать P"))
        self.decrypt_btn.setText(_translate("MainWindow", "Расшифровать"))
        self.input_file_btn.setText(_translate("MainWindow", "Входной файл"))
        self.input_path.setText(_translate("MainWindow", "NO INPUT FILE"))
