# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'work.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QWidget)
from . img_rc import *

class Ui_WorkWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 530)
        Form.setMinimumSize(QSize(590, 530))
        Form.setMaximumSize(QSize(600, 16777215))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        font.setPointSize(8)
        Form.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Image/\u56fe\u6807.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QFrame#frame {\n"
"background-color: #000000;\n"
"border-radius: 8px;\n"
"\n"
"}\n"
"\n"
"QGroupBox {\n"
"font: 12pt \"\u6977\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style:solid;\n"
"border-radius: 3px;\n"
"border-color:rgb(255, 255, 255);\n"
"margin-top:0.5ex;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"subcontrol-origin:margin;\n"
"subcontrol-position:top left;\n"
"left:10px;\n"
"padding:0 1px;\n"
"\n"
"}\n"
"\n"
"QLabel#label{\n"
" color: rgb(255, 255, 255);\n"
" border-image: url(:/Image/\u56fe\u6807.png);\n"
"\n"
"}\n"
"QLabel{\n"
" font: 12pt \"\u6977\u4f53\";\n"
" color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLabel#label2_1{\n"
" font: 8pt \"\u6977\u4f53\";\n"
" color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
" background-color:transparent;\n"
" font: 10pt \"\u6977\u4f53\";\n"
" color: rgb(255, 255, 255);\n"
" border:none;\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
" color: rgb(0, 0, 0);\n"
" border-radius: 3px;\n"
" background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
""
                        "QTableWidget          \n"
"{\n"
"    background:#FFFFFF;           \n"
"    border-radius:3px;    \n"
"    color:#666666;   \n"
"              \n"
"}\n"
"\n"
"\n"
"\n"
"QTableView QTableCornerButton::section \n"
"{\n"
"   border-style:solid;\n"
"   border-top-left-radius:3px;\n"
"   border-top-right-radius:0px;\n"
"   border-bottom-left-radius:0px;\n"
"   border-bottom-right-radius:0px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget::item::selected      \n"
"{\n"
"    color:red;                       \n"
"    background:#EFF4FF;           \n"
"}\n"
"QTableWidget::item:selected:active {\n"
"    background-color: #C0C0C0;\n"
"}\n"
"QTableWidget::item:selected:!active {\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QTableWidget::setItem\n"
"{\n"
"    color:red;                       \n"
"    background:#EFF4FF;           \n"
"}\n"
"\n"
"QHeaderView                    \n"
"{\n"
"	border:none; \n"
"	border-radius:3px; \n"
"    background:transparent;  \n"
"}\n"
"\n"
"QHeaderView::section      \n"
"{\n"
"    font-size:12px;"
                        "                \n"
"    color:#FFFFFF;             \n"
"    background:#60669B;           \n"
"    border:none;  \n"
"    width: 15px;  \n"
"    height:12px;    \n"
"	padding:3px; \n"
"	border-radius:3px; \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"    width: 10px;\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"    height: 11px;\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"    margin: 0px 0 0px 0;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical,QScrollBar::handle:horizontal {\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    background-color:  rgb(50, 100, 250);\n"
"    height: 60px;\n"
"    margin: 1px 0px 0px 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    borde"
                        "r: none;\n"
"    height: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"	border: none;\n"
"    width: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    width: 0px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::down-arrow:vertica,QScrollBar::down-arrow:horizontal {\n"
"    border:none;\n"
"}\n"
"QScrollBar::up-arrow:vertical,QScrollBar::up-arrow:horizontal {\n"
"    border:none;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::add-page:horizontal{\n"
"    background-color: rgba(50, 100, 250, 100);\n"
"}\n"
"QScrollBar::sub-page:vertical,QScrollBar::sub-page:horizontal {\n"
"    background-color: rgba(50, 100, 250, 100);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"   \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton#pushButton_move{\n"
" color: rgb(0, 0, 0);\n"
" backgro"
                        "und: transparent;\n"
" border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_help,QPushButton#pushButton_Small,QPushButton#pushButton_exit{\n"
" color: rgb(255, 255, 255);\n"
" background-color:rgb(30, 194, 27);\n"
" font: 12pt \"\u9ed1\u4f53\";\n"
" border-radius: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_help:hover{\n"
" background-color: rgb(26, 173, 25);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_help:pressed{\n"
" background-color: rgb(31, 200, 28);\n"
"}\n"
"\n"
"QPushButton#pushButton_Small:hover{\n"
" background-color: rgb(26, 173, 25);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_Small:pressed{\n"
" background-color: rgb(31, 200, 28);\n"
"}\n"
"\n"
"QPushButton#pushButton_exit:hover{\n"
" background-color: rgb(255, 52, 2);\n"
"}\n"
"\n"
"QPushButton#pushButton_exit:pressed{\n"
" background-color: rgb(182, 34, 5)\n"
"}\n"
"\n"
"QPushButton#pushButton_dr_robot,QPushButton#pushButton_dr_3d,QPushButton#pushButton_zbzh,QPushButton#pushButton_toolbox,QPushButton#pushButton_report{\n"
" color: r"
                        "gb(255, 255, 255);\n"
" background-color: rgb(128, 128, 128);\n"
" font: 12pt \"\u9ed1\u4f53\";\n"
" border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton#pushButton_dr_robot:hover,QPushButton#pushButton_dr_3d:hover,QPushButton#pushButton_zbzh:hover,QPushButton#pushButton_toolbox:hover,QPushButton#pushButton_report:hover{\n"
" background-color: rgb(160, 160, 160);\n"
"}\n"
"QPushButton#pushButton_dr_robot:pressed,QPushButton#pushButton_dr_3d:pressed,QPushButton#pushButton_zbzh:pressed,QPushButton#pushButton_toolbox:pressed,QPushButton#pushButton_report:pressed{\n"
" background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_ok{\n"
" color: rgb(255, 255, 255);\n"
" background-color:rgb(30, 194, 27);\n"
" font: 12pt \"\u9ed1\u4f53\";\n"
" border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:hover{\n"
" background-color: rgb(26, 173, 25);\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:pressed{\n"
" background-color: rgb(31, 200, 28);\n"
"}\n"
"\n"
"QRadioButton{\n"
" color: rgb(255, 255, 255);\n"
""
                        "}\n"
"\n"
"\n"
"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 590, 530))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_ok = QPushButton(self.frame)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(460, 436, 121, 80))
        self.pushButton_ok.setMinimumSize(QSize(50, 50))
        self.pushButton_ok.setMaximumSize(QSize(240, 80))
        self.pushButton_ok.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_ok.setStyleSheet(u"")
        self.pushButton_ok.setIconSize(QSize(20, 20))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 5, 40, 35))
        self.pushButton_Small = QPushButton(self.frame)
        self.pushButton_Small.setObjectName(u"pushButton_Small")
        self.pushButton_Small.setGeometry(QRect(495, 10, 40, 30))
        self.pushButton_Small.setMinimumSize(QSize(40, 30))
        self.pushButton_Small.setMaximumSize(QSize(40, 30))
        self.pushButton_Small.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_exit = QPushButton(self.frame)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(540, 10, 40, 30))
        self.pushButton_exit.setMinimumSize(QSize(40, 30))
        self.pushButton_exit.setMaximumSize(QSize(40, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_help = QPushButton(self.frame)
        self.pushButton_help.setObjectName(u"pushButton_help")
        self.pushButton_help.setGeometry(QRect(450, 10, 40, 30))
        self.pushButton_help.setMinimumSize(QSize(40, 30))
        self.pushButton_help.setMaximumSize(QSize(40, 30))
        self.pushButton_help.setCursor(QCursor(Qt.OpenHandCursor))
        self.label4 = QLabel(self.frame)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(0, 220, 30, 131))
        self.label2 = QLabel(self.frame)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(160, 20, 181, 20))
        self.label3 = QLabel(self.frame)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(0, 60, 30, 150))
        self.textEdit3 = QTextEdit(self.frame)
        self.textEdit3.setObjectName(u"textEdit3")
        self.textEdit3.setGeometry(QRect(10, 436, 441, 81))
        font1 = QFont()
        font1.setPointSize(8)
        self.textEdit3.setFont(font1)
        self.textEdit3.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(390, 210, 190, 215))
        self.label4_2 = QLabel(self.groupBox)
        self.label4_2.setObjectName(u"label4_2")
        self.label4_2.setGeometry(QRect(10, 140, 181, 21))
        self.label7_2 = QLabel(self.groupBox)
        self.label7_2.setObjectName(u"label7_2")
        self.label7_2.setGeometry(QRect(30, 160, 16, 16))
        self.label7_2.setStyleSheet(u"")
        self.label8_2 = QLabel(self.groupBox)
        self.label8_2.setObjectName(u"label8_2")
        self.label8_2.setGeometry(QRect(80, 160, 16, 16))
        self.label8_2.setStyleSheet(u"")
        self.label9_2 = QLabel(self.groupBox)
        self.label9_2.setObjectName(u"label9_2")
        self.label9_2.setGeometry(QRect(130, 160, 16, 16))
        self.label9_2.setStyleSheet(u"")
        self.lineEdit4 = QLineEdit(self.groupBox)
        self.lineEdit4.setObjectName(u"lineEdit4")
        self.lineEdit4.setGeometry(QRect(30, 180, 40, 16))
        self.lineEdit4.setStyleSheet(u"")
        self.lineEdit5 = QLineEdit(self.groupBox)
        self.lineEdit5.setObjectName(u"lineEdit5")
        self.lineEdit5.setGeometry(QRect(80, 180, 40, 16))
        self.lineEdit5.setStyleSheet(u"")
        self.lineEdit6 = QLineEdit(self.groupBox)
        self.lineEdit6.setObjectName(u"lineEdit6")
        self.lineEdit6.setGeometry(QRect(130, 180, 40, 16))
        self.lineEdit6.setStyleSheet(u"")
        self.label6 = QLabel(self.groupBox)
        self.label6.setObjectName(u"label6")
        self.label6.setGeometry(QRect(10, 80, 141, 20))
        self.label5 = QLabel(self.groupBox)
        self.label5.setObjectName(u"label5")
        self.label5.setGeometry(QRect(10, 20, 91, 21))
        self.radioButton1 = QRadioButton(self.groupBox)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton1)
        self.radioButton1.setObjectName(u"radioButton1")
        self.radioButton1.setGeometry(QRect(30, 40, 80, 20))
        self.radioButton1.setStyleSheet(u"")
        self.radioButton1.setChecked(True)
        self.radioButton2 = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.radioButton2)
        self.radioButton2.setObjectName(u"radioButton2")
        self.radioButton2.setGeometry(QRect(30, 60, 80, 20))
        self.radioButton2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.radioButton3 = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.radioButton3)
        self.radioButton3.setObjectName(u"radioButton3")
        self.radioButton3.setGeometry(QRect(100, 40, 80, 16))
        self.radioButton3.setStyleSheet(u"")
        self.radioButton3.setChecked(False)
        self.radioButton4 = QRadioButton(self.groupBox)
        self.buttonGroup.addButton(self.radioButton4)
        self.radioButton4.setObjectName(u"radioButton4")
        self.radioButton4.setGeometry(QRect(100, 60, 80, 16))
        self.radioButton4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label7 = QLabel(self.groupBox)
        self.label7.setObjectName(u"label7")
        self.label7.setGeometry(QRect(30, 100, 54, 16))
        self.label7.setStyleSheet(u"")
        self.lineEdit1 = QLineEdit(self.groupBox)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(30, 120, 51, 16))
        self.lineEdit1.setStyleSheet(u"")
        self.label8 = QLabel(self.groupBox)
        self.label8.setObjectName(u"label8")
        self.label8.setGeometry(QRect(80, 100, 54, 16))
        self.label8.setStyleSheet(u"")
        self.lineEdit2 = QLineEdit(self.groupBox)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(80, 120, 51, 16))
        self.lineEdit2.setStyleSheet(u"")
        self.label9 = QLabel(self.groupBox)
        self.label9.setObjectName(u"label9")
        self.label9.setGeometry(QRect(130, 100, 54, 16))
        self.label9.setStyleSheet(u"")
        self.lineEdit3 = QLineEdit(self.groupBox)
        self.lineEdit3.setObjectName(u"lineEdit3")
        self.lineEdit3.setGeometry(QRect(130, 120, 51, 16))
        self.lineEdit3.setStyleSheet(u"")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(40, 365, 341, 61))
        self.pushButton_report = QPushButton(self.groupBox_2)
        self.pushButton_report.setObjectName(u"pushButton_report")
        self.pushButton_report.setGeometry(QRect(250, 10, 80, 43))
        self.pushButton_report.setMinimumSize(QSize(50, 20))
        self.pushButton_report.setMaximumSize(QSize(240, 90))
        self.pushButton_report.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_report.setStyleSheet(u"")
        self.pushButton_report.setIconSize(QSize(20, 20))
        self.pushButton_toolbox = QPushButton(self.groupBox_2)
        self.pushButton_toolbox.setObjectName(u"pushButton_toolbox")
        self.pushButton_toolbox.setGeometry(QRect(130, 10, 80, 43))
        self.pushButton_toolbox.setMinimumSize(QSize(50, 20))
        self.pushButton_toolbox.setMaximumSize(QSize(240, 90))
        self.pushButton_toolbox.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_toolbox.setStyleSheet(u"")
        self.pushButton_toolbox.setIconSize(QSize(20, 20))
        self.pushButton_zbzh = QPushButton(self.groupBox_2)
        self.pushButton_zbzh.setObjectName(u"pushButton_zbzh")
        self.pushButton_zbzh.setGeometry(QRect(10, 10, 80, 43))
        self.pushButton_zbzh.setMinimumSize(QSize(50, 20))
        self.pushButton_zbzh.setMaximumSize(QSize(240, 90))
        self.pushButton_zbzh.setCursor(QCursor(Qt.OpenHandCursor))
        self.pushButton_zbzh.setStyleSheet(u"")
        self.pushButton_zbzh.setIconSize(QSize(20, 20))
        self.label5_2 = QLabel(self.frame)
        self.label5_2.setObjectName(u"label5_2")
        self.label5_2.setGeometry(QRect(0, 370, 30, 51))
        self.textEdit1 = QTextEdit(self.frame)
        self.textEdit1.setObjectName(u"textEdit1")
        self.textEdit1.setGeometry(QRect(40, 50, 541, 151))
        self.textEdit1.setFont(font1)
        self.textEdit1.setStyleSheet(u"")
        self.textEdit2 = QTextEdit(self.frame)
        self.textEdit2.setObjectName(u"textEdit2")
        self.textEdit2.setGeometry(QRect(40, 210, 341, 150))
        self.textEdit2.setFont(font1)
        self.textEdit2.setStyleSheet(u"")
        self.label2_1 = QLabel(self.frame)
        self.label2_1.setObjectName(u"label2_1")
        self.label2_1.setGeometry(QRect(350, 20, 31, 20))

        self.retranslateUi(Form)
        self.pushButton_Small.clicked.connect(Form.showMinimized)
        self.pushButton_exit.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Robot calibration off-line", None))
#if QT_CONFIG(tooltip)
        self.pushButton_ok.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_ok.setText(QCoreApplication.translate("Form", u"\u6267\u884c", None))
        self.label.setText("")
        self.pushButton_Small.setText(QCoreApplication.translate("Form", u"\u4e00", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_help.setText(QCoreApplication.translate("Form", u"?", None))
        self.label4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">\u4e09</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u5750</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u6807</span></p></body></html>", None))
        self.label2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#ffffff;\">\u673a \u5668 \u4eba \u79bb\u7ebf \u6807\u5b9a\u8f6f\u4ef6</span></p></body></html>", None))
        self.label3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">\u673a</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u5668</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u4eba</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u5750</span></p><p align=\"right\"><span style=\" color:#ffffff;\">\u6807</span></p><p align=\"right\"><br/></p><p align=\"right\"><br/></p></body></html>", None))
        self.textEdit3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5de5\u5177\u5750\u6807:[[X, Y, Z]]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5916\u90e8\u5de5\u5177\u5750\u6807:[[X, Y, Z]]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5de5\u4ef6\u5750\u6807:[[X, Y, Z]] Q4:[[q1,q2,q3"
                        ",q4]]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u8ba1\u7b97\u8bef\u5dee:0.000000000</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8bbe\u5b9a", None))
        self.label4_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u5916\u90e8 TCP,\u4e09\u5750\u6807\u6d4b\u91cf\u70b9:</span></p></body></html>", None))
        self.label7_2.setText(QCoreApplication.translate("Form", u"X:", None))
        self.label8_2.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.label9_2.setText(QCoreApplication.translate("Form", u"Z:", None))
        self.lineEdit4.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit5.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit6.setText(QCoreApplication.translate("Form", u"0", None))
        self.label6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">\u5de5\u5177\u5750\u6807\u9884\u4f30\u503c\uff1a</span></p></body></html>", None))
        self.label5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#ffffff;\">\u673a\u5668\u4eba\u54c1\u724c\uff1a</span></p></body></html>", None))
        self.radioButton1.setText(QCoreApplication.translate("Form", u"ABB", None))
        self.radioButton2.setText(QCoreApplication.translate("Form", u"KUKA", None))
        self.radioButton3.setText(QCoreApplication.translate("Form", u"FANUC", None))
        self.radioButton4.setText(QCoreApplication.translate("Form", u"YASKAWA", None))
        self.label7.setText(QCoreApplication.translate("Form", u"X:", None))
        self.lineEdit1.setText(QCoreApplication.translate("Form", u"0", None))
        self.label8.setText(QCoreApplication.translate("Form", u"Y:", None))
        self.lineEdit2.setText(QCoreApplication.translate("Form", u"0", None))
        self.label9.setText(QCoreApplication.translate("Form", u"Z:", None))
        self.lineEdit3.setText(QCoreApplication.translate("Form", u"1000", None))
        self.groupBox_2.setTitle("")
#if QT_CONFIG(tooltip)
        self.pushButton_report.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_report.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u62a5\u544a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_toolbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_toolbox.setText(QCoreApplication.translate("Form", u"\u5de5\u5177\u7bb1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_zbzh.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_zbzh.setText(QCoreApplication.translate("Form", u"\u5750\u6807\u8f6c\u6362", None))
        self.label5_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"right\">\u5de5</p><p align=\"right\">\u5177</p></body></html>", None))
        self.textEdit1.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b91:[X,Y,Z],[0,0,0,0] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b92:[X,Y,Z],[0,0,0,0] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><spa"
                        "n style=\" font-size:9pt;\">\u70b93:[X,Y,Z],[0,0,0,0] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b94:[X,Y,Z],[0,0,0,0] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b95:[X,Y,Z],[0,0,0,0] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b96:[X,Y,Z],[0,0,0,0] </span></p></body></html>", None))
        self.textEdit2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b91:[X,Y,Z] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b92:[X,Y,Z] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size"
                        ":9pt;\">\u70b93:[X,Y,Z] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b94:[X,Y,Z] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b95:[X,Y,Z] </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">\u70b96:[X,Y,Z] </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.label2_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>v</p></body></html>", None))
    # retranslateUi

