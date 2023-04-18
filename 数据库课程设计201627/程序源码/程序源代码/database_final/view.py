# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys

import service

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbUser = QtWidgets.QTableWidget(self.centralwidget)
        self.tbUser.setGeometry(QtCore.QRect(30, 30, 581, 421))
        self.tbUser.setObjectName("tbUser")
        self.tbUser.setColumnCount(5)
        self.tbUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(4, item)

        self.btnConsume = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsume.setGeometry(QtCore.QRect(110, 470, 141, 31))
        self.btnConsume.setObjectName("btnConsume")

        self.btnRecharge = QtWidgets.QPushButton(self.centralwidget)
        self.btnRecharge.setGeometry(QtCore.QRect(370, 470, 131, 31))
        self.btnRecharge.setObjectName("btnRecharge")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tbUser.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbUser.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.btnConsume.clicked.connect(self.consume)  # 绑定消费统计按钮的单击信号
        self.btnRecharge.clicked.connect(self.recharge)  # 绑定充值统计按钮的单击信号

    def consume(self):
        self.tbUser.setRowCount(0)  # 清空表格中的所有行
        result = service.query("select * from consum_sum")  # 调用服务类中方的公共法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbUser.setRowCount(row)  # 设置表格行数
        self.tbUser.setColumnCount(5)  # 设置表格列数
        self.tbUser.setHorizontalHeaderLabels(['校园卡号','学号', '姓名', '班级', '消费总额' ]) # 设置表格的标题名称
        for i in range(row):  # 遍历行
            for j in range(self.tbUser.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbUser.setItem(i, j, data)  # 设置每个单元格1的数据
    def recharge(self):
        self.tbUser.setRowCount(0)  # 清空表格中的所有行
        result = service.query("select * from charge_sum")  # 调用服务类中方的公共法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbUser.setRowCount(row)  # 设置表格行数
        self.tbUser.setColumnCount(5)  # 设置表格列数
        self.tbUser.setHorizontalHeaderLabels(['校园卡号','学号', '姓名', '班级', '充值总额' ])# 设置表格的标题名称
        for i in range(row):  # 遍历行
            for j in range(self.tbUser.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbUser.setItem(i, j, data)  # 设置每个单元格1的数据
                
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "统计"))
        item = self.tbUser.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "校园卡号"))
        item = self.tbUser.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tbUser.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tbUser.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tbUser.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "消费总额"))
        self.btnConsume.setText(_translate("MainWindow", "消费统计"))
        self.btnRecharge.setText(_translate("MainWindow", "充值统计"))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # 创建一个QWidget子类
#     w = Ui_MainWindow()
#     w.show()

#     app.exec()
