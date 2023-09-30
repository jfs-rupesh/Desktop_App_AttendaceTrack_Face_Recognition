# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from event import Ui_signUp
import mysql.connector

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    def signUpShow(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_signUp()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
		
    def loginCheck(self):
        username = unicode(self.lineEdit_3.text())
        self.username=username
        password = unicode(self.lineEdit_2.text())
        conn=mysql.connector.connect(user='root',password='',host='localhost',database='deepblue_attendance',port=3306)
        mycursor=conn.cursor()
        result = mycursor.execute("SELECT * FROM felicitator WHERE felicitator_username = %s AND felicitator_password = %s",(username,password))
        if(len(mycursor.fetchall()) > 0):
            print("User Found ! ")
            self.signUpWindow = QtGui.QDialog()
            self.ui = Ui_signUp()
            self.ui.setname(self.username)
            self.ui.setupUi(self.signUpWindow)
            self.signUpWindow.show()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Invalid Username And Password')
			
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(329, 244)
        Dialog.setAutoFillBackground(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 80, 171, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 140, 171, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ##############event###############
        self.pushButton.clicked.connect(self.loginCheck)
	    ##############
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bookman Old Style"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "     USERNAME", None))
        self.label_2.setText(_translate("Dialog", "    PASSWORD", None))
        self.pushButton.setText(_translate("Dialog", "LOGIN", None))
        self.label_3.setText(_translate("Dialog", "  LOGIN", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

