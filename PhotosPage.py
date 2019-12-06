# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PhotosPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 464)
        Dialog.setStyleSheet("color: white; background-color: #103cff;")
        self.PhotosContentLabel = QtWidgets.QLabel(Dialog)
        self.PhotosContentLabel.setGeometry(QtCore.QRect(120, 250, 321, 16))
        self.PhotosContentLabel.setObjectName("PhotosContentLabel")
        self.PhotosLine = QtWidgets.QFrame(Dialog)
        self.PhotosLine.setGeometry(QtCore.QRect(120, 28, 321, 16))
        self.PhotosLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.PhotosLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PhotosLine.setObjectName("PhotosLine")
        self.PhotosHomeButton = QtWidgets.QPushButton(Dialog)
        self.PhotosHomeButton.clicked.connect(Dialog.close)
        self.PhotosHomeButton.setGeometry(QtCore.QRect(29, 422, 491, 23))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.PhotosHomeButton.setFont(font)
        self.PhotosHomeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PhotosHomeButton.setMouseTracking(False)
        self.PhotosHomeButton.setAutoFillBackground(False)
        self.PhotosHomeButton.setStyleSheet("background-color: #333333;")
        self.PhotosHomeButton.setObjectName("PhotosHomeButton")
        self.PhotosTitle = QtWidgets.QLabel(Dialog)
        self.PhotosTitle.setGeometry(QtCore.QRect(120, 10, 321, 16))
        self.PhotosTitle.setObjectName("PhotosTitle")
        self.PhotosContentEditText = QtWidgets.QTextEdit(Dialog)
        self.PhotosContentEditText.setGeometry(QtCore.QRect(30, 270, 491, 121))
        self.PhotosContentEditText.setStyleSheet("border: 2px solid #333")
        self.PhotosContentEditText.setReadOnly(True)
        self.PhotosContentEditText.setObjectName("PhotosContentEditText")
        self.PhotosPhotoToLabel = QtWidgets.QLabel(Dialog)
        self.PhotosPhotoToLabel.setGeometry(QtCore.QRect(40, 50, 461, 181))
        self.PhotosPhotoToLabel.setStyleSheet("border: 2px solid white; border-image: url(s1.jpg);")
        self.PhotosPhotoToLabel.setObjectName("PhotosPhotoToLabel")
        # self.PhotosPhotoToLabel.setPixmap(QtGui.QPixmap("s1.jpg"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.PhotosContentEditText, self.PhotosHomeButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PhotosContentLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Some information about our trips</p></body></html>"))
        self.PhotosHomeButton.setText(_translate("Dialog", "Close"))
        self.PhotosTitle.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Photos</span></p></body></html>"))
        self.PhotosContentEditText.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Istanbul Trip: First inhabitants of Istanbul are dating back to second millennia BC, they were settled on the Asian side of the city. Its first name comes from Megara king Byzas who took his colonists here in the 7th century BC to establish a colony named Byzantium, the Greek name for a city on the Bosphorus. Byzas chose this spot after consulting an oracle of Delphi who told him to settle across from the &quot;land of the blind&quot;. Indeed, Byzas believed that earlier settlers must have been &quot;blind&quot; for overlooking this superb location at the entrance of the Bosphorus strait, only access to the Black Sea.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In the 6th century BC Persians ruled the city and than Alexander the Great took it over after 4th century BC, which was a peaceful period until the 2nd century BC.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In 193 AD Roman emperor Septimus Severus conquered the city and it remained under the Roman rule until 4th century AD, when emperor Constantine the Great made Byzantium the capital of entire Roman Empire and gave it his name: Constantinople, and Eastern Roman Empire was called Byzantine Empire after 5th century. The city was built on seven hills, like Rome.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Early Byzantine emperors filled their city with the treasures of the ancient world, especially between 4th and 6th centuries with a population exceeded half a million. In 532 during the reign of Justinian I, riots destroyed the city. But it was rebuilt and outstanding structures such as Hagia Sophia stand as monuments to the golden age of Byzantines.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Istanbul\'s latter history is full intrigues and sieges, it was besieged by the Arabs in the 7th and 8th centuries and by the Barbarians in the 9th and 10th, but ruled by the Fourth Crusade between 1204-1261 who destroyed and sacked all the wealth. After this, Constantinople did not regain its former richness nor strength.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ottoman Turks lead by Sultan Mehmet II conquered Constantinople in 1453. Renamed Islambol, the city became the capital of the Ottoman Empire. Between 15th and 16th centuries, sultans built many mosques and public buildings, topping the population again around half million by the mid 1500\'s, Istanbul was a major cultural, political, and commercial center. The name &quot;Istanbul&quot; was derived from a combination of &quot;Islambol&quot; (&quot;city of Islam&quot; in Turkish) and &quot;eis tin Polin&quot; (&quot;to the City&quot; in Greek) throughout the centuries.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ottoman rule lasted until World War I when Istanbul was occupied by the allied troops. After years of struggle led by Ataturk against the occupying forces, the Republic of Turkey was born in 1923 and the capital was moved to Ankara province. But Istanbul has continued to expand dramatically; today its population is over 13 million and still increases constantly. It continues to be the commercial and cultural center of Turkey.</p></body></html>"))
        self.PhotosPhotoToLabel.setText(_translate("Dialog","<html><head/><body></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
