# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\newpages\managerPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 239)
        Dialog.setStyleSheet("background-color: #103cff;\n"
"color: white;\n"
"")
        self.lookAtDonations = QtWidgets.QPushButton(Dialog)
        self.lookAtDonations.setGeometry(QtCore.QRect(10, 141, 206, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lookAtDonations.setFont(font)
        self.lookAtDonations.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookAtDonations.setStyleSheet("background-color: #333333;")
        self.lookAtDonations.setObjectName("lookAtDonations")
        self.lookAtTripAdvice = QtWidgets.QPushButton(Dialog)
        self.lookAtTripAdvice.setGeometry(QtCore.QRect(220, 180, 205, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lookAtTripAdvice.setFont(font)
        self.lookAtTripAdvice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookAtTripAdvice.setStyleSheet("background-color: #333333;")
        self.lookAtTripAdvice.setObjectName("lookAtTripAdvice")
        self.lookAtIdeas = QtWidgets.QPushButton(Dialog)
        self.lookAtIdeas.setGeometry(QtCore.QRect(222, 141, 205, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lookAtIdeas.setFont(font)
        self.lookAtIdeas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookAtIdeas.setStyleSheet("background-color: #333333;")
        self.lookAtIdeas.setObjectName("lookAtIdeas")
        self.HomePageWelcomeTitle = QtWidgets.QLabel(Dialog)
        self.HomePageWelcomeTitle.setGeometry(QtCore.QRect(10, 38, 417, 21))
        self.HomePageWelcomeTitle.setStyleSheet(".anasayfaHosgeldinizYazisi{\n"
"    back-ground: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")
        self.HomePageWelcomeTitle.setObjectName("HomePageWelcomeTitle")
        self.addNewManager = QtWidgets.QPushButton(Dialog)
        self.addNewManager.setGeometry(QtCore.QRect(10, 94, 417, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.addNewManager.setFont(font)
        self.addNewManager.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addNewManager.setStyleSheet("background-color: #333333;")
        self.addNewManager.setObjectName("addNewManager")
        self.lookAtTickets = QtWidgets.QPushButton(Dialog)
        self.lookAtTickets.setGeometry(QtCore.QRect(10, 180, 206, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.lookAtTickets.setFont(font)
        self.lookAtTickets.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookAtTickets.setStyleSheet("background-color: #333333;")
        self.lookAtTickets.setObjectName("lookAtTickets")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.addNewManager, self.lookAtDonations)
        Dialog.setTabOrder(self.lookAtDonations, self.lookAtIdeas)
        Dialog.setTabOrder(self.lookAtIdeas, self.lookAtTickets)
        Dialog.setTabOrder(self.lookAtTickets, self.lookAtTripAdvice)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lookAtDonations.setText(_translate("Dialog", "Look at all donations"))
        self.lookAtTripAdvice.setText(_translate("Dialog", "Look at Trip Advices"))
        self.lookAtIdeas.setText(_translate("Dialog", "Look at Ideas"))
        self.HomePageWelcomeTitle.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Welcome Sir. There are some options you can do.</span></p></body></html>"))
        self.addNewManager.setText(_translate("Dialog", "Add a new manager into database"))
        self.lookAtTickets.setText(_translate("Dialog", "Look at Tickets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

