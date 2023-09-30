# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'event.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from enrolltest import Ui_Dialog
import mysql.connector
import sys 
import os
import facerecognize
import trainer
import detector

c=0
list=[]
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

class Ui_signUp(object):
    def welcomeWindowShow(self):
        self.welcomeWindow = QtGui.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
		
    def eventCheck(self):
        eventname=self.comboBox.currentText()   
        facerecognize.setevent(eventname)
        trainer.setevent(eventname)
        detector.setevent(eventname)
        cur=os.getcwd()
        path=cur
        if not os.path.exists(str(eventname)):
            os.makedirs(str(eventname))
        self.welcomeWindowShow()
	
    def setname(self,username): 
        global c
        conn=mysql.connector.connect(user='root',password='',host='localhost',database='deepblue_attendance',port=3306)
        mycursor=conn.cursor()
        mycursor.execute("SELECT heading FROM event WHERE felicitator2_id = '%s'"%username)
        row=mycursor.fetchall()
        count=mycursor.rowcount 
        if((mycursor.rowcount) > 0):
            for row in row:
                print row[0]
                list.insert(c,row[0])
                c=c+1
        else:
		    print("no entry")
        print(c)
	
    def setupUi(self, Dialog):
        global c
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(397, 300)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 120, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        while(c!=0):
            c=c-1
            self.comboBox.addItem(unicode(list[c]))         
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 200, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
		######################################event########
        self.pushButton.clicked.connect(self.eventCheck)
		##########################################
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 80, 231, 41))
        self.label.setSizeIncrement(QtCore.QSize(20, 10))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Submit", None))
        self.label.setText(_translate("Dialog", "   SELECT EVENT FOR ENROLLMENT", None))
        self.label_2.setText(_translate("Dialog", "  EVENT MANAGEMENT", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_signUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

