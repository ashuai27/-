# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget
import sys  # 导入sys模块
import main
import service

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.name_element(self)
    def setupUi(self, MainWindow):
         

        # 设置窗口大小
        MainWindow.resize(360, 200)

        # 测试过删除传入的MainWindow没有影响
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        # 这一串没明白意思
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # 没有采用 self.label_2.setGeometry(QtCore.QRect(120, 100, 60, 20))形式
        # self.label.setGeometry(10, 0, 360, 80)

        # 设置背景图
        # self.centralwidget.setStyleSheet("background-image:url(images/login.jpg)")

        # 创建文本一和二
        # self.label.setText("")
        # self.label.setObjectName("label")

        #创建文本标签用来展示文字
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        #设置文本的位置
        self.label_2.setGeometry(70, 50, 60, 20)
        #声明字体对象用来设置字体的字号颜色等
        font = QtGui.QFont()
        #设置字体字号
        font.setPointSize(12)
        #利用qlabel对象，的setfont方法将传入的font参数应用到名字为label_2的label对象
        self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")

        # 创建文本三
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(70, 80, 60, 20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        # self.label_3.setObjectName("label_3")

        # 输入框
        self.editName = QtWidgets.QLineEdit(self.centralwidget)
        self.editName.setGeometry(145, 50, 140, 20)
        # self.editName.setObjectName("editName")

        # 输入框二
        self.editPwd = QtWidgets.QLineEdit(self.centralwidget)
        self.editPwd.setGeometry(145, 80, 140, 20)
        # 设置输入文本的回显模式
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.editPwd.setObjectName("editPwd")

        

        #创建按钮登录和退出按钮
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(150, 110, 60, 25)
        # self.btnLogin.setObjectName("btnLogin")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(220, 110, 60, 25)
        # self.btnExit.setObjectName("btnExit")

        #销毁原来MainWindow的中心窗口，用新设置好的centralwidget窗口以及其自带的部件进行替换
        MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow = self.centralwidget 不好使

        #调用我建立的组件命名方法对组件进行命名
        self.name_element(MainWindow)

        #利用信号（点击btnExit（退出按钮））驱动槽函数（关闭窗口）
        self.btnExit.clicked.connect(MainWindow.close) # 关闭登录窗体

        # 没懂意思：手动连接信号与槽
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 输入密码后按回车键执行登录操作容易产生当你移动鼠标时点击用户名框时误登录
        # self.editPwd.editingFinished.connect(self.openMain)
        
        # 单击“登录”按钮执行登录操作
        self.btnLogin.clicked.connect(self.openMain)

    # 打开主窗体
    def openMain(self):
        
        service.userName=self.editName.text() # 全局变量，记录用户名
        self.userPwd=self.editPwd.text() # 记录用户密码

        if service.userName != "" and self.userPwd != "": # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result=service.query("select * from manager where account_ = %s and password_ = %s",service.userName,self.userPwd)
            if len(result): # 如果查询结果不为空，说明存在该用户，可以登录
                MainWindow.hide() # 隐藏当前的登录窗体
                self.m = main.Ui_MainWindow()  # 创建主窗体对象
                self.m.show()  # 显示主窗体
                
            else:
                self.editName.setText("") # 清空用户名文本
                self.editPwd.setText("") # 清空密码文本框
                QMessageBox.warning(None, '警告', '请输入正确的用户名和密码！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入用户名和密码！', QMessageBox.Ok)

    def name_element(self, MainWindow):
        """设置组件的名称"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("系统登录")
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密  码："))
        self.btnLogin.setText(_translate("MainWindow", "登录"))
        self.btnExit.setText(_translate("MainWindow", "退出"))
# 主方法
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象后续利用窗体设计对象对传入的窗体对象进行设计
    ui = Ui_MainWindow() # 创建窗体设计对象

    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    # ui.show()
    sys.exit(app.exec_()) # 程序关闭时退出进程
