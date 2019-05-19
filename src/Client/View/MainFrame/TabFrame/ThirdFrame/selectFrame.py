# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.ThirdFrame.subWindows import addWindow, editWindow, viewAllWindow


class SelectFrame():
    """
    右侧选择GUI。同时对应右侧按钮进行调用。
    """
    def __init__(self, thirdTabFrame):
        """

        :param thirdTabFrame: 当前Frame的父容器
        """
        self.addMissionButtonVar = tkinter.StringVar()
        self.editMissionButtonVar = tkinter.StringVar()
        self.viewAllButtonVar = tkinter.StringVar()
        self.language()
        if DEBUG and VIEW_DEBUG:
            self.menuFrame = tkinter.Frame(thirdTabFrame, height=350, width=150, bg='pink')
        else:
            self.menuFrame = tkinter.Frame(thirdTabFrame, height=350, width=150)

        self.menuFrame.place(x=550, y=00, anchor='nw')

        #
        self.printSelect()


    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.addMissionButtonVar.set('添加背诵')
            self.editMissionButtonVar.set('编辑背诵')
            self.viewAllButtonVar.set('查看全部')
        elif languageType == 'EN':
            self.addMissionButtonVar.set('add question')
            self.editMissionButtonVar.set('edit question')
            self.viewAllButtonVar.set('view all')
        else:
            self.addMissionButtonVar.set('添加背诵')
            self.editMissionButtonVar.set('编辑背诵')
            self.viewAllButtonVar.set('查看全部')

    def selectAddButton(self):
        """
        选择添加按钮后的操作
        :return:
        """
        win = addWindow.AddWindow().window()
        # 调用用户操作记录函数，记录用户此次操作
        self.logUserAction('add recitation button has been pressed')
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
        self.logUserAction('edit recitation button has been pressed')
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
        self.logUserAction('view recitation button has been pressed')
        if DEBUG and VIEW_DEBUG:
            print('{USR}{SELECT_FRAME} view all button has been pressed')
        pass

    def printSelect(self):
        """
        绘制组件
        :return:
        """
        # 添加添加按钮
        addButton = tkinter.Button(self.menuFrame, text=self.addMissionButtonVar.get(), width=12, height=1, command=self.selectAddButton)
        addButton.place(x=35, y=60, anchor='nw')
        # 添加编辑按钮
        editButton = tkinter.Button(self.menuFrame, text=self.editMissionButtonVar.get(), width=12, height=1, command=self.selectEditButton)
        editButton.place(x=35, y=140, anchor='nw')
        # 添加查看按钮
        viewAllButton = tkinter.Button(self.menuFrame, text=self.viewAllButtonVar.get(), width=12, height=1, command=self.selectAllButton)
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
