# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\yenisayfalar\addingManagerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')

class Ui_Dialog(object):
    def load(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        query = 'SELECT Username,Password FROM Managers'
        res = dbase.execute(query)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        return

    def delete(self):
        cursor = dbase.cursor()
        query = 'SELECT * FROM Managers'
        alldata = dbase.execute(query)
        for row in enumerate(alldata):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                username = data[1]
                password = data[2]
                cursor.execute(
                    ''' DELETE FROM Managers WHERE Username = ? AND Password = ? ''',
                    (username, password))
                dbase.commit()
                self.deletedMessage()
                self.load()

    def deletedMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle("Deleted Info")
        msgBox.setText("Successfully Deleted.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def addManager(self):
        username = self.usernameLineEdit.text().format(str)
        password = self.passwordLineEdit.text().format(str)
        if len(username) > 0 and len(password) > 0:
            self.addInfos(username,password)
            self.successfullyAdded()
            self.load()
        else:
            self.giveError()

    def addInfos(self,username,password):
        dbase.execute('''INSERT INTO Managers(Username,Password) VALUES(?,?)''',
                      (username,password))
        dbase.commit()  # To Applying the Changes

    def successfullyAdded(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle("Successfully Added")
        msgBox.setText("Thank you. Successfully Added.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def giveError(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle("Check Page")
        msgBox.setText("Please check your information.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 448)
        Dialog.setStyleSheet("color: white; background-color: #103cff;")
        self.passwordLineEdit = QtWidgets.QLineEdit(Dialog)
        self.passwordLineEdit.setGeometry(QtCore.QRect(64, 357, 331, 21))
        self.passwordLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.passwordLineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.passwordLineEdit.setStyleSheet("border: 2px solid #333")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(71, 10, 321, 21))
        self.GetTicketTitle.setObjectName("GetTicketTitle")
        self.usernameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.usernameLineEdit.setGeometry(QtCore.QRect(64, 307, 331, 21))
        self.usernameLineEdit.setWhatsThis("")
        self.usernameLineEdit.setStyleSheet("border: 2px solid #333")
        self.usernameLineEdit.setMaxLength(11)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(71, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.GetTicketIdentityNumberLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIdentityNumberLabel.setGeometry(QtCore.QRect(64, 287, 231, 16))
        self.GetTicketIdentityNumberLabel.setObjectName("GetTicketIdentityNumberLabel")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(144, 400, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setMouseTracking(False)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setStyleSheet("background-color: #333333;")
        self.addButton.setObjectName("addButton")
        self.GetTicketNameSurnameLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketNameSurnameLabel.setGeometry(QtCore.QRect(64, 337, 111, 16))
        self.GetTicketNameSurnameLabel.setObjectName("GetTicketNameSurnameLabel")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(64, 400, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setMouseTracking(False)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("background-color: #333333;")
        self.closeButton.setObjectName("closeButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 381, 192))
        self.tableWidget.setStyleSheet("border: 2px solid black")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(320, 260, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.deleteButton.setFont(font)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setMouseTracking(False)
        self.deleteButton.setAutoFillBackground(False)
        self.deleteButton.setStyleSheet("background-color: #333333;")
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.usernameLineEdit, self.passwordLineEdit)
        Dialog.setTabOrder(self.passwordLineEdit, self.addButton)
        Dialog.setTabOrder(self.addButton, self.closeButton)
        self.closeButton.clicked.connect(Dialog.close)
        self.deleteButton.clicked.connect(self.delete)
        self.addButton.clicked.connect(self.addManager)
        self.tableWidget.setStyleSheet("color: black; text-weight: bold")
        self.load()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Adding Manager</span></p></body></html>"))
        self.GetTicketIdentityNumberLabel.setText(_translate("Dialog", "Username"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.GetTicketNameSurnameLabel.setText(_translate("Dialog", "Password"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

