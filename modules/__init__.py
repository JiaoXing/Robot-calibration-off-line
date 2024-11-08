# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
from .img_rc import *

from pyDes import des, CBC, PAD_PKCS5
import sqlite3
from datetime import datetime

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QWidget, QLabel, QLineEdit,
                               QPushButton)

# GUI FILE
from .ui_main import Ui_MainWindow
from .ui_main_1 import Ui_MainWindow_1
from .ui_main_2 import Ui_MainWindow_2
from .ui_qmessagebox import Ui_QMessageBoxWindow
from .ui_work import Ui_WorkWindow
from .ui_help import Ui_Help
from .ui_report import Ui_Report
from .register import Register
from .my_Sqlite3 import my_Sqlite3
