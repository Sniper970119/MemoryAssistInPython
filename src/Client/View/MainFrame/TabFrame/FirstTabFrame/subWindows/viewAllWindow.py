# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.MissionSystem import missionSystem
from src.Client.SystemTools.ConfFileRead import configFileRead


class ViewAllWindow():
    """
    显示全部任务的GUI界面
    """
    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.missionIdVar = tkinter.StringVar()
        self.missionNameVar = tkinter.StringVar()
        self.missionRangeVar = tkinter.StringVar()
        self.missionStateCodeVar = tkinter.StringVar()
        self.missionNextTimeCodeVar = tkinter.StringVar()
        self.missionLoopTimeCodeVar = tkinter.StringVar()
        self.missionisFinish = tkinter.StringVar()
        self.language()
        self.missionSystemTools = missionSystem.MissionSystem()

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('查看全部')
            self.missionIdVar.set('任务id')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.missionStateCodeVar.set('任务进度')
            self.missionNextTimeCodeVar.set('下次任务')
            self.missionLoopTimeCodeVar.set('循环次数')
            self.missionisFinish.set('是否完成')
        elif languageType == 'EN':
            self.windowTitleVar.set('view all')
            self.missionIdVar.set('mission id')
            self.missionNameVar.set('mission name')
            self.missionRangeVar.set('mission range')
            self.missionStateCodeVar.set('state')
            self.missionNextTimeCodeVar.set('next time')
            self.missionLoopTimeCodeVar.set('loop time')
            self.missionisFinish.set('isFinish')
        else:
            self.windowTitleVar.set('查看全部')
            self.missionIdVar.set('任务id')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.missionStateCodeVar.set('任务进度')
            self.missionNextTimeCodeVar.set('下次任务')
            self.missionLoopTimeCodeVar.set('循环次数')
            self.missionisFinish.set('是否完成')

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '550x320+' + str(int((screenWidth - 550) / 2)) + '+' + str(int((screenHeight - 320) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title(self.windowTitleVar.get())
        self.addWindow.iconbitmap('images/icon.ico')
        self.tree = ttk.Treeview(self.addWindow, columns=['1', '2', '3', '4', '5', '6', '7'], show='headings',
                                 height=15)

        self.tree.column('1', width=80, anchor='center')
        self.tree.column('2', width=80, anchor='center')
        self.tree.column('3', width=80, anchor='center')
        self.tree.column('4', width=80, anchor='center')
        self.tree.column('5', width=80, anchor='center')
        self.tree.column('6', width=80, anchor='center')
        self.tree.column('7', width=80, anchor='center')
        self.tree.heading('1', text=self.missionIdVar.get())
        self.tree.heading('2', text=self.missionNameVar.get())
        self.tree.heading('3', text=self.missionRangeVar.get())
        self.tree.heading('4', text=self.missionStateCodeVar.get())
        self.tree.heading('5', text=self.missionNextTimeCodeVar.get())
        self.tree.heading('6', text=self.missionLoopTimeCodeVar.get())
        self.tree.heading('7', text=self.missionisFinish.get())
        self.tree.place(x=0, y=0, anchor='nw')
        list = missionSystem.MissionSystem().loadMission()
        for each in list:
            dataInList = [each['missionId'], each['bookName'], each['missionRange'], each['state'], each['nextTime'],
                          each['loopTime'], each['isFinish']]
            self.tree.insert('', 'end', values=dataInList)
