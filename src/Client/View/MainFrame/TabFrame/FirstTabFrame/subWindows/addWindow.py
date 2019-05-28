# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.MissionSystem import missionSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import messageFrame


class AddWindow():
    """
    添加任务的GUI界面。负责显示添加任务的GUI以及非法输入拦截。
    """
    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.missionNameVar = tkinter.StringVar()
        self.missionRangeVar = tkinter.StringVar()
        self.addButtonVar = tkinter.StringVar()
        self.errorTitleVar = tkinter.StringVar()
        self.errorMessageVar = tkinter.StringVar()
        self.language()
        self.missionSystemTools = missionSystem.MissionSystem()
        self.addWindow = None

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('添加任务')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.addButtonVar.set('确认添加')
            self.errorTitleVar.set('添加错误')
            self.errorMessageVar.set('任务名和任务范围不可为空')
        elif languageType == 'EN':
            self.windowTitleVar.set('add mission')
            self.missionNameVar.set('mission name')
            self.missionRangeVar.set('mission range')
            self.addButtonVar.set('add')
            self.errorTitleVar.set('add error')
            self.errorMessageVar.set("mission name and mission range can't be null")
        else:
            self.windowTitleVar.set('添加任务')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.addButtonVar.set('确认添加')
            self.errorTitleVar.set('添加错误')
            self.errorMessageVar.set('任务名和任务范围不可为空')

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '300x230+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 230) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title(self.windowTitleVar.get())
        self.addWindow.iconbitmap('images/icon.ico')

        nameLabel = tkinter.Label(self.addWindow, text=self.missionNameVar.get(), font=('Arial', 12), width=15, height=2)
        nameLabel.place(x=-20, y=50, anchor='nw')

        nameEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        nameEntry.place(x=100, y=55, anchor='nw')

        missionRangeLabel = tkinter.Label(self.addWindow, text=self.missionRangeVar.get(), font=('Arial', 12), width=15, height=2)
        missionRangeLabel.place(x=-20, y=100, anchor='nw')

        missionRangeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        missionRangeEntry.place(x=100, y=105, anchor='nw')

        def addMission():
            """
            确认添加按钮的事件
            :return:
            """
            # 获取两个任务信息
            bookName = nameEntry.get()
            missionRange = missionRangeEntry.get()
            # 检查输入非空，若为空向用户反馈更改
            if bookName is '' or missionRange is '':
                messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessageVar.get())
                return
            # 调用添加任务工具
            self.missionSystemTools.addMission(bookName=bookName, missionRange=missionRange)
            # 关闭窗口
            self.addWindow.after(300, self.addWindow.destroy)
            # 将messageFrame的重绘变量置为True
            messageFrame.MessageFrame.needReprint = True
            if DEBUG and VIEW_DEBUG:
                print('{USR}{MESSAGE_FRAME} now user click add mission button and system save it')
            pass
        # 按钮
        addButton = tkinter.Button(self.addWindow, text=self.addButtonVar.get(), command=addMission, width=8)
        addButton.place(x=200, y=155, anchor='nw')

