# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\newpages\FirstPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import HomePage
import logInManagerPage
class Ui_Dialog(object):
    def goManagerPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = logInManagerPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def goHomePage(self):
        self.window = QtWidgets.QWidget()
        self.ui = HomePage.Ui_HomePage()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 331)
        Dialog.setStyleSheet("background-color: #103cff;\n"
"color: white;\n"
"")
        self.customerButton = QtWidgets.QPushButton(Dialog)
        self.customerButton.setGeometry(QtCore.QRect(270, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.customerButton.setFont(font)
        self.customerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.customerButton.setStyleSheet("background-color: #333333; color: white;")
        self.customerButton.setObjectName("customerButton")
        self.customerButton.clicked.connect(self.goHomePage)
        self.managerButton = QtWidgets.QPushButton(Dialog)
        self.managerButton.setGeometry(QtCore.QRect(40, 280, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.managerButton.setFont(font)
        self.managerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.managerButton.setStyleSheet("background-color: #333333; color: white;")
        self.managerButton.setObjectName("managerButton")
        self.managerButton.clicked.connect(self.goManagerPage)
        self.HomePageWelcomeTitle = QtWidgets.QLabel(Dialog)
        self.HomePageWelcomeTitle.setGeometry(QtCore.QRect(80, 10, 381, 61))
        self.HomePageWelcomeTitle.setStyleSheet(".anasayfaHosgeldinizYazisi{\n"
"    back-ground: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"}")
        self.HomePageWelcomeTitle.setObjectName("HomePageWelcomeTitle")
        self.photoLabel = QtWidgets.QLabel(Dialog)
        self.photoLabel.setGeometry(QtCore.QRect(50, 90, 441, 171))
        self.photoLabel.setStyleSheet("border: 2px solid white; border-image: url(s2.jpg);")
        self.photoLabel.setObjectName("photoLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.customerButton, self.managerButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.customerButton.setText(_translate("Dialog", "Customer"))
        self.managerButton.setText(_translate("Dialog", "Manager"))
        self.HomePageWelcomeTitle.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Welcome to ARU Submarine Underwater Trip System</span></p></body></html>"))
        self.photoLabel.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

