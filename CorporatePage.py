# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CorporatePage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_corporateForm(object):
    def setupUi(self, corporateForm):
        corporateForm.setObjectName("corporateForm")
        corporateForm.resize(403, 313)
        corporateForm.setStyleSheet("background-color: #103cff;\n"
"color: white;")
        self.corporatescrollArea = QtWidgets.QScrollArea(corporateForm)
        self.corporatescrollArea.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.corporatescrollArea.setWidgetResizable(True)
        self.corporatescrollArea.setObjectName("corporatescrollArea")
        self.corporateScrollAreaWidgetContents = QtWidgets.QWidget()
        self.corporateScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 259))
        self.corporateScrollAreaWidgetContents.setStyleSheet("background-color: white;\n"
"")
        self.corporateScrollAreaWidgetContents.setObjectName("corporateScrollAreaWidgetContents")
        self.corporateContent = QtWidgets.QTextEdit(self.corporateScrollAreaWidgetContents)
        self.corporateContent.setGeometry(QtCore.QRect(0, 0, 381, 261))
        self.corporateContent.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.corporateContent.setStyleSheet("border: 2px solid #333")
        self.corporateContent.setReadOnly(True)
        self.corporateContent.setObjectName("corporateContent")
        self.corporatescrollArea.setWidget(self.corporateScrollAreaWidgetContents)
        self.corporateCloseButton = QtWidgets.QPushButton(corporateForm)
        self.corporateCloseButton.setGeometry(QtCore.QRect(10, 280, 381, 23))
        self.corporateCloseButton.clicked.connect(corporateForm.close)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.corporateCloseButton.setFont(font)
        self.corporateCloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.corporateCloseButton.setStyleSheet("background-color: #333;\n"
"color: white;\n"
"")
        self.corporateCloseButton.setObjectName("corporateCloseButton")

        self.retranslateUi(corporateForm)
        QtCore.QMetaObject.connectSlotsByName(corporateForm)

    def retranslateUi(self, corporateForm):
        _translate = QtCore.QCoreApplication.translate
        corporateForm.setWindowTitle(_translate("corporateForm", "Form"))
        self.corporateContent.setHtml(_translate("corporateForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:18px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:110%; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#038eae; background-color:#ffffff;\">Amazing Submarine trip to the deep mystery seas</span></p>\n"
"<p style=\" margin-top:18px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:110%; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">Go for a once in a lifetime experience and discover the beautiful marine life and the underwater world of Mauritius!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">As part of the submarine trip will get to visit a shipwreck, explore the rich coral reefs of Mauritius, and observe and encounter various species of fish.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">This is a wonderful experience for everyone visiting Mauritius. You will get to experience what you only dream about, when going underwater and staring into the crystal clear Indian Ocean water and discovering the rich sea life deep underwater.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">The submarine activity begins with a pre departure briefing on land, followed by a motor boat transfer to the main platform where you will board the submarine. Then the submarine will start its decent into the deep sea for a real fantasy adventure trip.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">You will cruise along the reef and view the corals from very close, explore the local rich marine life, visit the ship wreck of the famous Star Hope cruiser, and discover a 17th century anchor on the bottom of the ocean.</span><img src=\"https://mauritiusattractions.com/slir/w364-c2x1/content/images/product-images/48/mauritius-submarine-excursion.jpg\" style=\"vertical-align: middle;\" style=\"float: right;\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">The submarine is air-conditioned with fully transparent-glassed cabin so you will enjoy exceptionally clear panoramic views of the extraordinary underwater world. It is designed so each passenger has individual observation window for viewing outside on the wonderful underwater world.</span><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333;\"><br />There is also a camera situated on the submarine’s bridge which projects the great views from outside through a TV screen located inside the submarine, giving you an additional view of the marine life.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">At 35 meters undersea, you may see some rare species and will explore the underwater world of Mauritius like on safari trip. Apart from the marine life, the sprawling exotic corals make this submarine trip a memorable experience.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">The pilots of the submarine are well educated in marine biology and are trained to provide a safe trip to all the travelers.</span></p>\n"
"<p style=\" margin-top:13px; margin-bottom:13px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:110%; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; font-weight:600; color:#222222; background-color:#ffffff;\">Beverages will be provided during the trip.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:9px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:18px; background-color:#ffffff;\"><span style=\" font-family:\'Arial,Helvetica,sans-serif\'; font-size:8pt; color:#333333; background-color:#ffffff;\">At the end of the trip each passenger will receive an individual certificate signed by the submarine pilot certifying your experience on the submarine.</span></p></body></html>"))
        self.corporateCloseButton.setText(_translate("corporateForm", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    corporateForm = QtWidgets.QWidget()
    ui = Ui_corporateForm()
    ui.setupUi(corporateForm)
    corporateForm.show()
    sys.exit(app.exec_())
