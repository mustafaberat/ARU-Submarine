# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HaveAnIdeaPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
dbase = sqlite3.connect('ARU_Submarine_Project_Data_Base.db')

class Ui_HaveIdeaForm(object):

    def checkTripAdviceSendButton(self):
        nameSurname = self.HaveIdeaNameSurnameLineEdit.text().format(str)
        idea = self.HaveIdeaIdeaTextEdit.toPlainText().format(str)
        notRobot = self.HaveIdeaNotRobotLineEdit.text().upper().format(str)
        if len(nameSurname) != 0 and len(idea) != 0 and len(notRobot) != 0 :
            if notRobot == "I AM NOT ROBOT" or notRobot == "IM NOT ROBOT":
                dbase.execute(
                    '''INSERT INTO Ideas(NameSurname, Idea) VALUES (?,?)''',
                    (nameSurname, idea))
                dbase.commit()
                dbase.close()
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setWindowTitle("Thanks")
                msgBox.setText("Thank you for idea.")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec_()
            else:
                self.HaveIdeaNotRobotLineEdit.setStyleSheet("border: 2px solid #C40D0D")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Check Page")
            msgBox.setText("Please check your information.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def setupUi(self, HaveIdeaForm):
        HaveIdeaForm.setObjectName("HaveIdeaForm")
        HaveIdeaForm.resize(405, 325)
        HaveIdeaForm.setStyleSheet("color: white; background-color: #103cff;")
        self.HaveIdeaSendButton = QtWidgets.QPushButton(HaveIdeaForm)
        self.HaveIdeaSendButton.setGeometry(QtCore.QRect(121, 272, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HaveIdeaSendButton.setFont(font)
        self.HaveIdeaSendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HaveIdeaSendButton.setMouseTracking(False)
        self.HaveIdeaSendButton.setAutoFillBackground(False)
        self.HaveIdeaSendButton.setStyleSheet("background-color: #333333;")
        self.HaveIdeaSendButton.setObjectName("HaveIdeaSendButton")
        self.HaveIdeaSendButton.clicked.connect(self.checkTripAdviceSendButton)
        self.HaveIdeaIdeaLabel = QtWidgets.QLabel(HaveIdeaForm)
        self.HaveIdeaIdeaLabel.setGeometry(QtCore.QRect(50, 104, 141, 16))
        self.HaveIdeaIdeaLabel.setObjectName("HaveIdeaIdeaLabel")
        self.HaveIdeaTitle = QtWidgets.QLabel(HaveIdeaForm)
        self.HaveIdeaTitle.setGeometry(QtCore.QRect(47, 16, 321, 16))
        self.HaveIdeaTitle.setObjectName("HaveIdeaTitle")
        self.HaveIdeaNameSurnameLineEdit = QtWidgets.QLineEdit(HaveIdeaForm)
        self.HaveIdeaNameSurnameLineEdit.setGeometry(QtCore.QRect(47, 76, 321, 21))
        self.HaveIdeaNameSurnameLineEdit.setWhatsThis("")
        self.HaveIdeaNameSurnameLineEdit.setStyleSheet("border: 2px solid #333")
        self.HaveIdeaNameSurnameLineEdit.setMaxLength(26)
        self.HaveIdeaNameSurnameLineEdit.setObjectName("HaveIdeaNameSurnameLineEdit")
        self.HaveIdeaNotRobotLabel = QtWidgets.QLabel(HaveIdeaForm)
        self.HaveIdeaNotRobotLabel.setGeometry(QtCore.QRect(48, 216, 321, 16))
        self.HaveIdeaNotRobotLabel.setObjectName("HaveIdeaNotRobotLabel")
        self.HaveIdeaNameSurnameLabel = QtWidgets.QLabel(HaveIdeaForm)
        self.HaveIdeaNameSurnameLabel.setGeometry(QtCore.QRect(47, 56, 231, 16))
        self.HaveIdeaNameSurnameLabel.setObjectName("HaveIdeaNameSurnameLabel")
        self.HaveIdeaNotRobotLineEdit = QtWidgets.QLineEdit(HaveIdeaForm)
        self.HaveIdeaNotRobotLineEdit.setGeometry(QtCore.QRect(48, 236, 321, 20))
        self.HaveIdeaNotRobotLineEdit.setStyleSheet("border: 2px solid #333")
        self.HaveIdeaNotRobotLineEdit.setObjectName("HaveIdeaNotRobotLineEdit")
        self.HaveIdeaIdeaTextEdit = QtWidgets.QTextEdit(HaveIdeaForm)
        self.HaveIdeaIdeaTextEdit.setGeometry(QtCore.QRect(50, 126, 321, 81))
        self.HaveIdeaIdeaTextEdit.setStyleSheet("border: 2px solid #333")
        self.HaveIdeaIdeaTextEdit.setObjectName("HaveIdeaIdeaTextEdit")
        self.HaveIdeaHomeButton = QtWidgets.QPushButton(HaveIdeaForm)
        self.HaveIdeaHomeButton.setGeometry(QtCore.QRect(50, 272, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HaveIdeaHomeButton.setFont(font)
        self.HaveIdeaHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HaveIdeaHomeButton.setMouseTracking(False)
        self.HaveIdeaHomeButton.setAutoFillBackground(False)
        self.HaveIdeaHomeButton.setStyleSheet("background-color: #333333;")
        self.HaveIdeaHomeButton.setObjectName("HaveIdeaHomeButton")
        self.HaveIdeaHomeButton.clicked.connect(HaveIdeaForm.close)
        self.HaveIdeaLine = QtWidgets.QFrame(HaveIdeaForm)
        self.HaveIdeaLine.setGeometry(QtCore.QRect(50, 34, 301, 16))
        self.HaveIdeaLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.HaveIdeaLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HaveIdeaLine.setObjectName("HaveIdeaLine")

        self.retranslateUi(HaveIdeaForm)
        QtCore.QMetaObject.connectSlotsByName(HaveIdeaForm)
        HaveIdeaForm.setTabOrder(self.HaveIdeaNameSurnameLineEdit, self.HaveIdeaIdeaTextEdit)
        HaveIdeaForm.setTabOrder(self.HaveIdeaIdeaTextEdit, self.HaveIdeaNotRobotLineEdit)
        HaveIdeaForm.setTabOrder(self.HaveIdeaNotRobotLineEdit, self.HaveIdeaSendButton)
        HaveIdeaForm.setTabOrder(self.HaveIdeaSendButton, self.HaveIdeaHomeButton)

    def retranslateUi(self, HaveIdeaForm):
        _translate = QtCore.QCoreApplication.translate
        HaveIdeaForm.setWindowTitle(_translate("HaveIdeaForm", "Form"))
        self.HaveIdeaSendButton.setText(_translate("HaveIdeaForm", "Send"))
        self.HaveIdeaIdeaLabel.setText(_translate("HaveIdeaForm", "Idea"))
        self.HaveIdeaTitle.setText(_translate("HaveIdeaForm", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Help Us Improve By Sharing Your Feedback</span></p></body></html>"))
        self.HaveIdeaNotRobotLabel.setText(_translate("HaveIdeaForm", "Please write \"I am not robot\""))
        self.HaveIdeaNameSurnameLabel.setText(_translate("HaveIdeaForm", "Name and Surname"))
        self.HaveIdeaHomeButton.setText(_translate("HaveIdeaForm", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HaveIdeaForm = QtWidgets.QWidget()
    ui = Ui_HaveIdeaForm()
    ui.setupUi(HaveIdeaForm)
    HaveIdeaForm.show()
    sys.exit(app.exec_())
