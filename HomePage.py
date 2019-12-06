# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import ContactPage
import CorporatePage
import PhotosPage
import TripAdvicePage
import HaveAnIdeaPage
import DonatePage
import GetTicketPage

class Ui_HomePage(object):

    def checkGetTicketButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = GetTicketPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkDonateButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = DonatePage.Ui_DonateForm()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkHaveAnIdeaButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = HaveAnIdeaPage.Ui_HaveIdeaForm()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkContactButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = ContactPage.Ui_ContactForm()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkPhotosButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = PhotosPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkEventApplicationButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = TripAdvicePage.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkCorporateButton(self):
        self.window = QtWidgets.QWidget()
        self.ui = CorporatePage.Ui_corporateForm()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.setWindowModality(QtCore.Qt.NonModal)
        HomePage.resize(447, 284)
        HomePage.setStyleSheet("background-color: #103cff;color: white;")
        self.gridLayout = QtWidgets.QGridLayout(HomePage)
        self.gridLayout.setObjectName("gridLayout")
        self.HomePageGridLayout = QtWidgets.QGridLayout()
        self.HomePageGridLayout.setContentsMargins(6, 6, 6, 6)
        self.HomePageGridLayout.setObjectName("HomePageGridLayout")
        self.HomePageCorporateButton = QtWidgets.QPushButton(HomePage)
        self.HomePageCorporateButton.clicked.connect(self.checkCorporateButton)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageCorporateButton.setFont(font)
        self.HomePageCorporateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageCorporateButton.setStyleSheet("background-color: #333333;")
        self.HomePageCorporateButton.setObjectName("HomePageCorporateButton")
        self.HomePageGridLayout.addWidget(self.HomePageCorporateButton, 5, 0, 1, 1)
        self.HomePageHaveAnIdeaButton = QtWidgets.QPushButton(HomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageHaveAnIdeaButton.setFont(font)
        self.HomePageHaveAnIdeaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageHaveAnIdeaButton.setStyleSheet("background-color: #333333;")
        self.HomePageHaveAnIdeaButton.setObjectName("HomePageHaveAnIdeaButton")
        self.HomePageHaveAnIdeaButton.clicked.connect(self.checkHaveAnIdeaButton)
        self.HomePageGridLayout.addWidget(self.HomePageHaveAnIdeaButton, 6, 1, 1, 1)
        self.HomePageOnlineTicketButton = QtWidgets.QPushButton(HomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageOnlineTicketButton.setFont(font)
        self.HomePageOnlineTicketButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageOnlineTicketButton.setStyleSheet("background-color: #333333;")
        self.HomePageOnlineTicketButton.setObjectName("HomePageOnlineTicketButton")
        self.HomePageOnlineTicketButton.clicked.connect(self.checkGetTicketButton)
        self.HomePageGridLayout.addWidget(self.HomePageOnlineTicketButton, 2, 0, 1, 2)
        self.HomePageEventApplicationButton = QtWidgets.QPushButton(HomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageEventApplicationButton.setFont(font)
        self.HomePageEventApplicationButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageEventApplicationButton.setStyleSheet("background-color: #333333;")
        self.HomePageEventApplicationButton.clicked.connect(self.checkEventApplicationButton)
        self.HomePageEventApplicationButton.setObjectName("HomePageEventApplicationButton")
        self.HomePageGridLayout.addWidget(self.HomePageEventApplicationButton, 5, 1, 1, 1)
        self.HomePageContactButton = QtWidgets.QPushButton(HomePage)
        self.HomePageContactButton.clicked.connect(self.checkContactButton)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageContactButton.setFont(font)
        self.HomePageContactButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageContactButton.setStyleSheet("background-color: #333333;")
        self.HomePageContactButton.setObjectName("HomePageContactButton")
        self.HomePageGridLayout.addWidget(self.HomePageContactButton, 6, 0, 1, 1)
        self.HomePageDonateButton = QtWidgets.QPushButton(HomePage)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageDonateButton.setFont(font)
        self.HomePageDonateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageDonateButton.setStyleSheet("background-color: #333333;")
        self.HomePageDonateButton.setObjectName("HomePageDonateButton")
        self.HomePageDonateButton.clicked.connect(self.checkDonateButton)
        self.HomePageGridLayout.addWidget(self.HomePageDonateButton, 4, 1, 1, 1)
        self.HomePageWelcomeTitle = QtWidgets.QLabel(HomePage)
        self.HomePageWelcomeTitle.setStyleSheet(".anasayfaHosgeldinizYazisi{\n"
                                                "    back-ground: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
                                                "}")
        self.HomePageWelcomeTitle.setObjectName("HomePageWelcomeTitle")
        self.HomePageGridLayout.addWidget(self.HomePageWelcomeTitle, 0, 0, 1, 2)
        self.HomePageWelcomeTitle.setStyleSheet(" border-image: url(s2.jpg);")
        self.HomePageTripPhotosButton = QtWidgets.QPushButton(HomePage)
        self.HomePageTripPhotosButton.clicked.connect(self.checkPhotosButton)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.HomePageTripPhotosButton.setFont(font)
        self.HomePageTripPhotosButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomePageTripPhotosButton.setStyleSheet("background-color: #333333;")
        self.HomePageTripPhotosButton.setObjectName("HomePageTripPhotosButton")
        self.HomePageGridLayout.addWidget(self.HomePageTripPhotosButton, 4, 0, 1, 1)
        self.HomePageLine = QtWidgets.QFrame(HomePage)
        self.HomePageLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.HomePageLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.HomePageLine.setObjectName("HomePageLine")
        self.HomePageGridLayout.addWidget(self.HomePageLine, 1, 0, 1, 2)
        self.gridLayout.addLayout(self.HomePageGridLayout, 0, 0, 1, 1)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)
        HomePage.setTabOrder(self.HomePageOnlineTicketButton, self.HomePageTripPhotosButton)
        HomePage.setTabOrder(self.HomePageTripPhotosButton, self.HomePageDonateButton)
        HomePage.setTabOrder(self.HomePageDonateButton, self.HomePageCorporateButton)
        HomePage.setTabOrder(self.HomePageCorporateButton, self.HomePageEventApplicationButton)
        HomePage.setTabOrder(self.HomePageEventApplicationButton, self.HomePageContactButton)
        HomePage.setTabOrder(self.HomePageContactButton, self.HomePageHaveAnIdeaButton)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "Form"))
        self.HomePageCorporateButton.setText(_translate("HomePage", "Corporate"))
        self.HomePageHaveAnIdeaButton.setText(_translate("HomePage", "Have An Idea"))
        self.HomePageOnlineTicketButton.setText(_translate("HomePage", "Online Ticket"))
        self.HomePageEventApplicationButton.setText(_translate("HomePage", "Event Application"))
        self.HomePageContactButton.setText(_translate("HomePage", "Contact"))
        self.HomePageDonateButton.setText(_translate("HomePage", "Donate"))
        self.HomePageWelcomeTitle.setText(_translate("HomePage",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\"></span></p></body></html>"))
        self.HomePageTripPhotosButton.setText(_translate("HomePage", "Trip Photos"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HomePage = QtWidgets.QWidget()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.show()
    sys.exit(app.exec_())
