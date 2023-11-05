# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,QSize, Qt)
from PySide6.QtGui import (QCursor,QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton)
from . img_rc import *

class Ui_MainWindow_2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 300)
        Form.setMinimumSize(QSize(200, 300))
        Form.setMaximumSize(QSize(200, 300))
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
                           " border-image:url(:/Image/\u4e8c\u7ef4\u7801.jpg);\n"
                           " border-radius: 8px;\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QPushButton#pushButton_exit{\n"
                           " color: rgb(255, 255, 255);\n"
                           " background-color:rgb(30, 194, 27);\n"
                           " font: 12pt \"\u9ed1\u4f53\";\n"
                           " border-radius: 5px;\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QPushButton#pushButton_exit:hover{\n"
                           " background-color: rgb(255, 52, 2);\n"
                           "\n"
                           "}\n"
                           "\n"
                           "QPushButton#pushButton_exit:pressed{\n"
                           " background-color: rgb(182, 34, 5)\n"
                           "}\n"
                           "\n"
                           "\n"
                           "\n"
                           "\n"
                           "\n"
                           "\n"
                           "")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 200, 250))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label2 = QLabel(self.frame)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(0, 196, 200, 40))
        self.label2.setMinimumSize(QSize(200, 40))
        self.label2.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        self.label2.setFont(font)
        self.label2.setStyleSheet(u"")
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(150, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))

        self.retranslateUi(Form)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot calibration off-line", None))
        self.label2.setText(QCoreApplication.translate("Form",
                                                       u"<html><head/><body><p align=\"center\">\u6dfb\u52a0\u597d\u53cb\uff1a\u53d1\u9001\u673a\u5668\u7279\u5f81\u7801</p></body></html>",
                                                       None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
    # retranslateUi
