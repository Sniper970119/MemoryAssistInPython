# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.View.MainFrame.TabFrame.FirstTabFrame.subWindows import addWindow
from src.View.MainFrame.TabFrame.FirstTabFrame.subWindows import editWindow
from src.View.MainFrame.TabFrame.FirstTabFrame.subWindows import viewAllWindow


class SelectFrame():

    def __init__(self, firstTabFrame):
        """

        :param firstTabFrame: 当前Frame的父容器
        """
        if DEBUG and VIEW_DEBUG:
            self.menuFrame = tkinter.Frame(firstTabFrame, height=350, width=150, bg='pink')
        else:
            self.menuFrame = tkinter.Frame(firstTabFrame, height=350, width=150)

        self.menuFrame.place(x=550, y=00, anchor='nw')

        #
        self.printSelect()

    def selectAddButton(self):
        """
        选择添加按钮后的操作
        :return:
        """
        win = addWindow.AddWindow().window()
        # 调用用户操作记录函数，记录用户此次操作
        self.logUserAction('add button has been pressed')
        if DEBUG and VIEW_DEBUG:
            print('{USR}{SELECT_FRAME} add button has been pressed')
        pass

    def selectEditButton(self):
        """
        选择编辑按钮后的操作
        :return:
        """
        win = editWindow.EditWindow().window()
        # 调用用户操作记录函数，记录用户此次操作
        self.logUserAction('edit button has been pressed')
        if DEBUG and VIEW_DEBUG:
            print('{USR}{SELECT_FRAME} edit button has been pressed')
        pass

    def selectAllButton(self):
        """
        选择查看全部后的操作
        :return:
        """
        win = viewAllWindow.ViewAllWindow().window()
        # 调用用户操作记录函数，记录用户此次操作
        self.logUserAction('view button has been pressed')
        if DEBUG and VIEW_DEBUG:
            print('{USR}{SELECT_FRAME} view all button has been pressed')
        pass

    def printSelect(self):
        """
        绘制组件
        :return:
        """
        # 添加添加按钮
        addButton = tkinter.Button(self.menuFrame, text='添加任务', width=10, height=1, command=self.selectAddButton)
        addButton.place(x=35, y=60, anchor='nw')
        # 添加编辑按钮
        editButton = tkinter.Button(self.menuFrame, text='编辑任务', width=10, height=1, command=self.selectEditButton)
        editButton.place(x=35, y=140, anchor='nw')
        # 添加查看按钮
        viewAllButton = tkinter.Button(self.menuFrame, text='查看全部', width=10, height=1, command=self.selectAllButton)
        viewAllButton.place(x=35, y=220, anchor='nw')
        pass

    def logUserAction(self, action, message=None):

        # 记录用户操作
        userActionLogFile = open('data/userAction.dat', 'a+')
        # 获取当前时间
        currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                     '%Y-%m-%d-%H-%M-%S'))
        # 生成记录信息
        if message is None:
            userAction = '{' + currentTime + '} ' + action + ' '
        else:
            userAction = '{' + currentTime + '} ' + action + ' ' + message

        # 存入文件
        userActionLogFile.write(str(userAction))
        # 增加换行符
        userActionLogFile.write('\n')
        userActionLogFile.close()
