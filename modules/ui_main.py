# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit,
                               QPushButton)
from . img_rc import *

class Ui_MainWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 300)
        Form.setMinimumSize(QSize(240, 300))
        Form.setMaximumSize(QSize(300, 300))
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
"border-image: url(:/Image/\u80cc\u666f.png);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QLabel#label1{\n"
"color: rgb(255, 255, 255);\n"
"border-image: url(:/Image/\u56fe\u6807.png);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 10pt \"\u6977\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:transparent;\n"
"font: 10pt \"\u6977\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:1px solid lightgray\n"
"}\n"
"\n"
"QPushButton#pushButton_Small,QPushButton#pushButton_exit{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(30, 194, 27);\n"
"font: 12pt \"\u9ed1\u4f53\";\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_Small:hover{\n"
"background-color: rgb(26, 173, 25);\n"
"}\n"
"\n"
"QPushButton#pushButton_Small:pressed{\n"
"background-color: rgb(31, 200, 28);\n"
"}\n"
"\n"
"QPushButton#pushButton_exit:hover{\n"
"background-color: rgb(255, 52, 2);\n"
"}\n"
"\n"
"QPushButton#pushButton_exit:pressed{\n"
"background-color: rgb(182, 34, 5"
                        ")\n"
"}\n"
"\n"
"QPushButton#pushButton_ok{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(30, 194, 27);\n"
"font: 12pt \"\u9ed1\u4f53\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:hover{\n"
"background-color: rgb(26, 173, 25);\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:pressed{\n"
"background-color: rgb(31, 200, 28);\n"
"}\n"
"\n"
"QPushButton#pushButton_tz,QPushButton#pushButton_zc{\n"
"background-color:transparent;\n"
"font: 10pt \"\u6977\u4f53\";\n"
"color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton#pushButton_tz:hover,QPushButton#pushButton_zc:hover{\n"
"color:rgb(26, 173, 25);\n"
"}\n"
"\n"
"QPushButton#pushButton_tz:pressed,QPushButton#pushButton_zc:pressed{\n"
"color:rgb(31, 200, 28);\n"
"}")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 240, 300))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_ok = QPushButton(self.frame)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(20, 210, 200, 50))
        self.pushButton_ok.setMinimumSize(QSize(200, 50))
        self.pushButton_ok.setMaximumSize(QSize(200, 50))
        self.pushButton_ok.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_ok.setStyleSheet(u"")
        self.pushButton_ok.setIconSize(QSize(20, 20))
        self.lineEdit_password = QLineEdit(self.frame)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(80, 170, 135, 25))
        self.lineEdit_password.setMinimumSize(QSize(135, 25))
        self.lineEdit_password.setMaximumSize(QSize(135, 25))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(u"")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.pushButton_tz = QPushButton(self.frame)
        self.pushButton_tz.setObjectName(u"pushButton_tz")
        self.pushButton_tz.setGeometry(QRect(22, 266, 93, 30))
        self.pushButton_tz.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_tz.setStyleSheet(u"")
        self.pushButton_zc = QPushButton(self.frame)
        self.pushButton_zc.setObjectName(u"pushButton_zc")
        self.pushButton_zc.setGeometry(QRect(130, 266, 93, 30))
        self.pushButton_zc.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_zc.setStyleSheet(u"")
        self.label2 = QLabel(self.frame)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(25, 160, 80, 40))
        self.label2.setMinimumSize(QSize(80, 40))
        self.label2.setMaximumSize(QSize(80, 40))
        self.label2.setStyleSheet(u"")
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(190, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))
        self.label1 = QLabel(self.frame)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(0, 5, 40, 35))
#if QT_CONFIG(shortcut)
        self.label2.setBuddy(self.lineEdit_password)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot calibration off-line", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ok.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_ok.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.lineEdit_password.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton_tz.setText(QCoreApplication.translate("Form", u"\u673a\u5668\u7279\u5f81\u7801", None))
        self.pushButton_zc.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.label2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c\u7801\uff1a", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.label1.setText("")
    # retranslateUi

