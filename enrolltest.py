# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enrolltest.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from welcometest import Ui_MainWindow
import mysql.connector
import facerecognize
import detector

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
    def welcomeWindowShow(self):
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
	
    def detectorCheck(self):
        import detector
        detector.finalrecognition()

    def trainCheck(self):
        import trainer
        trainer.trainertest()	    
    
    def enrollCheck(self):
        username = unicode(self.lineEdit_3.text())
        conn=mysql.connector.connect(user='root',password='',host='localhost',database='deepblue_attendance',port=3306)
        mycursor=conn.cursor()
        result = mycursor.execute("SELECT * FROM enrolement WHERE student_id=%s"%username) 
        if(len(mycursor.fetchall()) > 0):
            print("User Found ! ")
            facerecognize.set(username)
            facerecognize.test()
        else:
            print("User Not Found !")
            self.showMessageBox('Warning','Student is not registered!!Read Note')
		
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(693, 529)
        Dialog.setAutoFillBackground(False)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 200, 181, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ###############event################
        self.pushButton.clicked.connect(self.enrollCheck)
		##########################################
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(150, 160, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 460, 141, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        ######################################event########
        self.pushButton_2.clicked.connect(self.trainCheck)
        ##########################################
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 691, 131))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 150, 301, 41))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 460, 141, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        ######################################event########
        self.pushButton_3.clicked.connect(self.detectorCheck)
        ##########################################
        self.textEdit_3 = QtGui.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(200, 360, 271, 41))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 433, 71, 20))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 87 14pt \"Arial Black\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(550, 430, 81, 20))
        self.label_4.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"font: 87 14pt \"Arial Black\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Student\'s ID", None))
        self.pushButton.setText(_translate("Dialog", "Enroll Now", None))
        self.pushButton_2.setText(_translate("Dialog", "TRAIN ", None))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#c10000;\">NOTE</span><span style=\" font-size:8pt; text-decoration: underline; color:#c10000;\">: </span><span style=\" font-size:10pt; color:#c10000;\">For Enrolling  Student enter Student\'s ID  given at the time of Registration and Click on </span><span style=\" font-size:10pt; font-weight:600; color:#c10000;\">&quot;Enroll&quot; </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#c10000;\">Once Enrollment for an Event is Complete,for Attendace Marking do following Steps-</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#c10000;\">1.Train the database by clicking on </span><span style=\" font-size:10pt; font-weight:600; color:#c10000;\">&quot;Train&quot;</span><span style=\" font-size:10pt; color:#c10000;\"> .</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#c10000;\">2.Mark the attendace by clicking on &quot;</span><span style=\" font-size:10pt; font-weight:600; color:#c10000;\">MARK ATTEDANCE&quot;</span></p></body></html>", None))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#2d0a78;\">  STUDENT ENROLLMENT</span></p></body></html>", None))
        self.pushButton_3.setText(_translate("Dialog", "MARK ATTENDANCE", None))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#1e0e78;\">ATTENDANCE MARKING</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "STEP-1", None))
        self.label_4.setText(_translate("Dialog", "STEP-2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

