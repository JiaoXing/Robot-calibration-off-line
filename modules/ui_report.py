# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
from .img_rc import *


class Ui_Report(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 130)
        Form.setMinimumSize(QSize(550, 130))
        Form.setMaximumSize(QSize(550, 520))
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
"background-color: rgb(0, 0, 0);\n"
" border-radius: 8px;\n"
"\n"
"}\n"
"QLabel{\n"
"  font: 10pt \"\u6977\u4f53\";\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"QLabel#label{\n"
"\n"
" color: rgb(255, 255, 255);\n"
" border-image: url(:/Image/\u56fe\u6807.png);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
" border-radius: 3px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton#pushButton_exit,QPushButton#pushButton_save{\n"
" color: rgb(255, 255, 255);\n"
" background-color:rgb(30, 194, 27);\n"
" font: 12pt \"\u9ed1\u4f53\";\n"
" border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton#pushButton_exit:hover{\n"
" background-color: rgb(255, 52, 2);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_exit:pressed{\n"
" background-color: rgb(182, 34, 5)\n"
"}\n"
"\n"
"	QPushButton#pushButton_ok:hover,QPushButton#pushButton_save:hover{\n"
" background-color: rgb(26, 173, 25);\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:pressed,QPushButton#pushButton_save:pressed{\n"
" background-color: rg"
                        "b(31, 200, 28);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 550, 130))
        font = QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(500, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 5, 40, 35))
        self.label2 = QLabel(self.frame)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(140, 10, 251, 20))
        self.pushButton_save = QPushButton(self.frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(450, 60, 91, 61))
        self.label3 = QLabel(self.frame)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(20, 50, 71, 30))
        self.lineEdit1 = QLineEdit(self.frame)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(110, 50, 110, 30))
        self.lineEdit1.setFont(font)
        self.label3_2 = QLabel(self.frame)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setGeometry(QRect(20, 90, 71, 30))
        self.lineEdit2 = QLineEdit(self.frame)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(110, 90, 281, 30))
        self.lineEdit2.setFont(font)

        self.retranslateUi(Form)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot calibration off-line", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.label.setText("")
        self.label2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">\u673a \u5668 \u4eba \u79bb\u7ebf\u6807\u5b9a \u62a5\u544a\u751f\u6210</span></p></body></html>", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.label3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u673a\u5668\u4eba\u540d\u79f0:</p></body></html>", None))
        self.label3_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u4fdd\u5b58\u76ee\u5f55:</p></body></html>", None))
    # retranslateUi

