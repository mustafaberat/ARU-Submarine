# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\newpages\addingManagerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 219)
        Dialog.setStyleSheet("color: white; background-color: #103cff;")
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(40, 117, 331, 21))
        self.passwordLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.passwordLineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passwordLineEdit.setStyleSheet("border: 2px solid #333")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(40, 10, 321, 21))
        self.GetTicketTitle.setObjectName("GetTicketTitle")
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(40, 67, 331, 21))
        self.usernameLineEdit.setWhatsThis("")
        self.usernameLineEdit.setStyleSheet("border: 2px solid #333")
        self.usernameLineEdit.setMaxLength(11)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(40, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.GetTicketIdentityNumberLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIdentityNumberLabel.setGeometry(QtCore.QRect(40, 47, 231, 16))
        self.GetTicketIdentityNumberLabel.setObjectName("GetTicketIdentityNumberLabel")
        self.logInButton = QtWidgets.QPushButton(Dialog)
        self.logInButton.setGeometry(QtCore.QRect(120, 160, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.logInButton.setFont(font)
        self.logInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logInButton.setMouseTracking(False)
        self.logInButton.setAutoFillBackground(False)
        self.logInButton.setStyleSheet("background-color: #333333;")
        self.logInButton.setObjectName("logInButton")
        self.GetTicketNameSurnameLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketNameSurnameLabel.setGeometry(QtCore.QRect(40, 97, 111, 16))
        self.GetTicketNameSurnameLabel.setObjectName("GetTicketNameSurnameLabel")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(40, 160, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(False)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("background-color: #333333;")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        Dialog.setTabOrder(self.passwordLineEdit, self.logInButton)
        Dialog.setTabOrder(self.logInButton, self.closeButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Adding Manager</span></p></body></html>"))
        self.GetTicketIdentityNumberLabel.setText(_translate("Dialog", "Username"))
        self.logInButton.setText(_translate("Dialog", "Add"))
        self.GetTicketNameSurnameLabel.setText(_translate("Dialog", "Password"))
        self.closeButton.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

