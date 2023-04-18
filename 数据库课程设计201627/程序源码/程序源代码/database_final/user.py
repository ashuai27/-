# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


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
        # MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        self.tbUser = QtWidgets.QTableWidget(self.centralwidget)
        self.tbUser.setGeometry(QtCore.QRect(0, 0, 400, 200))
        # self.tbUser.setObjectName("tbUser")
        self.tbUser.setColumnCount(2)
        self.tbUser.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbUser.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        # self.label_3.setObjectName("label_3")
        self.editName = QtWidgets.QLineEdit("",self.centralwidget)
        self.editName.setGeometry(QtCore.QRect(100, 220, 80, 20))
        # self.editName.setObjectName("editID")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        self.editPwd = QtWidgets.QLineEdit("",self.centralwidget)
        self.editPwd.setGeometry(QtCore.QRect(300, 220, 80, 20))
        self.editPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.editPwd.setObjectName("editName")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(40, 260, 50, 30))
        # self.btnAdd.setObjectName("btnAdd")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(130, 260, 50, 30))
        # self.btnEdit.setObjectName("btnEdit")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(220, 260, 50, 30))
        # self.btnDel.setObjectName("btnDel")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(310, 260, 50, 30))
        # self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btnExit.clicked.connect(MainWindow.close) # 关闭窗口
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tbUser.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.tbUser.verticalHeader().setVisible(False)  # 隐藏垂直标题
        self.query() # 窗体加载时显示所有数据
        self.tbUser.itemClicked.connect(self.getItem) # 获取选中的单元格数据
        self.btnAdd.clicked.connect(self.add) # 绑定添加按钮的单击信号
        self.btnEdit.clicked.connect(self.edit) # 绑定修改按钮的单击信号
        self.btnDel.clicked.connect(self.delete) # 绑定删除按钮的单击信号

    # 查询用户信息，并显示在表格中
    def query(self):
        self.tbUser.setRowCount(0) # 清空表格中的所有行
        result = service.query("select * from manager") # 调用服务类中方的公共法执行查询语句
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tbUser.setRowCount(row)  # 设置表格行数
        self.tbUser.setColumnCount(2)  # 设置表格列数
        # 设置表格的标题名称
        self.tbUser.setHorizontalHeaderLabels(['用户名称', '用户密码'])
        for i in range(row):  # 遍历行
            for j in range(self.tbUser.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tbUser.setItem(i, j, data) # 设置每个单元格的数据

    # 获取选中的表格内容
    def getItem(self, item):
        # self.judge = 0 用来判断最后的选择是否是学号单元格用于edit函数进行修改数据
        row =  item.row()
        self.editPwd.setText(self.tbUser.item(row,1).text()) 
        self.editName.setText(self.tbUser.item(row,0).text()) 
        
        # self.editName_2.setText(self.tbStudent.item(row,4).text()) 
        # self.editBankcardID_2.setText(self.tbStudent.item(row,4).text()) 
        

    # 清空输入框
    def clear_input_table(self):
        self.editName.setText("")
        self.editPwd.setText("")

    # 添加用户信息
    def add(self):
        userName = self.editName.text() # 记录输入的用户名
        userPwd = self.editPwd.text() # 记录输入的用户密码
        if userName != "" and userPwd != "": # 判断用户名和密码不为空
            # 执行添加语句
            result=service.exec("insert into manager(account_,password_ ) values (%s,%s)",(userName,userPwd))
            if result>0:  # 如果结果大于0，说明添加成功
                self.query() # 在表格中显示最新数据
                QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
                self.clear_input_table()
            else:
                QMessageBox.warning(None, '警告', '信息添加失败，用户名重复！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入全部数据后，再执行相关操作！', QMessageBox.Ok)

    # 修改用户信息
    def edit(self):
        try:
            userName = self.editName.text() # 记录输入的用户名
            userPwd = self.editPwd.text() # 记录输入的用户密码
            print(userName,userPwd)
            if userName !="" : # 判断是否选择了要修改的数据
                if userPwd == "":
                    QMessageBox.warning(None, '警告', '密码不能为空！', QMessageBox.Ok)
                else:
                    userPwd = self.editPwd.text() # 记录修改的用户密码
                    if userPwd != "" and userName !="": # 判断密码不为空
                        # 执行修改操作
                        result=service.exec("update manager set  password_  = %s where account_=%s;",(userPwd, userName))
                        print(result)
                        if result>0: # 如果结果大于0，说明修改成功
                            self.query() # 在表格中显示最新数据
                            QMessageBox.information(None, '提示', '信息修改成功！', QMessageBox.Ok)
                            self.clear_input_table()
                        else:
                            QMessageBox.warning(None, '警告', '信息修改失败，请检查所有信息后重试！', QMessageBox.Ok)
            else:
                QMessageBox.warning(None, '警告', '请先选择要修改的账户！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '请先选择要修改的账户！', QMessageBox.Ok)

    # 删除用户信息
    def delete(self):
        try:
            userName = self.editName.text() # 记录输入的用户名
            userPwd = self.editPwd.text() # 记录输入的用户密码
            print(userName, userPwd)
            if userName !="" "": # 判断是否选择了要删除的数据
                # 执行删除操作
                exist = service.query("select * from manager where account_=  %s ;", (userName,))  # 调用服务类中方的公共法执行查询语句
                print("查找到",exist) 
                if len(exist) == 0:
                    QMessageBox.information(None, '警告', '该用户不存在，请检查信息后重试！', QMessageBox.Ok)
                else:

                    result=service.delete("delete from manager where account_ = %s;",(userName))
                    if result>0: # 如果结果大于0，说明删除成功
                        self.query() # 在表格中显示最新数据
                        QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
                        self.clear_input_table()
                    else:
                        QMessageBox.information(None, '警告', '信息删除失败，请检查用户信息后重试！', QMessageBox.Ok)
            else:
                QMessageBox.warning(None, '警告', '请先选择要删除的用户名！', QMessageBox.Ok)
        except:
            QMessageBox.warning(None, '警告', '删除失败！', QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户信息维护"))
        item = self.tbUser.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用户名"))
        item = self.tbUser.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "密码"))
        self.label_3.setText(_translate("MainWindow", "用户密码："))
        self.label_2.setText(_translate("MainWindow", "用户名称："))
        self.btnAdd.setText(_translate("MainWindow", "添加"))
        self.btnEdit.setText(_translate("MainWindow", "修改"))
        self.btnDel.setText(_translate("MainWindow", "删除"))
        self.btnExit.setText(_translate("MainWindow", "退出"))




# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     # 创建一个QWidget子类
#     w = Ui_MainWindow()
#     w.show()

#     app.exec()