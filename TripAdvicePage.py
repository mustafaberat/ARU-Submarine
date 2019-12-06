# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TripAdvicePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')

class Ui_Form(object):
    def checkTripAdviceSendButton(self):
        nameSurname = self.TripAdviceNameSurnameLineEdit.text().format(str)
        cityName = self.TripAdviceCityNameLineEdit.text().format(str)
        stateName = self.TripAdviceStateNameLineEdit.text().format(str)
        locationAndReasons = self.TripAdviceLocationEditText.toPlainText().format(str)
        # print("State Name: ", stateName, "\t Type and Length: ", type(stateName)," ", len(stateName))
        # print("Location Reasons: ", locationAndReasons, "\t Type and Length: ", type(locationAndReasons), " ", len(locationAndReasons))
        if len(nameSurname) != 0 and len(cityName) != 0 and len(stateName) != 0 and len(locationAndReasons) != 0 :
            dbase.execute('''INSERT INTO TripAdvices(NameSurname, CityName, StateName, LocationsAndReasons) VALUES (?,?,?,?)''',
                (nameSurname, cityName, stateName, locationAndReasons))
            dbase.commit()
            dbase.close()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setWindowTitle("Thanks")
            msgBox.setText("Thank you for advice.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Check Page")
            msgBox.setText("Please check your information.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 308)
        Form.setStyleSheet("color: white; background-color: #103cff;")
        self.TripAdviceSendButton = QtWidgets.QPushButton(Form)
        self.TripAdviceSendButton.setGeometry(QtCore.QRect(114, 261, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.TripAdviceSendButton.setFont(font)
        self.TripAdviceSendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TripAdviceSendButton.setMouseTracking(False)
        self.TripAdviceSendButton.setAutoFillBackground(False)
        self.TripAdviceSendButton.setStyleSheet("background-color: #333333;")
        self.TripAdviceSendButton.setObjectName("TripAdviceSendButton")
        self.TripAdviceSendButton.clicked.connect(self.checkTripAdviceSendButton)
        self.TripAdviceNameSurnameLineEdit = QtWidgets.QLineEdit(Form)
        self.TripAdviceNameSurnameLineEdit.setGeometry(QtCore.QRect(40, 63, 321, 21))
        self.TripAdviceNameSurnameLineEdit.setWhatsThis("")
        self.TripAdviceNameSurnameLineEdit.setStyleSheet("border: 2px solid #333")
        self.TripAdviceNameSurnameLineEdit.setMaxLength(26)
        self.TripAdviceNameSurnameLineEdit.setObjectName("TripAdviceNameSurnameLineEdit")
        self.TripAdviceCityNameLineEdit = QtWidgets.QLineEdit(Form)
        self.TripAdviceCityNameLineEdit.setGeometry(QtCore.QRect(40, 117, 161, 20))
        self.TripAdviceCityNameLineEdit.setStyleSheet("border: 2px solid #333")
        self.TripAdviceCityNameLineEdit.setObjectName("TripAdviceCityNameLineEdit")
        self.TripAdviceLocationEditText = QtWidgets.QTextEdit(Form)
        self.TripAdviceLocationEditText.setGeometry(QtCore.QRect(40, 168, 321, 81))
        self.TripAdviceLocationEditText.setStyleSheet("border: 2px solid #333")
        self.TripAdviceLocationEditText.setObjectName("TripAdviceLocationEditText")
        self.TripAdviceLocationLabel = QtWidgets.QLabel(Form)
        self.TripAdviceLocationLabel.setGeometry(QtCore.QRect(40, 146, 141, 16))
        self.TripAdviceLocationLabel.setObjectName("TripAdviceLocationLabel")
        self.TripAdviceCityNameLabel = QtWidgets.QLabel(Form)
        self.TripAdviceCityNameLabel.setGeometry(QtCore.QRect(40, 97, 161, 16))
        self.TripAdviceCityNameLabel.setObjectName("TripAdviceCityNameLabel")
        self.TripAdviceNameSurnameLabel = QtWidgets.QLabel(Form)
        self.TripAdviceNameSurnameLabel.setGeometry(QtCore.QRect(40, 43, 231, 16))
        self.TripAdviceNameSurnameLabel.setObjectName("TripAdviceNameSurnameLabel")
        self.TripAdviceTitle = QtWidgets.QLabel(Form)
        self.TripAdviceTitle.setGeometry(QtCore.QRect(40, 10, 321, 16))
        self.TripAdviceTitle.setObjectName("TripAdviceTitle")
        self.TripAdviceStateNameLabel = QtWidgets.QLabel(Form)
        self.TripAdviceStateNameLabel.setGeometry(QtCore.QRect(210, 96, 161, 16))
        self.TripAdviceStateNameLabel.setObjectName("TripAdviceStateNameLabel")
        self.TripAdviceStateNameLineEdit = QtWidgets.QLineEdit(Form)
        self.TripAdviceStateNameLineEdit.setGeometry(QtCore.QRect(210, 116, 161, 20))
        self.TripAdviceStateNameLineEdit.setStyleSheet("border: 2px solid #333")
        self.TripAdviceStateNameLineEdit.setObjectName("TripAdviceStateNameLineEdit")
        self.TripAdviceHomeButton = QtWidgets.QPushButton(Form)
        self.TripAdviceHomeButton.setGeometry(QtCore.QRect(41, 262, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.TripAdviceHomeButton.setFont(font)
        self.TripAdviceHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TripAdviceHomeButton.setMouseTracking(False)
        self.TripAdviceHomeButton.setAutoFillBackground(False)
        self.TripAdviceHomeButton.setStyleSheet("background-color: #333333;")
        self.TripAdviceHomeButton.setObjectName("TripAdviceHomeButton")
        self.TripAdviceLine = QtWidgets.QFrame(Form)
        self.TripAdviceLine.setGeometry(QtCore.QRect(40, 23, 321, 16))
        self.TripAdviceLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.TripAdviceLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TripAdviceLine.setObjectName("TripAdviceLine")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.TripAdviceNameSurnameLineEdit, self.TripAdviceCityNameLineEdit)
        Form.setTabOrder(self.TripAdviceCityNameLineEdit, self.TripAdviceStateNameLineEdit)
        Form.setTabOrder(self.TripAdviceStateNameLineEdit, self.TripAdviceLocationEditText)
        Form.setTabOrder(self.TripAdviceLocationEditText, self.TripAdviceSendButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TripAdviceSendButton.setText(_translate("Form", "Send"))
        self.TripAdviceLocationLabel.setText(_translate("Form", "Locations & Reason"))
        self.TripAdviceCityNameLabel.setText(_translate("Form", "City Name"))
        self.TripAdviceNameSurnameLabel.setText(_translate("Form", "Name and Surname"))
        self.TripAdviceTitle.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Give A Location Address Where You Want To Go</span></p></body></html>"))
        self.TripAdviceStateNameLabel.setText(_translate("Form", "State Name"))
        self.TripAdviceHomeButton.setText(_translate("Form", "Close"))
        self.TripAdviceHomeButton.clicked.connect(Form.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
