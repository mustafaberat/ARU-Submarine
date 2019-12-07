# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\yenisayfalar\LookDonationPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
class Ui_Dialog(object):
    def load(self):
        dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        query = 'SELECT IBAN, NameSurname, DonationAmount FROM Donations'
        res = dbase.execute(query)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        dbase.close()
        return

    def delete(self):
        dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')
        cursor = dbase.cursor()
        query = 'SELECT * FROM Donations'
        alldata = dbase.execute(query)
        for row in enumerate(alldata):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                IBAN = data[1]
                NameSurname = data[2]
                DonationAmount = data[3]
                cursor.execute(
                    ''' DELETE FROM Donations WHERE IBAN = ? AND NameSurname = ? AND DonationAmount = ?''',
                    (IBAN, NameSurname, DonationAmount))
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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 319)
        Dialog.setStyleSheet("background-color: #103cff;\n"
                             "color: white;\n"
                             "")
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(57, 16, 321, 16))
        self.GetTicketTitle.setObjectName("GetTicketTitle")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(57, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(21, 50, 381, 192))
        self.tableWidget.setStyleSheet("border: 2px solid black")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(50, 280, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: #333333;")
        self.closeButton.setObjectName("closeButton")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(50, 250, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.deleteButton.setFont(font)
        self.deleteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setStyleSheet("background-color: #333333;")
        self.deleteButton.setObjectName("deleteButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.closeButton.clicked.connect(Dialog.close)
        self.deleteButton.clicked.connect(self.delete)
        self.tableWidget.setStyleSheet("color: black; text-weight: bold")
        self.load()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Donations</span></p></body></html>"))
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

