# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import service
import charge, consume
import bankcard
import campuscard, view
import user
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        # self.retranslateUi(self)

    def setupUi(self, MainWindow):
        # MainWindow.setObjectName("MainWindow")

        # 设置窗口大小
        MainWindow.resize(792, 583)

        # 设置图标删除并没有影响
        # icon = QtGui.QIcon()
        # MainWindow.setWindowIcon(icon)
        # MainWindow.setIconSize(QtCore.QSize(32, 32))

        # self是qmainwindow对象，而centralwidget是qwidget对象
        self.centralwidget = QtWidgets.QWidget()
        # self.centralwidget.setStyleSheet("background-image:url(images/main.jpg)")
        # self.centralwidget.setObjectName("centralwidget")

        #可以不必要进行替换操作
        MainWindow.setCentralWidget(self.centralwidget)

        #创建菜单栏
        self.menubar0 = self.menuBar()
        self.menubar0.setGeometry(0, 0, 792, 23)
        # self.menubar.setObjectName("menubar")
        #创建菜单4个
        self.menu = self.menubar0.addMenu("校园卡")
        # self.menu.setObjectName("menu")
        self.menu_2 = self.menubar0.addMenu("银行卡")
        # self.menu_2.setObjectName("menu_2")
        self.menu_3 = self.menubar0.addMenu("流水查询")
        # self.menu_3.setObjectName("menu_3")
        self.menu_4 = self.menubar0.addMenu("系统管理")
        # self.menu_4.setObjectName("menu_4")

        #注释掉后，之前的位置设置就好使了
        # MainWindow.setMenuBar(self.menubar)
        
        #创建状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.actioncampuscard = QtWidgets.QAction(MainWindow)
        # # self.actioncampuscard.setObjectName("actioncampuscard")
        # self.actionsubject = QtWidgets.QAction(MainWindow)
        # # self.actionsubject.setObjectName("actionsubject")
        # self.actionresult = QtWidgets.QAction(MainWindow)
        # # self.actionresult.setObjectName("actionresult")
        # self.actionstudentinfo = QtWidgets.QAction(MainWindow)
        # # self.actionstudentinfo.setObjectName("actionstudentinfo")
        # self.actionresultinfo = QtWidgets.QAction(MainWindow)
        # # self.actionresultinfo.setObjectName("actionresultinfo")
        # self.actionuserinfo = QtWidgets.QAction(MainWindow)
        # # self.actionuserinfo.setObjectName("actionuserinfo")
        # self.actionexit = QtWidgets.QAction(MainWindow)
        # # self.actionexit.setObjectName("actionexit")

        self.menu.addAction('校园卡管理')
        self.menu.addAction('统计')
        self.menu_2.addAction("银行卡管理")
        self.menu_3.addAction("消费记录管理")
        self.menu_3.addAction("充值记录管理")
        self.menu_4.addAction("用户维护")
        self.actionexit = self.menu_4.addAction("退出")
        #  = self.menubar.addAction(self.menu.menuAction())
        #  = self.menubar.addAction(self.menu_2.menuAction())
        #  = self.menubar.addAction(self.menu_3.menuAction())
        #  = self.menubar.addAction(self.menu_4.menuAction())

        # 调用组件命名方法
        self.retranslateUi(MainWindow)

        self.actionexit.triggered.connect(MainWindow.close)

        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        datetime = QtCore.QDateTime.currentDateTime()  # 获取当前日期时间
        time = datetime.toString("yyyy-MM-dd HH:mm:ss")  # 对日期时间进行格式化
        # 状态栏中显示登录用户、登录时间
        self.statusbar.showMessage("当前登录用户：" + service.userName + " | 登录时间：" + time ,0)

        
        # 为基础设置菜单中的QAction绑定triggered信号
        self.menu.triggered.connect(self.openSet)
        # 为基本信息管理菜单中的QAction绑定triggered信号
        self.menu_2.triggered.connect(self.openBase)
        # 为系统查询菜单中的QAction绑定triggered信号
        self.menu_3.triggered.connect(self.openQuery)
        # 为系统管理菜单中的QAction绑定triggered信号
        self.menu_4.triggered.connect(self.openSys)

    # 基础设置菜单对应槽函数
    def openSet(self,m):
        if m.text()=="校园卡管理":
            self.m = campuscard.Ui_MainWindow()  # 创建校园卡管理窗体对象
            self.m.show()  # 显示窗体
        elif m.text() == "统计":
            self.m = view.Ui_MainWindow()  # 创建统计窗体对象
            self.m.show()  # 显示窗体

    # 基本信息管理菜单对应槽函数
    def openBase(self,m):
        if  m.text()=="银行卡管理":
            self.m = bankcard.Ui_MainWindow()  # 创建银行卡管理窗体对象
            self.m.show()  # 显示窗体

    # 系统查询菜单对应槽函数
    def openQuery(self,m):
        if  m.text()=="消费记录管理":
            self.m = consume.Ui_MainWindow()  # 创建消费记录管理窗体对象
            self.m.show()  # 显示窗体
        elif  m.text()=="充值记录管理":
            self.m = charge.Ui_MainWindow()  # 创建充值记录窗体对象
            self.m.show()  # 显示窗体

    # 系统管理菜单对应槽函数
    def openSys(self,m):
        if  m.text()=="用户维护":
            self.m = user.Ui_MainWindow()  # 创建用户维护窗体对象
            self.m.show()  # 显示窗体

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "校园一卡通管理系统"))
        
