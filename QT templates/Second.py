# Form implementation generated from reading ui file 'timerWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Timer(object):
    def setupUi(self, Timer):
        Timer.setObjectName("Timer")
        Timer.resize(211, 110)
        Timer.setStyleSheet("QDialog {\n"
"background-color:black;\n"
"}")
        self.timeEdit = QtWidgets.QTimeEdit(Timer)
        self.timeEdit.setGeometry(QtCore.QRect(30, 40, 151, 22))
        self.timeEdit.setStyleSheet("QTimeEdit {\n"
"border-radius:25px;\n"
"background-color:rgb(240, 240, 241)\n"
"}")
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(Timer)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(0, 244, 138);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Timer)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 70, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(0, 255, 255);\n"
"font-size: 20px\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Timer)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 191, 22))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border-radius:5px;\n"
"background-color:rgb(240, 240, 241)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Timer)
        QtCore.QMetaObject.connectSlotsByName(Timer)

    def retranslateUi(self, Timer):
        _translate = QtCore.QCoreApplication.translate
        Timer.setWindowTitle(_translate("Timer", "Timer"))
        self.pushButton.setText(_translate("Timer", "Done"))
        self.pushButton_2.setText(_translate("Timer", "Back"))
        self.lineEdit.setText(_translate("Timer", "    What u want to see here ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Timer = QtWidgets.QDialog()
    ui = Ui_Timer()
    ui.setupUi(Timer)
    Timer.show()
    sys.exit(app.exec())
