# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistrationWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.resize(400, 365)
        RegistrationWindow.setMinimumSize(QtCore.QSize(400, 365))
        RegistrationWindow.setMaximumSize(QtCore.QSize(400, 365))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        RegistrationWindow.setFont(font)
        RegistrationWindow.setStyleSheet("background: rgb(233, 234, 255)")
        self.newLoginLabel = QtWidgets.QLabel(RegistrationWindow)
        self.newLoginLabel.setGeometry(QtCore.QRect(150, 30, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newLoginLabel.setFont(font)
        self.newLoginLabel.setStyleSheet("")
        self.newLoginLabel.setTextFormat(QtCore.Qt.AutoText)
        self.newLoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newLoginLabel.setObjectName("newLoginLabel")
        self.newLoginLineEdit = QtWidgets.QLineEdit(RegistrationWindow)
        self.newLoginLineEdit.setGeometry(QtCore.QRect(75, 70, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newLoginLineEdit.setFont(font)
        self.newLoginLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid blue;\n"
"}\n"
"")
        self.newLoginLineEdit.setObjectName("newLoginLineEdit")
        self.newPasswordLabel = QtWidgets.QLabel(RegistrationWindow)
        self.newPasswordLabel.setGeometry(QtCore.QRect(150, 120, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newPasswordLabel.setFont(font)
        self.newPasswordLabel.setStyleSheet("")
        self.newPasswordLabel.setTextFormat(QtCore.Qt.AutoText)
        self.newPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newPasswordLabel.setObjectName("newPasswordLabel")
        self.newPasswordLineEdit = QtWidgets.QLineEdit(RegistrationWindow)
        self.newPasswordLineEdit.setGeometry(QtCore.QRect(75, 160, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newPasswordLineEdit.setFont(font)
        self.newPasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid blue;\n"
"}")
        self.newPasswordLineEdit.setObjectName("newPasswordLineEdit")
        self.newPasswordLineEdit2 = QtWidgets.QLineEdit(RegistrationWindow)
        self.newPasswordLineEdit2.setGeometry(QtCore.QRect(75, 210, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newPasswordLineEdit2.setFont(font)
        self.newPasswordLineEdit2.setStyleSheet("QLineEdit {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid blue;\n"
"}")
        self.newPasswordLineEdit2.setObjectName("newPasswordLineEdit2")
        self.newPasswordCheckBox2 = QtWidgets.QCheckBox(RegistrationWindow)
        self.newPasswordCheckBox2.setGeometry(QtCore.QRect(340, 210, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newPasswordCheckBox2.setFont(font)
        self.newPasswordCheckBox2.setText("")
        self.newPasswordCheckBox2.setObjectName("newPasswordCheckBox2")
        self.newPasswordCheckBox = QtWidgets.QCheckBox(RegistrationWindow)
        self.newPasswordCheckBox.setGeometry(QtCore.QRect(340, 160, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newPasswordCheckBox.setFont(font)
        self.newPasswordCheckBox.setText("")
        self.newPasswordCheckBox.setObjectName("newPasswordCheckBox")
        self.newRegistrationButton = QtWidgets.QPushButton(RegistrationWindow)
        self.newRegistrationButton.setGeometry(QtCore.QRect(120, 260, 176, 25))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newRegistrationButton.setFont(font)
        self.newRegistrationButton.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid blue;\n"
"}\n"
"")
        self.newRegistrationButton.setObjectName("newRegistrationButton")
        self.newRegInfoLabel = QtWidgets.QLabel(RegistrationWindow)
        self.newRegInfoLabel.setGeometry(QtCore.QRect(25, 305, 350, 30))
        font = QtGui.QFont()
        font.setFamily("Open Sans Condensed SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        self.newRegInfoLabel.setFont(font)
        self.newRegInfoLabel.setStyleSheet("color: red;")
        self.newRegInfoLabel.setText("")
        self.newRegInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.newRegInfoLabel.setObjectName("newRegInfoLabel")

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "RegistrationWindow"))
        self.newLoginLabel.setText(_translate("RegistrationWindow", "Логин"))
        self.newLoginLineEdit.setPlaceholderText(_translate("RegistrationWindow", "Введите логин"))
        self.newPasswordLabel.setText(_translate("RegistrationWindow", "Пароль"))
        self.newPasswordLineEdit.setPlaceholderText(_translate("RegistrationWindow", "Введите пароль"))
        self.newPasswordLineEdit2.setPlaceholderText(_translate("RegistrationWindow", "Повторите пароль"))
        self.newRegistrationButton.setText(_translate("RegistrationWindow", "Зарегистрироваться"))
