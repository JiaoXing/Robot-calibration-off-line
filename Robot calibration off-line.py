# -*- coding: utf-8 -*-
"""
# @Project  :Python
# @File     :Main_启动
# @Date     :2022/11/28 9:47
# @Author   :叫猩
# @Email    :1027918098@qq.com
# @Software :PyCharm
"""
import time, re, sys
# 加密
# 窗口UI文件调用地址
from modules import *
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image as excel_Image

# 离线标定算法
from re import findall
from matplotlib import pyplot as plt
from matplotlib import patches as mp
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from numpy import *
from scipy.optimize import leastsq
from scipy.spatial.transform import Rotation


class Window(QWidget):
    TZ = register()
    def __init__(self):
        super().__init__()
        self.Window = None
        self.mainwindow_1 = None
        self.mainwindow_2 = None
        self.windowqmessagebox = None
        self.main()
        pass

    def main(self):
        self.Window = MainWindow()
        self.Window.Si_MainWindow_1.connect(self.MainWindow_1)
        self.Window.Si_MainWindow_2.connect(self.MainWindow_2)
        self.Window.Si_WindowQMessageBox.connect(self.WindowQMessageBox)
        self.Window.Si_WorkWindow.connect(self.WorkWindow)
        self.Window.show()

    def MainWindow_1(self):
        self.mainwindow_1 = MainWindow_1()
        self.mainwindow_1.show()

    def MainWindow_2(self):
        self.mainwindow_2 = MainWindow_2()
        self.mainwindow_2.show()

    def WindowQMessageBox(self, qmessage):

        self.windowqmessagebox = WindowQMessageBox()
        self.windowqmessagebox.ui.label.setText(qmessage)
        self.windowqmessagebox.show()

    def WorkWindow(self):
        self.workwindow = WorkWindow()
        self.Window.close()
        if self.mainwindow_1 != None:
            self.mainwindow_1.close()
        if self.mainwindow_2 != None:
            self.mainwindow_2.close()
        if self.windowqmessagebox != None:
            self.windowqmessagebox.close()
        self.workwindow.show()


class MainWindow(QWidget):
    Si_MainWindow_1 = Signal()
    Si_MainWindow_2 = Signal()
    Si_WorkWindow = Signal()
    Si_WindowQMessageBox = Signal(str)

    # 窗口UI属性
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)

        # # 信号槽
        self.ui.pushButton_tz.clicked.connect(self.pushButton_tz)
        self.ui.pushButton_zc.clicked.connect(self.pushButton_zc)
        self.ui.pushButton_ok.clicked.connect(self.pushButton_ok)

    def pushButton_tz(self):
        self.Si_MainWindow_1.emit()

    def pushButton_zc(self):
        self.Si_MainWindow_2.emit()

    def pushButton_ok(self):
        self.ok, self.qmessage = Window.TZ.checkAuthored()
        if self.ok == 1:
            self.Si_WorkWindow.emit()
        else:
            if len(self.ui.lineEdit_password.text()) > 5:
                Window.TZ.regist(self.ui.lineEdit_password.text())  # 使用函数进行数据写入
            self.ok, self.qmessage = Window.TZ.checkAuthored()
            self.Si_WindowQMessageBox.emit(self.qmessage)
        # 处理异常的代码


class MainWindow_1(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_1()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)
        key_hash = Window.TZ.getCombinNumber()
        # # 信号槽
        self.ui.textEdit.setText(key_hash)


class MainWindow_2(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_2()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)


class WindowQMessageBox(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_QMessageBoxWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)
        self.ui.label.setText("")


class WorkWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.windowhelp = None
        self.window_3d = None
        self.windowReport = None
        self.ui = Ui_WorkWindow()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)

        self.ui.label2_1.setText('v2.1')  # 版本号
        # 信号槽
        self.ui.buttonGroup.buttonClicked.connect(self.buttonGroup)
        self.ui.pushButton_ok.clicked.connect(self.pushButton_ok)
        self.ui.pushButton_help.clicked.connect(self.pushButton_help)
        self.ui.pushButton_report.clicked.connect(self.pushButton_report)
        self.ui.pushButton_exit.clicked.connect(self.pushButton_exit)
        self.ui.textEdit1.dragEnterEvent = self.dragEnterEvent1
        self.ui.textEdit2.dragEnterEvent = self.dragEnterEvent2
        self.ui.textEdit1.dropEvent = self.dropEvent1
        self.ui.textEdit2.dropEvent = self.dropEvent2

        # 报告数据
        self.buttonGroup_name = None
        self.path_save = None
        self.content = None
        self.fig = None
        self.Robot_input = None
        self.Calibration_input = None
        self.Calculated_TCP = None
        self.Calculated_RTCP = None
        self.Calculated_Error = None
        self.Calculated_Rmse = None
        self.Orientation_Matrix = None
        self.Calculated_Base = None
        self.Orientation_Base = None
        self.Calculated_Frame = None
        self.Orientation_Frame = None

    # 重写鼠标事件
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drag = False

    def pushButton_exit(self):

        if self.windowhelp != None:
            self.windowhelp.close()
        if self.window_3d != None:
            self.window_3d.close()
        if self.windowReport != None:
            self.windowReport.close()

    def buttonGroup(self):
        buttonGroup_name = self.ui.buttonGroup.checkedButton().text()

        if buttonGroup_name == "ABB":
            self.ui.textEdit1.setText(
                "点1:[X,Y,Z],[0,0,0,0] \n点2:[X,Y,Z],[0,0,0,0] \n点3:[X,Y,Z],[0,0,0,0] \n点4:[X,Y,Z],[0,0,0,0] \n点5:[X,Y,Z],[0,0,0,0] \n点6:[X,Y,Z],[0,0,0,0] \n")
        elif buttonGroup_name == "KUKA":
            self.ui.textEdit1.setText(
                "点1:[X,Y,Z],[0,0,0] \n点2:[X,Y,Z],[0,0,0] \n点3:[X,Y,Z],[0,0,0] \n点4:[X,Y,Z],[0,0,0] \n点5:[X,Y,Z],[0,0,0] \n点6:[X,Y,Z],[0,0,0] \n")
        elif buttonGroup_name == "FANUC":
            self.ui.textEdit1.setText(
                "点1:[X,Y,Z],[0,0,0] \n点2:[X,Y,Z],[0,0,0] \n点3:[X,Y,Z],[0,0,0] \n点4:[X,Y,Z],[0,0,0] \n点5:[X,Y,Z],[0,0,0] \n点6:[X,Y,Z],[0,0,0] \n")
        elif buttonGroup_name == "YASKAWA":
            self.ui.textEdit1.setText(
                "点1:[X,Y,Z],[0,0,0] \n点2:[X,Y,Z],[0,0,0] \n点3:[X,Y,Z],[0,0,0] \n点4:[X,Y,Z],[0,0,0] \n点5:[X,Y,Z],[0,0,0] \n点6:[X,Y,Z],[0,0,0] \n")

    def pushButton_ok(self):
        self.buttonGroup_name = self.ui.buttonGroup.checkedButton().text()
        if self.buttonGroup_name != "":
            try:
                A, tR = self.getDataA(self.ui.textEdit1.toPlainText())
            except:
                # 处理异常的代码
                self.windowqmessagebox = WindowQMessageBox()
                self.windowqmessagebox.ui.label.setText("机器人数据错误:")
                self.windowqmessagebox.show()
            try:
                B = self.getDataB(self.ui.textEdit2.toPlainText())
            except:
                # 处理异常的代码
                self.windowqmessagebox = WindowQMessageBox()
                self.windowqmessagebox.ui.label.setText("三坐标数据错误:")
                self.windowqmessagebox.show()
            TEXT = self.Rigid_tT_3D(self.buttonGroup_name, A, B, tR)
            self.ui.textEdit3.setText(TEXT)
            self.deta_txt(self.buttonGroup_name, self.ui.textEdit1.toPlainText(), self.ui.textEdit2.toPlainText(), TEXT)
        else:
            pass

    def pushButton_help(self):
        self.windowhelp = WorkHelp()
        self.windowhelp.show()

    def pushButton_report(self):
        self.windowReport = WorkReport()
        self.windowReport.show()

        self.windowReport.buttonGroup_name = self.buttonGroup_name
        if self.path_save != None:
            self.windowReport.ui.lineEdit2.setText(self.path_save.rsplit('/', 1)[0])
        self.windowReport.content = self.content
        self.windowReport.fig = self.fig

        self.windowReport.Robot_input = self.Robot_input
        self.windowReport.Calibration_input = self.Calibration_input
        self.windowReport.Calculated_TCP = self.Calculated_TCP
        self.windowReport.Calculated_RTCP = self.Calculated_RTCP
        self.windowReport.Calculated_Error = self.Calculated_Error
        self.windowReport.Calculated_Rmse = format(around(self.Calculated_Rmse, 4))
        self.windowReport.Orientation_Matrix = self.Orientation_Matrix
        self.windowReport.Calculated_Base = self.Calculated_Base
        self.windowReport.Orientation_Base = self.Orientation_Base
        self.windowReport.Calculated_Frame = self.Calculated_Frame
        self.windowReport.Orientation_Frame = self.Orientation_Frame

    def dragEnterEvent1(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.ui.textEdit1.setText("")
        # 放下

    def dragEnterEvent2(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.ui.textEdit2.setText("")
        # 放下

    def dropEvent1(self, event: QDropEvent):
        for url in event.mimeData().urls():
            Robot = self.ui.buttonGroup.checkedButton().text()
            self.path = url.toLocalFile()
            self.path_save = url.toLocalFile()
            # 读取文本文件
            with open(self.path, 'r', encoding="utf-8") as file_A:
                DataA = file_A.read()

            if Robot == "ABB":
                # 匹配以“CONST robtarget”开头的行
                pattern = re.compile(r'^\s*CONST robtarget.*$', re.MULTILINE)
            elif Robot == "KUKA":
                # 匹配以“decl e6pos”开头的行
                pattern = re.compile(r'^\s*DECL E6POS.*$', re.MULTILINE)
                special_chars = re.compile(r'X (.*?),Y (.*?),Z (.*?),A (.*?),B (.*?),C (.*?),S (.*?)')
            elif Robot == "FANUC":
                # 匹配有 “{ }”的行
                pattern = re.compile(r'{(.*?)}', re.DOTALL)
            elif Robot == "YASKAWA":
                # 匹配以“decl e6pos”开头的行
                pattern = re.compile(r'^\s*DECL E6POS.*$', re.MULTILINE)

            matches = pattern.findall(DataA)
            self.ui.textEdit1.setText("")

            # 输出匹配到的行
            for DataA, number in zip(matches, range(1, len(matches) + 1)):
                # 构建新的文本字符串
                if Robot == "ABB":
                    start = DataA.index("[[")  # 找到列表的起始位置
                    end = DataA.index("]]")  # 找到列表的结束位置
                    matches = DataA[start + 2:end].split("],[")
                    # 构建新的文本字符串
                    DataA = "Print" + str(number) + "=[{}],[{}]".format(matches[0], matches[1])
                elif Robot == "KUKA":
                    matches = special_chars.findall(DataA)
                    matches = [s for s in matches[0]]
                    DataA = "Print" + str(number) + "=[{},{},{}],[{},{},{}]".format(matches[0], matches[1], matches[2],
                                                                                    matches[3], matches[4],
                                                                                    matches[5])
                elif Robot == "FANUC":
                    replaced_text = DataA.replace('\n', '')
                    replaced_text = replaced_text.replace('\t', '')
                    replaced = replaced_text.replace(' ', '')
                    x = re.findall(r"X=(-?\d+\.\d+)mm", replaced)
                    y = re.findall(r"Y=(-?\d+\.\d+)mm", replaced)
                    z = re.findall(r"Z=(-?\d+\.\d+)mm", replaced)
                    w = re.findall(r"W=(-?\d+\.\d+)deg", replaced)
                    p = re.findall(r"P=(-?\d+\.\d+)deg", replaced)
                    r = re.findall(r"R=(-?\d+\.\d+)deg", replaced)

                    DataA = "Print" + str(number) + "=[{},{},{}],[{},{},{}]".format(x[0], y[0], z[0],
                                                                                    w[0], p[0], r[0])
                elif Robot == "YASKAWA":
                    DataA = "Print" + str(number) + "=[{},{},{}],[{},{},{}]".format(matches[0], matches[1], matches[2],
                                                                                    matches[3], matches[4],
                                                                                    matches[5])
                self.ui.textEdit1.append(DataA)

    def dropEvent2(self, event: QDropEvent):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            # 读取文本文件
            with open(path, 'r', encoding="utf-8") as file_B:
                DataB = file_B.read()

            pattern = re.compile(r'^\s*..*$', re.MULTILINE)
            matches = pattern.findall(DataB)
            self.ui.textEdit2.setText("")
            # 输出匹配到的行
            for DataB, number in zip(matches, range(1, len(matches) + 1)):
                # matches = DataB.split('\t')
                matches = DataB.split(',')
                DataB = "P" + str(number) + "=[{},{},{}]".format(matches[-3], matches[-2], matches[-1])
                self.ui.textEdit2.append(DataB)

    # format 格式化
    def getDataA(self, text):
        # 获取text全部内容并去除内容中的空格,用split将内容以每一行末尾的\n分割成一个列表
        text = text.replace(" ", "")
        pat = r'\[(.*?)\]'
        text = findall(pat, text)
        N = len(text)
        M = int(N / 2)
        content = ones((M, 3))
        X = len(text[1].split(","))
        tR = ones((M, X))
        j = 0
        for i in range(0, N, 2):
            content[j, 0:3] = text[i].split(",")
            tR[j, 0:X] = text[i + 1].split(",")
            j += 1
        self.Robot_input = []
        list1 = content.tolist()
        list2 = tR.tolist()
        for i in range(len(list1)):
            self.Robot_input.append(list1[i] + list2[i])
        return content.tolist(), tR.tolist()

    # format 格式化
    def getDataB(self, text):
        # 获取text全部内容并去除内容中的空格,用split将内容以每一行末尾的\n分割成一个列表
        text = text.replace(" ", "")
        pat = r'\[(.*?)\]'
        text = findall(pat, text)
        N = len(text)
        content = ones((N, 3))
        for i in range(N):
            content[i, 0:3] = text[i].split(",")

        self.Calibration_input = content.tolist()
        return content.tolist()

    def rigid_transform_3D(self, Pa, Pb):
        assert len(Pa) == len(Pb)

        Pa = mat(Pa)
        Pb = mat(Pb)
        N = Pa.shape[0]
        mu_Pa = mean(Pa, axis=0)
        mu_Pb = mean(Pb, axis=0)

        AA = Pa - tile(mu_Pa, (N, 1))
        BB = Pb - tile(mu_Pb, (N, 1))
        H = (BB.T * AA)

        U, S, Vt = linalg.svd(H)
        R = Vt.T * U.T
        FR = R.I

        if linalg.det(R) < 0:
            print("检测到反射")
            Vt[2, :] *= -1
            R = Vt.T * U.T
            FR = R.I

        t = mu_Pa.T - R * mu_Pb.T
        Ft = mu_Pb.T - FR * mu_Pa.T

        return R, t, FR, Ft

    def Rigid_tT_3D(self, Robot, Pa, Pb, r):
        try:
            assert len(Pa) == len(Pb) == len(r)  # 断言Pa、Pb、r的长度相等
        except:
            # 处理异常的代码
            self.windowqmessagebox = WindowQMessageBox()
            self.windowqmessagebox.ui.label.setText("数据未一一对应:")
            self.windowqmessagebox.show()
        # 到旋转矩阵
        N = len(Pa)  # 获取Pa的长度
        tr = ones((N, 4, 4))  # 初始化tr
        for i in range(N):
            Pa[i].insert(N, 1)  # 将Pa[i]的最后一个元素插入1
            Pb[i].insert(N, 1)  # 将Pb[i]的最后一个元素插入1
            if Robot == "ABB":
                r[i].insert(4, r[i][0])  # 将r[i]的第一个元素插入到r[i]的第5个位置
                r[i].remove(r[i][0])  # 删除r[i]的第一个元素
                tr[i, :3, :3] = Rotation.from_quat(r[i]).as_matrix()  # 将四元数转换为旋转矩阵
            elif Robot == "KUKA":
                tr[i, 0:3, 0:3] = Rotation.from_euler('ZYX', r[i], degrees=True).as_matrix()  # 将欧拉角转换为旋转矩阵
            elif Robot == "FANUC" or Robot == "YASKAWA":
                tr[i, 0:3, 0:3] = Rotation.from_euler('xyz', r[i], degrees=True).as_matrix()  # 将欧拉角转换为旋转矩阵

            tr[i, 0:4, 3:4] = mat(Pa[i]).T  # 将Pa[i]转换为齐次坐标并赋值给tr[i, 0:4, 3:4]
            tr[i, 3:4, 0:3] = 0  # 将tr[i, 3:4, 0:3]赋值为0
        # 将Pa和Pb转换为矩阵
        Pa = mat(Pa)
        Pb = mat(Pb)

        MO_tr = tr - roll(tr, 1, axis=0)
        MO_Pb = Pb - roll(Pb, 1, axis=0)
        mu_tr = tr - mean(tr, axis=0)  # 计算tr的均值
        mu_Pb = Pb - mean(Pb, axis=0)  # 计算Pb的均值

        # 获取MX, MY, MZ的值
        MX, MY, MZ = map(float, [self.ui.lineEdit1.text(), self.ui.lineEdit2.text(), self.ui.lineEdit3.text()])
        if MX != 0 or MY != 0 or MZ != 1000:
            tT = [MX, MY, MZ]
        else:
            def TOOL(tool_xyz):
                X, Y, Z = tool_xyz[0], tool_xyz[1], tool_xyz[2]
                tool = mat([[X], [Y], [Z], [1]])
                system = []
                for i in range(N):
                    system.append(sum(array(MO_tr[i] * tool) ** 2) - sum(array(MO_Pb[i].T) ** 2))
                    system.append(sum(array(mu_tr[i] * tool) ** 2) - sum(array(mu_Pb[i].T) ** 2))

                return array(system)

            tT = leastsq(TOOL, [MX, MY, MZ])[0]  # 通过最小二乘法计算未知工具 X Y Z;

        tT = mat(append(tT, 1)).T  # 将计算出的 X Y Z 转换为齐次坐标;

        # 重新生成工具下的点集;
        Paa = ones((N, 4))
        for i in range(N):
            Paa[i] = (mat(tr[i]) * tT).T

        W_R, W_t, F_R, F_t = self.rigid_transform_3D(Paa, Pb)

        Pbb = (W_R.I * (Paa.T - tile(W_t, (1, N)))).T
        Error = Pbb - Pb
        SUM_Error = sum(multiply(Error, Error))
        self.Calculated_Rmse = sqrt(SUM_Error / N)
        TEXT = "Tcp:{}".format(around(tT[:3], 4).T.tolist())

        MX = float(self.ui.lineEdit4.text())
        MY = float(self.ui.lineEdit5.text())
        MZ = float(self.ui.lineEdit6.text())

        QTCP = W_R * mat([[MX], [MY], [MZ], [1]]) + W_t
        TEXT += "\nRTcp:{}".format(around(QTCP[:3], 4).T.tolist())

        self.Calculated_TCP = around(tT[:3], 4).T.tolist()
        self.Calculated_RTCP = around(QTCP[:3], 4).T.tolist()
        self.Calculated_Error = around(Error[:, :3], 4)
        self.Orientation_Matrix = W_R[:3, :3].tolist()
        self.Calculated_Base = around(W_t[:3], 4).T.tolist()
        self.Calculated_Frame = around(F_t[:3], 4).T.tolist()

        if Robot == "ABB":
            # ABB 旋转矩阵到四元数;
            Q4 = Rotation.from_matrix(W_R[:3, :3]).as_quat()
            self.Orientation_Base = around(Q4, 5).tolist()
            TEXT += "\nWobj:{}".format(around(W_t[:3], 4).T.tolist()) + " q:" + "[[{},{},{},{}]]".format(
                round(Q4[3], 8), round(Q4[0], 8), round(Q4[1], 8), round(Q4[2], 8))
        elif Robot == "KUKA":
            # KUKA 旋转矩阵到欧拉角
            ZYX = Rotation.from_matrix(W_R[:3, :3]).as_euler('ZYX', degrees=True)
            self.Orientation_Base = around(ZYX, 5).tolist()
            TEXT += "\nBase:{}".format(around(W_t[:3], 4).T.tolist()) + " ABC:[[{},{},{}]]".format(round(ZYX[0], 5),
                                                                                                   round(ZYX[1], 5),
                                                                                                   round(ZYX[2], 5))
        elif Robot == "FANUC" or "YASKAWA":
            # FANUC 旋转矩阵到欧拉角
            xyz = Rotation.from_matrix(W_R[:3, :3]).as_euler('xyz', degrees=True)
            self.Orientation_Base = around(xyz, 5).tolist()
            TEXT += "\nBase:{}".format(around(W_t[:3], 4).T.tolist()) + " rX rY rZ:[[{},{},{}]]".format(
                round(xyz[0], 5), round(xyz[1], 5), round(xyz[2], 5))

        F_R = Rotation.from_matrix(F_R[:3, :3]).as_euler('XYZ', degrees=True)
        self.Orientation_Frame = around(F_R, 5).tolist()
        TEXT += "\nFrame:{}".format(around(F_t[:3], 4).T.tolist()) + " XYZ:[[{},{},{}]]".format(round(F_R[0], 5),
                                                                                                round(F_R[1], 5),
                                                                                                round(F_R[2], 5))

        TEXT += "\nRmse:{}mm".format(around(self.Calculated_Rmse, 10))

        self.window_3d = Window_3D()
        self.window_3d.plot(Pa, Pb, Pbb)
        self.window_3d.show()
        self.fig = self.window_3d.canvas

        return TEXT

    def deta_txt(self, Robot, A, B, text):
        self.content = "************************ Robot calibration off-line: " + Robot + " ************************" + "\n"
        self.content += "Calculation started: " + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())) + "\n\n"
        self.content += 'Robot input:' + '\n\n' + A + '\n\n'
        self.content += 'Calibration input:' + '\n\n' + B + '\n\n'
        self.content += "Remaining Cell Alignment error (X-err,Y-err,Z-err):" + '\n\n' + format(
            self.Calculated_Error) + '\n\n'
        self.content += text + '\n'

        with open('Data.txt', 'a') as f:
            f.write(self.content)
            f.close()
        return True


class Window_3D(QDialog):

    def __init__(self, parent=None):
        super(Window_3D, self).__init__(parent)
        # a figure instance to plot on
        self.figure = plt.figure()
        self.figure.tight_layout()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setFixedSize(1000, 500)
        self.setWindowTitle("误差折线图——3D拟合图")  # 界面名称
        self.setWindowIcon(QIcon(u":/Image/\u56fe\u6807.png"))

    def plot(self, Pa, Pb, Pbb):
        self.figure.clear()
        # 折线图
        err = Pbb - Pb
        err_len = len(err)
        X = [i for i in range(1, err_len + 1)]
        ax = self.figure.add_subplot(121)
        ax.plot(X, err[:, 0], marker='.')
        ax.plot(X, err[:, 1], marker='.')
        ax.plot(X, err[:, 2], marker='.')

        abs_sum_list = [sum([abs(x) for x in row]) for row in err]  # 计算每行误差的绝对值之和
        if max(abs_sum_list) > 1:  # 如果最大值大于1
            max_index = abs_sum_list.index(max(abs_sum_list))  # 获取最大值的索引
            y_min = min(amin(err, axis=1))[0]  # 获取err中的最小值
            y_max = max(amax(err, axis=1))[0]  # 获取err中的最大值
            red_patch = mp.Rectangle((max_index + 0.8, y_min - 0.1), 0.4, y_max - y_min, fill=False, edgecolor='red',
                                     linewidth=2)  # 将红色矩形补丁添加到图中
            ax.add_patch(red_patch)  # 添加红色矩形补丁
            plt.text(max_index + 0.4, y_max, max_index + 1, c='r')

        # 3D图
        ax = self.figure.add_subplot(122, projection='3d')
        ax.scatter(Pa[:, 0], Pa[:, 1], Pa[:, 2], s=100, marker='.')
        ax.scatter(Pb[:, 0], Pb[:, 1], Pb[:, 2], s=100, marker='o')
        ax.scatter(Pbb[:, 0], Pbb[:, 1], Pbb[:, 2], s=100, marker='x')

        for X, Y, Z, n in zip(Pa[:, 0], Pa[:, 1], Pa[:, 2], range(1, len(Pa) + 1)):
            ax.text(X[0, 0], Y[0, 0], Z[0, 0], n)
        for X, Y, Z, n in zip(Pb[:, 0], Pb[:, 1], Pb[:, 2], range(1, len(Pa) + 1)):
            ax.text(X[0, 0], Y[0, 0], Z[0, 0], n)
        self.canvas.draw()


class WorkHelp(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Help()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)
        # 读写文件要加判断
        help_string = open('help.txt', 'r', encoding="utf-8").read()
        #
        self.ui.textEdit.setText(help_string)

    # 重写鼠标事件
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drag = False


class WorkReport(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Report()
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗体标题栏隐藏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 背景透明
        self.ui.setupUi(self)
        self.ui.pushButton_save.clicked.connect(self.Report_all)

        self.today = None
        self.Robot_Name = None
        self.buttonGroup_name = None
        self.path_save = None
        self.content = None
        self.fig = None  # PDF 折线图

        self.Robot_input = None
        self.Calibration_input = None

        self.Calculated_TCP = None
        self.Calculated_RTCP = None
        self.Calculated_Error = None
        self.Calculated_Rmse = None
        self.Orientation_Matrix = None
        self.Calculated_Base = None
        self.Orientation_Base = None
        self.Calculated_Frame = None
        self.Orientation_Frame = None

    # 重写鼠标事件
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton:
            self.drag = False

    def Report_all(self):
        # 定义生成日期
        self.today = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        self.Robot_Name = self.ui.lineEdit1.text()
        self.path_save = self.ui.lineEdit2.text() + '/Robot calibration report/Robot calibration off-line ' + self.ui.lineEdit1.text()
        path_save = os.path.exists(self.ui.lineEdit2.text() + '/Robot calibration report')
        if path_save == False:
            os.mkdir(self.ui.lineEdit2.text() + '/Robot calibration report')

        self.Report_txt()
        self.Report_excel()
        self.Report_PDF()
        self.WindowQMessageBox()
        self.ui

    def Report_txt(self):

        with open(self.path_save + '.txt', 'w') as f:
            f.write(self.content)
            f.close()
        return True

    def Report_excel(self):
        # 创建工作簿
        wb = Workbook()
        # 创建第一个表格
        ws1 = wb.active  # 默认表格
        ws1.title = self.buttonGroup_name  # 修改表格名称

        # 添加logo
        logo = excel_Image('./plugins/logo.png')
        ws1.add_image(logo, 'A1')

        # 写入数据
        data_ABB = [
            ['', '', '', '', '', 'Name:', self.Robot_Name, ''],
            ['', '', '', '', '', 'Data:', self.today, ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'q1', 'q2', 'q3', 'q4'],
            ['测量:TCP', '=Data!A2', '=Data!B2', '=Data!C2', '', '', '', ''],
            ['理论:TCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'q1', 'q2', 'q3', 'q4'],
            ['测量:RTCP', '=Data!A5', '=Data!B5', '=Data!C5', '', '', '', ''],
            ['理论:RTCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'q1', 'q2', 'q3', 'q4'],
            ['测量:Base', '=Data!A8', '=Data!B8', '=Data!C8', '=Data!A9', '=Data!B9', '=Data!C9', '=Data!D9'],
            ['理论:Base', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:Frame', '=Data!A12', '=Data!B12', '=Data!C12', '=Data!A12', '=Data!B12', '=Data!C12', ''],
            ['理论:Frame', '', '', '', '', '', '', ''],
        ]
        data_KUKA = [
            ['', '', '', '', '', 'Name:', self.Robot_Name, ''],
            ['', '', '', '', '', 'Data:', self.today, ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:TCP', '=Data!A2', '=Data!B2', '=Data!C2', '', '', '', ''],
            ['理论:TCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:RTCP', '=Data!A5', '=Data!B5', '=Data!C5', '', '', '', ''],
            ['理论:RTCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:Base', '=Data!A8', '=Data!B8', '=Data!C8', '=Data!A9', '=Data!B9', '=Data!C9', ''],
            ['理论:Base', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:Frame', '=Data!A12', '=Data!B12', '=Data!C12', '=Data!A12', '=Data!B12', '=Data!C12', ''],
            ['理论:Frame', '', '', '', '', '', '', ''],
        ]
        data_FANUC = [
            ['', '', '', '', '', 'Name:', self.Robot_Name, ''],
            ['', '', '', '', '', 'Data:', self.today, ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:TCP', '=Data!A2', '=Data!B2', '=Data!C2', '', '', '', ''],
            ['理论:TCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:RTCP', '=Data!A5', '=Data!B5', '=Data!C5', '', '', '', ''],
            ['理论:RTCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:Base', '=Data!A8', '=Data!B8', '=Data!C8', '=Data!A9', '=Data!B9', '=Data!C9', ''],
            ['理论:Base', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:Frame', '=Data!A12', '=Data!B12', '=Data!C12', '=Data!A12', '=Data!B12', '=Data!C12', ''],
            ['理论:Frame', '', '', '', '', '', '', ''],
        ]
        data_YASKAWA = [
            ['', '', '', '', '', 'Name:', self.Robot_Name, ''],
            ['', '', '', '', '', 'Data:', self.today, ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:TCP', '=Data!A2', '=Data!B2', '=Data!C2', '', '', '', ''],
            ['理论:TCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:RTCP', '=Data!A5', '=Data!B5', '=Data!C5', '', '', '', ''],
            ['理论:RTCP', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'A', 'B', 'C', ''],
            ['测量:Base', '=Data!A8', '=Data!B8', '=Data!C8', '=Data!A9', '=Data!B9', '=Data!C9', ''],
            ['理论:Base', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', 'X', 'Y', 'Z', 'rX', 'rY', 'rZ', ''],
            ['测量:Frame', '=Data!A12', '=Data!B12', '=Data!C12', '=Data!A12', '=Data!B12', '=Data!C12', ''],
            ['理论:Frame', '', '', '', '', '', '', ''],
        ]

        if self.buttonGroup_name == "ABB":
            data = data_ABB
        elif self.buttonGroup_name == "KUKA":
            data = data_KUKA
        elif self.buttonGroup_name == "FANUC":
            data = data_FANUC
        elif self.buttonGroup_name == "YASKAWA":
            data = data_YASKAWA

        for row in data:
            ws1.append(row)

        # ws1.protection.sheet = True
        # ws1.protection.password = '123'

        # 创建第二个表格
        ws2 = wb.create_sheet(title='Data')  # 指定表格名称
        # 写入数据

        ws2.append(['Calculated TCP:'])
        data2 = self.Calculated_TCP
        for row in data2:
            ws2.append(row)
        ws2.append([''])
        ws2.append(['Calculated RTCP:'])
        data2 = self.Calculated_RTCP
        for row in data2:
            ws2.append(row)
        ws2.append([''])

        ws2.append(['Base:'])
        data2 = self.Calculated_Base
        for row in data2:
            ws2.append(row)
        ws2.append(self.Orientation_Base)
        ws2.append([''])

        ws2.append(['From:'])
        data2 = self.Calculated_Frame
        for row in data2:
            ws2.append(row)
        ws2.append(self.Orientation_Frame)
        ws2.append([''])

        ws2.append(['Orientation Matrix:'])
        data2 = self.Orientation_Matrix
        for row in data2:
            ws2.append(row)
        ws2.append([''])
        ws2.append(['Robot input:'])
        data2 = self.Robot_input
        for row in data2:
            ws2.append(row)
        ws2.append([''])
        ws2.append(['Calibration input:'])
        data2 = self.Calibration_input
        for row in data2:
            ws2.append(row)
        ws2.append([''])
        ws2.append(['Remaining Cell Alignment error (X-err,Y-err,Z-err):'])
        data2 = self.Calculated_Error.tolist()
        for row in data2:
            ws2.append(row)

        # 保存工作簿
        wb.save(self.path_save + '.xlsx')

    def Report_PDF(self):
        self.fig.print_figure(self.path_save + '.png')
        # 创建 PDF 文件
        pdf_canvas = canvas.Canvas(self.path_save + '.pdf')

        # 添加logo
        logo = ImageReader('./plugins/logo.png')
        pdf_canvas.drawImage(logo, 30, 800, width=200, height=20)
        # 添加标题
        pdf_canvas.setFont('Helvetica-Bold', 24)
        pdf_canvas.drawCentredString(4.25 * inch, 10.2 * inch, 'Robot calibration off-line Report')

        pdf_canvas.setFontSize(18)
        pdf_canvas.drawString(0.8 * inch, 9.5 * inch, 'Measerement report:')
        pdf_canvas.setFontSize(12)
        pdf_canvas.drawString(0.8 * inch, 9 * inch, 'Project information:')

        pdf_canvas.setFontSize(12)
        pdf_canvas.drawString(1.5 * inch, 8.6 * inch, 'Robot: ' + self.buttonGroup_name)
        pdf_canvas.drawString(1.5 * inch, 8.4 * inch, 'Name: ' + self.Robot_Name)
        pdf_canvas.drawString(1.5 * inch, 8.2 * inch, 'Rmse: ' + self.Calculated_Rmse + ' mm ')

        pdf_canvas.setFontSize(12)
        pdf_canvas.drawString(0.8 * inch, 7.5 * inch, 'Deviation per Position:')
        img = Image.open(self.path_save + '.png')
        img_width, img_height = img.size
        pdf_canvas.drawImage(self.path_save + '.png', x=0.8 * inch, y=4 * inch, width=img_width * 0.5,
                             height=0.5 * img_height)

        pdf_canvas.setFontSize(10)
        pdf_canvas.drawString(1.5 * inch, 3.6 * inch, 'TCP: ' + format(self.Calculated_TCP))
        pdf_canvas.drawString(1.5 * inch, 3.4 * inch, 'RTCP: ' + format(self.Calculated_RTCP))
        pdf_canvas.drawString(1.5 * inch, 3.2 * inch, 'Base: ' + format(self.Calculated_Base + [self.Orientation_Base]))
        pdf_canvas.drawString(1.5 * inch, 3.0 * inch,
                              'From: ' + format(self.Calculated_Frame + [self.Orientation_Frame]))

        # 底部信息
        # 加载作者logo图像
        Author_logo = ImageReader('./plugins/图标.png')
        # 在PDF文档中添加作者logo
        pdf_canvas.drawImage(Author_logo, x=5.8 * inch, y=0.55 * inch, width=0.5 * inch, height=0.5 * inch, mask='auto')
        # 定义作者
        author = "GW00261571"
        # 定义联系方式
        contact_info = "w13555929918@qq.com"
        # 在PDF文档中添加这些信息
        pdf_canvas.setFontSize(5.5)
        pdf_canvas.drawString(6.5 * inch, 0.9 * inch, "Apply: Robot calibration off-line ")
        pdf_canvas.drawString(6.5 * inch, 0.8 * inch, "Generated on: " + self.today)
        pdf_canvas.drawString(6.5 * inch, 0.7 * inch, "Author: " + author)
        pdf_canvas.drawString(6.5 * inch, 0.6 * inch, "Contact: " + contact_info)
        # 关闭 PDF 文件
        pdf_canvas.save()

    def WindowQMessageBox(self):
        self.windowqmessagebox = WindowQMessageBox()
        self.windowqmessagebox.ui.label.setText("报告生成成功!")
        self.windowqmessagebox.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MianWindow = Window()
    sys.exit(app.exec())
