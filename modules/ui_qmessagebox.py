# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qmessagebox.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,QSize, Qt)
from PySide6.QtGui import (QCursor,QIcon)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton)
from . img_rc import *

class Ui_QMessageBoxWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 139)
        Form.setMinimumSize(QSize(200, 50))
        Form.setMaximumSize(QSize(200, 300))
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
                           "	background-color: rgb(0, 0, 0);\n"
                           " border-radius: 8px;\n"
                           "\n"
                           "}\n"
                           "QLabel{\n"
                           "  font: 10pt \"\u6977\u4f53\";\n"
                           "  color: rgb(255, 255, 255);\n"
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
        self.frame.setGeometry(QRect(0, 0, 200, 50))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(150, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 120, 30))

        self.retranslateUi(Form)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot_calibration_off-line", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c\u7801\u9519\u8bef", None))
    # retranslateUi
