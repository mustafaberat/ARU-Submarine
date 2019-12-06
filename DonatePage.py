# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DonatePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sqlite3
dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')


class Ui_DonateForm(object):
    def checkDonateButton(self):
        iban = self.donateSenderIBANLineEdit.text().format(str)
        nameSurname = self.donateSenderNameAndSurnameLineEdit.text().format(str)
        donationAmount = self.donateDonationAmountSpinBox.text().format(str)
        donationAmount = donationAmount.replace(",",".")
        donationAmount = float(donationAmount)
        approval = self.donateIncomingMessageLineEdit.text().format(int)
        # print("Name Surname: ", nameSurname, "\t Type and Length: ", type(nameSurname)," ", len(nameSurname))
        # print("donationAmount: ", donationAmount, "\t Type and Length: ", type(donationAmount), " ", len(donationAmount))
        if len(nameSurname) != 0 and len(iban) == 26 and donationAmount != 0.0 and len(approval) != 0 :
            dbase.execute(
                '''INSERT INTO Donations(IBAN,NameSurname, DonationAmount) VALUES (?,?,?)''',
                (iban,nameSurname, donationAmount))
            dbase.commit()
            dbase.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle("Thanks")
            msgBox.setText("Thank you for donation.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Check Page")
            msgBox.setText("Please check your information.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def checkApprovalButton(self):
        self.donateIncomingMessageLineEdit.setText(str(random.randint(999,9999)))
        donationAmount = self.donateDonationAmountSpinBox.text().format(str)
        donationAmount = donationAmount.replace(",", ".")
        donationAmount = float(donationAmount)
        self.donateAmountShowedByQLC.display(donationAmount)

    def setupUi(self, DonateForm):
        DonateForm.setObjectName("DonateForm")
        DonateForm.resize(370, 363)
        DonateForm.setStyleSheet("background-color: #103cff;\n"
"color: white;\n"
"")
        self.donateSenderNameAndSurnameLineEdit = QtWidgets.QLineEdit(DonateForm)
        self.donateSenderNameAndSurnameLineEdit.setGeometry(QtCore.QRect(20, 112, 321, 21))
        self.donateSenderNameAndSurnameLineEdit.setStyleSheet("border: 2px solid #333")
        self.donateSenderNameAndSurnameLineEdit.setObjectName("donateSenderNameAndSurnameLineEdit")
        self.donateSenderNameAndSurnameLabel = QtWidgets.QLabel(DonateForm)
        self.donateSenderNameAndSurnameLabel.setGeometry(QtCore.QRect(20, 92, 111, 16))
        self.donateSenderNameAndSurnameLabel.setObjectName("donateSenderNameAndSurnameLabel")
        self.donateSenderIBANLineEdit = QtWidgets.QLineEdit(DonateForm)
        self.donateSenderIBANLineEdit.setGeometry(QtCore.QRect(20, 62, 321, 21))
        self.donateSenderIBANLineEdit.setWhatsThis("")
        self.donateSenderIBANLineEdit.setStyleSheet("border: 2px solid #333")
        self.donateSenderIBANLineEdit.setMaxLength(26)
        self.donateSenderIBANLineEdit.setObjectName("donateSenderIBANLineEdit")
        self.donateDonateButton = QtWidgets.QPushButton(DonateForm)
        self.donateDonateButton.setGeometry(QtCore.QRect(90, 327, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.donateDonateButton.setFont(font)
        self.donateDonateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.donateDonateButton.setMouseTracking(False)
        self.donateDonateButton.setAutoFillBackground(False)
        self.donateDonateButton.setStyleSheet("background-color: #333333;")
        self.donateDonateButton.setObjectName("donateDonateButton")
        self.donateDonateButton.clicked.connect(self.checkDonateButton)
        self.donateSenderIBANLabel = QtWidgets.QLabel(DonateForm)
        self.donateSenderIBANLabel.setGeometry(QtCore.QRect(20, 42, 231, 16))
        self.donateSenderIBANLabel.setObjectName("donateSenderIBANLabel")
        self.donateGetApprovalButton = QtWidgets.QPushButton(DonateForm)
        self.donateGetApprovalButton.setGeometry(QtCore.QRect(20, 202, 321, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.donateGetApprovalButton.setFont(font)
        self.donateGetApprovalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.donateGetApprovalButton.setMouseTracking(False)
        self.donateGetApprovalButton.setAutoFillBackground(False)
        self.donateGetApprovalButton.setStyleSheet("background-color: #333333;")
        self.donateGetApprovalButton.setObjectName("donateGetApprovalButton")
        self.donateGetApprovalButton.clicked.connect(self.checkApprovalButton)
        self.donateDonationAmountLabel = QtWidgets.QLabel(DonateForm)
        self.donateDonationAmountLabel.setGeometry(QtCore.QRect(20, 142, 111, 16))
        self.donateDonationAmountLabel.setObjectName("donateDonationAmountLabel")
        self.donateDonationAmountSpinBox = QtWidgets.QDoubleSpinBox(DonateForm)
        self.donateDonationAmountSpinBox.setGeometry(QtCore.QRect(20, 163, 321, 22))
        self.donateDonationAmountSpinBox.setStyleSheet("border: 2px solid #333")
        self.donateDonationAmountSpinBox.setDecimals(1)
        self.donateDonationAmountSpinBox.setMaximum(1000.0)
        self.donateDonationAmountSpinBox.setSingleStep(10.0)
        self.donateDonationAmountSpinBox.setObjectName("donateDonationAmountSpinBox")
        self.donateAmountShowedByQLC = QtWidgets.QLCDNumber(DonateForm)
        self.donateAmountShowedByQLC.setGeometry(QtCore.QRect(270, 292, 71, 23))
        self.donateAmountShowedByQLC.setObjectName("donateAmountShowedByQLC")
        self.donateSenderShowedAgain = QtWidgets.QLabel(DonateForm)
        self.donateSenderShowedAgain.setGeometry(QtCore.QRect(23, 292, 241, 21))
        self.donateSenderShowedAgain.setObjectName("donateSenderShowedAgain")
        self.donateIncomingMessageLineEdit = QtWidgets.QLineEdit(DonateForm)
        self.donateIncomingMessageLineEdit.setGeometry(QtCore.QRect(20, 256, 321, 20))
        self.donateIncomingMessageLineEdit.setStyleSheet("border: 2px solid #333")
        self.donateIncomingMessageLineEdit.setObjectName("donateIncomingMessageLineEdit")
        self.donateIncomingMessageLabel = QtWidgets.QLabel(DonateForm)
        self.donateIncomingMessageLabel.setGeometry(QtCore.QRect(20, 236, 321, 16))
        self.donateIncomingMessageLabel.setObjectName("donateIncomingMessageLabel")
        self.donateThanksTitle = QtWidgets.QLabel(DonateForm)
        self.donateThanksTitle.setGeometry(QtCore.QRect(20, 12, 321, 16))
        self.donateThanksTitle.setObjectName("donateThanksTitle")
        self.donateHomeButton = QtWidgets.QPushButton(DonateForm)
        self.donateHomeButton.setGeometry(QtCore.QRect(19, 327, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.donateHomeButton.setFont(font)
        self.donateHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.donateHomeButton.setMouseTracking(False)
        self.donateHomeButton.setAutoFillBackground(False)
        self.donateHomeButton.setStyleSheet("background-color: #333333;")
        self.donateHomeButton.setObjectName("donateHomeButton")
        self.donateHomeButton.clicked.connect(DonateForm.close)
        self.line = QtWidgets.QFrame(DonateForm)
        self.line.setGeometry(QtCore.QRect(20, 30, 321, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(DonateForm)
        QtCore.QMetaObject.connectSlotsByName(DonateForm)
        DonateForm.setTabOrder(self.donateSenderIBANLineEdit, self.donateSenderNameAndSurnameLineEdit)
        DonateForm.setTabOrder(self.donateSenderNameAndSurnameLineEdit, self.donateDonationAmountSpinBox)
        DonateForm.setTabOrder(self.donateDonationAmountSpinBox, self.donateGetApprovalButton)
        DonateForm.setTabOrder(self.donateGetApprovalButton, self.donateIncomingMessageLineEdit)
        DonateForm.setTabOrder(self.donateIncomingMessageLineEdit, self.donateDonateButton)

    def retranslateUi(self, DonateForm):
        _translate = QtCore.QCoreApplication.translate
        DonateForm.setWindowTitle(_translate("DonateForm", "Form"))
        self.donateSenderNameAndSurnameLabel.setText(_translate("DonateForm", "Name and Surname"))
        self.donateDonateButton.setText(_translate("DonateForm", "Donate"))
        self.donateSenderIBANLabel.setText(_translate("DonateForm", "Sender IBAN"))
        self.donateGetApprovalButton.setText(_translate("DonateForm", "Get Approval"))
        self.donateDonationAmountLabel.setText(_translate("DonateForm", "Donation Amount (TL)"))
        self.donateSenderShowedAgain.setText(_translate("DonateForm", "Sender: "))
        self.donateIncomingMessageLabel.setText(_translate("DonateForm", "Incoming Message to Your Phone"))
        self.donateThanksTitle.setText(_translate("DonateForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Thanks Already For The Donation</span></p></body></html>"))
        self.donateHomeButton.setText(_translate("DonateForm", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DonateForm = QtWidgets.QWidget()
    ui = Ui_DonateForm()
    ui.setupUi(DonateForm)
    DonateForm.show()
    sys.exit(app.exec_())
