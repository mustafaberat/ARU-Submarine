# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetTicketPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sqlite3

dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')

class Ui_Dialog(object):
    def checkGetTicketButton(self):
        identityNumber = self.GetTicketIdentityNumberLineEdit.text().format(str)
        nameSurname = self.GetTicketNameSurnameLineEdit.text().format(str)
        tripDate = self.GetTicketDateEdit.text().format(str)
        approval = self.GetTicketIncomingMessageLineEdit.text().format(str)
        if self.GetTicketRadioButtonTrabzon.isChecked():
            location = "Trabzon"
        elif self.GetTicketRadioButtonBursa.isChecked():
            location = "Bursa"
        elif self.GetTicketRadioButtonIstanbul.isChecked():
            location = "Istanbul"
        elif self.GetTicketRadioButtonHatay.isChecked():
            location = "Hatay"
        else:
            print("Check your information on RadioButton [Location]")

        if self.GetTicketRadioButtonStandart.isChecked():
            classType = "Standard"
        elif self.GetTicketRadioButtonEconomy.isChecked():
            classType = "Economy"
        elif self.GetTicketRadioButtonFirstClass.isChecked():
            classType = "First Class"
        else:
            print("Check your information on RadioButton [ClassType]")
        iban = self.GetTicketIBANLineEdit.text().format(str)
        if len(nameSurname) != 0 and len(iban) == 26 and identityNumber != 0 and len(approval) != 0 and tripDate != "1.01.2000" :
            dbase.execute(
                '''INSERT INTO TicketsReceived(IdentityNo,NameSurname, TripDate, Location, ClassType,IBAN) VALUES (?,?,?,?,?,?)''',
                (identityNumber,nameSurname, tripDate,location,classType,iban))
            dbase.commit()
            dbase.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle("Thanks")
            msgBox.setText("Thank you for shopping.")
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
        self.GetTicketIncomingMessageLineEdit.setText(str(random.randint(999,9999)))
        istanbul = 100
        trabzon = 80
        bursa = 90
        hatay = 50
        standard = 30
        economy = 20
        firsClass = 80
        totalMoney = 0
        if self.GetTicketRadioButtonTrabzon.isChecked():
            totalMoney = totalMoney + trabzon
        elif self.GetTicketRadioButtonBursa.isChecked():
            totalMoney = totalMoney + bursa
        elif self.GetTicketRadioButtonIstanbul.isChecked():
            totalMoney = totalMoney + istanbul
        elif self.GetTicketRadioButtonHatay.isChecked():
            totalMoney = totalMoney + hatay
        else:
            totalMoney = totalMoney + 0

        if self.GetTicketRadioButtonStandart.isChecked():
            totalMoney = totalMoney + standard
        elif self.GetTicketRadioButtonEconomy.isChecked():
            totalMoney = totalMoney + economy
        elif self.GetTicketRadioButtonFirstClass.isChecked():
            totalMoney = totalMoney + firsClass
        else:
            totalMoney = totalMoney + 0
        self.GetTicketAmountShowedByQLC.display(totalMoney)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 601)
        Dialog.setStyleSheet("color: white; background-color: #103cff;")
        self.GetTicketNameSurnameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.GetTicketNameSurnameLineEdit.setGeometry(QtCore.QRect(60, 123, 331, 21))
        self.GetTicketNameSurnameLineEdit.setStyleSheet("border: 2px solid #333")
        self.GetTicketNameSurnameLineEdit.setObjectName("GetTicketNameSurnameLineEdit")
        self.GetTicketAmountShowedByLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketAmountShowedByLabel.setGeometry(QtCore.QRect(60, 301, 211, 20))
        self.GetTicketAmountShowedByLabel.setObjectName("GetTicketAmountShowedByLabel")
        self.GetTicketNameSurnameLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketNameSurnameLabel.setGeometry(QtCore.QRect(60, 103, 111, 16))
        self.GetTicketNameSurnameLabel.setObjectName("GetTicketNameSurnameLabel")
        self.GetTicketIncomingMessageLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIncomingMessageLabel.setGeometry(QtCore.QRect(60, 490, 321, 16))
        self.GetTicketIncomingMessageLabel.setObjectName("GetTicketIncomingMessageLabel")
        self.GetTicketRadioButtonsLocationLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketRadioButtonsLocationLabel.setGeometry(QtCore.QRect(60, 200, 111, 16))
        self.GetTicketRadioButtonsLocationLabel.setObjectName("GetTicketRadioButtonsLocationLabel")
        self.GetTicketAmountShowedByQLC = QtWidgets.QLCDNumber(Dialog)
        self.GetTicketAmountShowedByQLC.setGeometry(QtCore.QRect(310, 304, 71, 23))
        self.GetTicketAmountShowedByQLC.setProperty("value", 0.0)
        self.GetTicketAmountShowedByQLC.setProperty("intValue", 0)
        self.GetTicketAmountShowedByQLC.setObjectName("GetTicketAmountShowedByQLC")
        self.GetTicketLine = QtWidgets.QFrame(Dialog)
        self.GetTicketLine.setGeometry(QtCore.QRect(60, 30, 321, 16))
        self.GetTicketLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.GetTicketLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.GetTicketLine.setObjectName("GetTicketLine")
        self.GetTicketGetTicketButton = QtWidgets.QPushButton(Dialog)
        self.GetTicketGetTicketButton.setGeometry(QtCore.QRect(130, 548, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.GetTicketGetTicketButton.setFont(font)
        self.GetTicketGetTicketButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetTicketGetTicketButton.setMouseTracking(False)
        self.GetTicketGetTicketButton.setAutoFillBackground(False)
        self.GetTicketGetTicketButton.setStyleSheet("background-color: #333333;")
        self.GetTicketGetTicketButton.setObjectName("GetTicketGetTicketButton")
        self.GetTicketGetTicketButton.clicked.connect(self.checkGetTicketButton)
        self.GetTicketTitle = QtWidgets.QLabel(Dialog)
        self.GetTicketTitle.setGeometry(QtCore.QRect(60, 16, 321, 16))
        self.GetTicketTitle.setObjectName("GetTicketTitle")
        self.GetTicketGetApprovalButton = QtWidgets.QPushButton(Dialog)
        self.GetTicketGetApprovalButton.setGeometry(QtCore.QRect(60, 458, 321, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.GetTicketGetApprovalButton.setFont(font)
        self.GetTicketGetApprovalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetTicketGetApprovalButton.setMouseTracking(False)
        self.GetTicketGetApprovalButton.setAutoFillBackground(False)
        self.GetTicketGetApprovalButton.setStyleSheet("background-color: #333333;")
        self.GetTicketGetApprovalButton.setObjectName("GetTicketGetApprovalButton")
        self.GetTicketGetApprovalButton.clicked.connect(self.checkApprovalButton)
        self.GetTicketIdentityNumberLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIdentityNumberLabel.setGeometry(QtCore.QRect(60, 53, 231, 16))
        self.GetTicketIdentityNumberLabel.setObjectName("GetTicketIdentityNumberLabel")
        self.GetTicketIdentityNumberLineEdit = QtWidgets.QLineEdit(Dialog)
        self.GetTicketIdentityNumberLineEdit.setGeometry(QtCore.QRect(60, 73, 331, 21))
        self.GetTicketIdentityNumberLineEdit.setWhatsThis("")
        self.GetTicketIdentityNumberLineEdit.setStyleSheet("border: 2px solid #333")
        self.GetTicketIdentityNumberLineEdit.setMaxLength(11)
        self.GetTicketIdentityNumberLineEdit.setObjectName("GetTicketIdentityNumberLineEdit")
        self.GetTicketHomeButton = QtWidgets.QPushButton(Dialog)
        self.GetTicketHomeButton.setGeometry(QtCore.QRect(60, 548, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.GetTicketHomeButton.setFont(font)
        self.GetTicketHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetTicketHomeButton.setMouseTracking(False)
        self.GetTicketHomeButton.setAutoFillBackground(False)
        self.GetTicketHomeButton.setStyleSheet("background-color: #333333;")
        self.GetTicketHomeButton.setObjectName("GetTicketHomeButton")
        self.GetTicketHomeButton.clicked.connect(Dialog.close)
        self.GetTicketIncomingMessageLineEdit = QtWidgets.QLineEdit(Dialog)
        self.GetTicketIncomingMessageLineEdit.setGeometry(QtCore.QRect(60, 510, 321, 20))
        self.GetTicketIncomingMessageLineEdit.setStyleSheet("border: 2px solid #333")
        self.GetTicketIncomingMessageLineEdit.setObjectName("GetTicketIncomingMessageLineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 219, 328, 19))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.GetTicketRadioButtonLayoutLocation = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.GetTicketRadioButtonLayoutLocation.setContentsMargins(0, 0, 0, 0)
        self.GetTicketRadioButtonLayoutLocation.setObjectName("GetTicketRadioButtonLayoutLocation")
        self.GetTicketRadioButtonIstanbul = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.GetTicketRadioButtonIstanbul.setObjectName("GetTicketRadioButtonIstanbul")
        self.GetTicketRadioButtonLayoutLocation.addWidget(self.GetTicketRadioButtonIstanbul)
        self.GetTicketRadioButtonTrabzon = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.GetTicketRadioButtonTrabzon.setObjectName("GetTicketRadioButtonTrabzon")
        self.GetTicketRadioButtonLayoutLocation.addWidget(self.GetTicketRadioButtonTrabzon)
        self.GetTicketRadioButtonBursa = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.GetTicketRadioButtonBursa.setObjectName("GetTicketRadioButtonBursa")
        self.GetTicketRadioButtonLayoutLocation.addWidget(self.GetTicketRadioButtonBursa)
        self.GetTicketRadioButtonHatay = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.GetTicketRadioButtonHatay.setObjectName("GetTicketRadioButtonHatay")
        self.GetTicketRadioButtonLayoutLocation.addWidget(self.GetTicketRadioButtonHatay)
        self.GetTicketRadioButtonsClassLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketRadioButtonsClassLabel.setGeometry(QtCore.QRect(60, 250, 111, 16))
        self.GetTicketRadioButtonsClassLabel.setObjectName("GetTicketRadioButtonsClassLabel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(60, 270, 328, 19))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.GetTicketRadioButtonLayoutClass = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_2)
        self.GetTicketRadioButtonLayoutClass.setContentsMargins(0, 0, 0, 0)
        self.GetTicketRadioButtonLayoutClass.setObjectName("GetTicketRadioButtonLayoutClass")
        self.GetTicketRadioButtonStandart = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.GetTicketRadioButtonStandart.setObjectName("GetTicketRadioButtonStandart")
        self.GetTicketRadioButtonLayoutClass.addWidget(self.GetTicketRadioButtonStandart)
        self.GetTicketRadioButtonEconomy = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.GetTicketRadioButtonEconomy.setObjectName("GetTicketRadioButtonEconomy")
        self.GetTicketRadioButtonLayoutClass.addWidget(self.GetTicketRadioButtonEconomy)
        self.GetTicketRadioButtonFirstClass = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.GetTicketRadioButtonFirstClass.setObjectName("GetTicketRadioButtonFirstClass")
        self.GetTicketRadioButtonLayoutClass.addWidget(self.GetTicketRadioButtonFirstClass)
        self.GetTicketIBANLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketIBANLabel.setGeometry(QtCore.QRect(60, 331, 111, 16))
        self.GetTicketIBANLabel.setObjectName("GetTicketIBANLabel")
        self.GetTicketIBANLineEdit = QtWidgets.QLineEdit(Dialog)
        self.GetTicketIBANLineEdit.setGeometry(QtCore.QRect(60, 351, 321, 21))
        self.GetTicketIBANLineEdit.setStyleSheet("border: 2px solid #333")
        self.GetTicketIBANLineEdit.setMaxLength(26)
        self.GetTicketIBANLineEdit.setObjectName("GetTicketIBANLineEdit")
        self.GetTicketInformationTextEdit = QtWidgets.QTextEdit(Dialog)
        self.GetTicketInformationTextEdit.setGeometry(QtCore.QRect(60, 381, 321, 71))
        self.GetTicketInformationTextEdit.setStyleSheet("border: 1px solid #333;")
        self.GetTicketInformationTextEdit.setReadOnly(True)
        self.GetTicketInformationTextEdit.setObjectName("GetTicketInformationTextEdit")
        self.GetTicketDateEdit = QtWidgets.QDateEdit(Dialog)
        self.GetTicketDateEdit.setGeometry(QtCore.QRect(60, 170, 331, 22))
        self.GetTicketDateEdit.setStyleSheet("border: 2px solid #333;")
        self.GetTicketDateEdit.setObjectName("GetTicketDateEdit")
        self.GetTicketDateLabel = QtWidgets.QLabel(Dialog)
        self.GetTicketDateLabel.setGeometry(QtCore.QRect(60, 150, 331, 16))
        self.GetTicketDateLabel.setObjectName("GetTicketDateLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.GetTicketIdentityNumberLineEdit, self.GetTicketNameSurnameLineEdit)
        Dialog.setTabOrder(self.GetTicketNameSurnameLineEdit, self.GetTicketDateEdit)
        Dialog.setTabOrder(self.GetTicketDateEdit, self.GetTicketRadioButtonIstanbul)
        Dialog.setTabOrder(self.GetTicketRadioButtonIstanbul, self.GetTicketRadioButtonTrabzon)
        Dialog.setTabOrder(self.GetTicketRadioButtonTrabzon, self.GetTicketRadioButtonBursa)
        Dialog.setTabOrder(self.GetTicketRadioButtonBursa, self.GetTicketRadioButtonHatay)
        Dialog.setTabOrder(self.GetTicketRadioButtonHatay, self.GetTicketRadioButtonStandart)
        Dialog.setTabOrder(self.GetTicketRadioButtonStandart, self.GetTicketRadioButtonEconomy)
        Dialog.setTabOrder(self.GetTicketRadioButtonEconomy, self.GetTicketRadioButtonFirstClass)
        Dialog.setTabOrder(self.GetTicketRadioButtonFirstClass, self.GetTicketIBANLineEdit)
        Dialog.setTabOrder(self.GetTicketIBANLineEdit, self.GetTicketInformationTextEdit)
        Dialog.setTabOrder(self.GetTicketInformationTextEdit, self.GetTicketGetApprovalButton)
        Dialog.setTabOrder(self.GetTicketGetApprovalButton, self.GetTicketIncomingMessageLineEdit)
        Dialog.setTabOrder(self.GetTicketIncomingMessageLineEdit, self.GetTicketGetTicketButton)
        Dialog.setTabOrder(self.GetTicketGetTicketButton, self.GetTicketHomeButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.GetTicketAmountShowedByLabel.setText(_translate("Dialog", "Total Money (TL) : "))
        self.GetTicketNameSurnameLabel.setText(_translate("Dialog", "Name and Surname"))
        self.GetTicketIncomingMessageLabel.setText(_translate("Dialog", "Incoming Message to Your Phone"))
        self.GetTicketRadioButtonsLocationLabel.setText(_translate("Dialog", "Location"))
        self.GetTicketGetTicketButton.setText(_translate("Dialog", "Get Your Ticket"))
        self.GetTicketTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Have Good Trip</span></p></body></html>"))
        self.GetTicketGetApprovalButton.setText(_translate("Dialog", "Get Approval"))
        self.GetTicketIdentityNumberLabel.setText(_translate("Dialog", " Identity Number "))
        self.GetTicketHomeButton.setText(_translate("Dialog", "Close"))
        self.GetTicketRadioButtonIstanbul.setText(_translate("Dialog", "Istanbul"))
        self.GetTicketRadioButtonTrabzon.setText(_translate("Dialog", "Trabzon"))
        self.GetTicketRadioButtonBursa.setText(_translate("Dialog", "Bursa"))
        self.GetTicketRadioButtonHatay.setText(_translate("Dialog", "Hatay"))
        self.GetTicketRadioButtonsClassLabel.setText(_translate("Dialog", "Class Type"))
        self.GetTicketRadioButtonStandart.setText(_translate("Dialog", "Standart"))
        self.GetTicketRadioButtonEconomy.setText(_translate("Dialog", "Economy"))
        self.GetTicketRadioButtonFirstClass.setText(_translate("Dialog", "First Class"))
        self.GetTicketIBANLabel.setText(_translate("Dialog", "IBAN"))
        self.GetTicketInformationTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Operating Hours: 08:30 - 16:30</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Operating Days: All Days</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Duration:2 Hours</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Activity Time: Flexible</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Transportation: Offered as Supplement Comment</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The submarine is offered several times a day</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dont be late!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.GetTicketDateLabel.setText(_translate("Dialog", "Date (dd.mm.yyyy)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
