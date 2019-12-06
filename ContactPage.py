# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ContactPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import HomePage

class Ui_ContactForm(object):
    def setupUi(self, ContactForm):
        ContactForm.setObjectName("ContactForm")
        ContactForm.resize(409, 253)
        ContactForm.setStyleSheet("background-color: #103cff;\n"
"color: white;\n"
"")
        self.ContactTitle = QtWidgets.QLabel(ContactForm)
        self.ContactTitle.setGeometry(QtCore.QRect(20, 20, 361, 20))
        self.ContactTitle.setObjectName("ContactTitle")
        self.ContactLine = QtWidgets.QFrame(ContactForm)
        self.ContactLine.setGeometry(QtCore.QRect(20, 40, 371, 20))
        self.ContactLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.ContactLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ContactLine.setObjectName("ContactLine")
        self.ContactAddressLineEdit = QtWidgets.QLineEdit(ContactForm)
        self.ContactAddressLineEdit.setGeometry(QtCore.QRect(30, 86, 351, 20))
        self.ContactAddressLineEdit.setStyleSheet("border: 2px solid #333")
        self.ContactAddressLineEdit.setReadOnly(True)
        self.ContactAddressLineEdit.setObjectName("ContactAddressLineEdit")
        self.ContactAddressLabel = QtWidgets.QLabel(ContactForm)
        self.ContactAddressLabel.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.ContactAddressLabel.setObjectName("ContactAddressLabel")
        self.ContactPhoneLineEdit = QtWidgets.QLineEdit(ContactForm)
        self.ContactPhoneLineEdit.setGeometry(QtCore.QRect(30, 134, 351, 20))
        self.ContactPhoneLineEdit.setStyleSheet("border: 2px solid #333")
        self.ContactPhoneLineEdit.setReadOnly(True)
        self.ContactPhoneLineEdit.setObjectName("ContactPhoneLineEdit")
        self.ContactPhoneLabel = QtWidgets.QLabel(ContactForm)
        self.ContactPhoneLabel.setGeometry(QtCore.QRect(30, 118, 47, 13))
        self.ContactPhoneLabel.setObjectName("ContactPhoneLabel")
        self.ContactPhoneLabel_2 = QtWidgets.QLabel(ContactForm)
        self.ContactPhoneLabel_2.setGeometry(QtCore.QRect(30, 164, 47, 13))
        self.ContactPhoneLabel_2.setObjectName("ContactPhoneLabel_2")
        self.ContactPhoneLineEdit_2 = QtWidgets.QLineEdit(ContactForm)
        self.ContactPhoneLineEdit_2.setGeometry(QtCore.QRect(30, 180, 351, 20))
        self.ContactPhoneLineEdit_2.setStyleSheet("border: 2px solid #333")
        self.ContactPhoneLineEdit_2.setReadOnly(True)
        self.ContactPhoneLineEdit_2.setObjectName("ContactPhoneLineEdit_2")
        self.ContactHomeButton = QtWidgets.QPushButton(ContactForm)
        self.ContactHomeButton.clicked.connect(ContactForm.hide)
        self.ContactHomeButton.setGeometry(QtCore.QRect(30, 212, 351, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.ContactHomeButton.setFont(font)
        self.ContactHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ContactHomeButton.setMouseTracking(False)
        self.ContactHomeButton.setAutoFillBackground(False)
        self.ContactHomeButton.setStyleSheet("background-color: #333333;")
        self.ContactHomeButton.setObjectName("ContactHomeButton")

        self.retranslateUi(ContactForm)
        QtCore.QMetaObject.connectSlotsByName(ContactForm)

    def retranslateUi(self, ContactForm):
        _translate = QtCore.QCoreApplication.translate
        ContactForm.setWindowTitle(_translate("ContactForm", "Form"))
        self.ContactTitle.setText(_translate("ContactForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ARU Submarine Underwater Trip</span></p></body></html>"))
        self.ContactAddressLineEdit.setText(_translate("ContactForm", "Cecilia Chapman 711-2880 Nulla St. Mankato Mississippi 96522"))
        self.ContactAddressLabel.setText(_translate("ContactForm", "Address"))
        self.ContactPhoneLineEdit.setText(_translate("ContactForm", "551 162 42 86"))
        self.ContactPhoneLabel.setText(_translate("ContactForm", "Phone"))
        self.ContactPhoneLabel_2.setText(_translate("ContactForm", "E-mail"))
        self.ContactPhoneLineEdit_2.setText(_translate("ContactForm", "mustafa.aru@std.izu.edu.tr"))
        self.ContactHomeButton.setText(_translate("ContactForm", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactForm = QtWidgets.QWidget()
    ui = Ui_ContactForm()
    ui.setupUi(ContactForm)
    ContactForm.show()
    sys.exit(app.exec_())
