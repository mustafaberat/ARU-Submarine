# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\newpages\logInManagerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import managerPage
dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')
class Ui_Dialog(object):
    def checkInfos(self):
        username = self.usernameLineEdit.text().format(str)
        password = self.passwordLineEdit.text().format(str)
        result = dbase.execute(''' SELECT * FROM Managers WHERE Username = ? AND Password = ?''', (username,password))
        if (len(result.fetchall())>0):
            self.goManagerPage()
        else :
            self.giveError()
    def goManagerPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = managerPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def giveError(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle("Check Page")
        msgBox.setText("Please check your information.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 215)
        Dialog.setStyleSheet("color: white; background-color: #103cff;")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(30, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(30, 117, 331, 21))
        self.passwordLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.passwordLineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passwordLineEdit.setStyleSheet("border: 2px solid #333")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.logInButton = QtWidgets.QPushButton(Dialog)
        self.logInButton.setGeometry(QtCore.QRect(110, 160, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.logInButton.setFont(font)
        self.logInButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logInButton.setMouseTracking(False)
        self.logInButton.setAutoFillBackground(False)
        self.logInButton.setStyleSheet("background-color: #333333;")
        self.logInButton.setObjectName("logInButton")
        self.logInButton.clicked.connect(self.checkInfos)
        self.GetTicketNameSurnameLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketNameSurnameLabel.setGeometry(QtCore.QRect(30, 97, 111, 16))
        self.GetTicketNameSurnameLabel.setObjectName("GetTicketNameSurnameLabel")
        self.GetTicketIdentityNumberLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIdentityNumberLabel.setGeometry(QtCore.QRect(30, 47, 231, 16))
        self.GetTicketIdentityNumberLabel.setObjectName("GetTicketIdentityNumberLabel")
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(30, 67, 331, 21))
        self.usernameLineEdit.setWhatsThis("")
        self.usernameLineEdit.setStyleSheet("border: 2px solid #333")
        self.usernameLineEdit.setMaxLength(35)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(30, 160, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(False)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("background-color: #333333;")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(30, 16, 321, 16))
        self.GetTicketTitle.setObjectName("GetTicketTitle")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        Dialog.setTabOrder(self.passwordLineEdit, self.logInButton)
        Dialog.setTabOrder(self.logInButton, self.closeButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logInButton.setText(_translate("Dialog", "Login"))
        self.GetTicketNameSurnameLabel.setText(_translate("Dialog", "Password"))
        self.GetTicketIdentityNumberLabel.setText(_translate("Dialog", "Username"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Login Page</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

