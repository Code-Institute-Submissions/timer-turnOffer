# Form implementation generated from reading ui file 'turnOff.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TurnOff(object):
    def setupUi(self, TurnOff):
        TurnOff.setObjectName("TurnOff")
        TurnOff.resize(210, 139)
        TurnOff.setStyleSheet("QDialog {\n"
"background:black;\n"
"}")
        self.timeEdit = QtWidgets.QTimeEdit(TurnOff)
        self.timeEdit.setGeometry(QtCore.QRect(50, 70, 121, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.textBrowser = QtWidgets.QTextBrowser(TurnOff)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 191, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(TurnOff)
        self.pushButton.setGeometry(QtCore.QRect(10, 100, 93, 28))
        self.pushButton.setStyleSheet("QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(TurnOff)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 100, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(TurnOff)
        QtCore.QMetaObject.connectSlotsByName(TurnOff)

    def retranslateUi(self, TurnOff):
        _translate = QtCore.QCoreApplication.translate
        TurnOff.setWindowTitle(_translate("TurnOff", "Dialog"))
        self.textBrowser.setHtml(_translate("TurnOff", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">When should i turn off your computer?</span></p></body></html>"))
        self.pushButton.setText(_translate("TurnOff", "Done"))
        self.pushButton_2.setText(_translate("TurnOff", "Back"))



