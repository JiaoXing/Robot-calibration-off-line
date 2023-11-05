# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_1.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
from . img_rc import *

class Ui_MainWindow_1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(272, 110)
        font = QFont()
        font.setPointSize(8)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
" background-color: rgb(0, 0, 0);\n"
" border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"  font: 10pt \"\u6977\u4f53\";\n"
"  color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTextEdit{\n"
"  font: 8pt \"\u6977\u4f53\";\n"
"color: rgb(0, 0, 0);\n"
" border-radius: 3px;\n"
"background-color: rgb(255, 255, 255);\n"
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
"\n"
"QPushButton#pushButton_exit:pressed{\n"
" background-color: rgb(182, 34, 5)\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 271, 110))
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(220, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 106, 36))
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 50, 231, 41))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.textEdit.setFont(font1)

        self.retranslateUi(Form)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot calibration off-line", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u673a\u5668\u7279\u5f81\u7801:", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u6977\u4f53'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
    # retranslateUi

