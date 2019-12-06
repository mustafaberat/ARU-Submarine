# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\newpages\LookDonationPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #103cff;\n"
"color: white;\n"
"")
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(40, 16, 321, 16))
        self.GetTicketTitle.setObjectName("GetTicketTitle")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(40, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(40, 40, 321, 201))
        self.tableView.setStyleSheet("border: 2px solid black")
        self.tableView.setObjectName("tableView")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(44, 250, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: #333333;")
        self.closeButton.setObjectName("closeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Donations</span></p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

