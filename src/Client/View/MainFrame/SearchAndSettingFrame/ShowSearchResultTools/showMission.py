# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
import sys


class ShowMission():
    """
    搜索栏显示任务GUI部分。
    """

    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.missionIdVar = tkinter.StringVar()
        self.missionNameVar = tkinter.StringVar()
        self.missionRangeVar = tkinter.StringVar()
        self.missionNextTimeVar = tkinter.StringVar()
        self.missionStateVar = tkinter.StringVar()
        self.missionLoopTimeVar = tkinter.StringVar()
        self.missionStateVar = tkinter.StringVar()
        reload(sys)
        sys.setdefaultencoding("utf-8")
        self.language()

        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('任务详情')
            self.missionIdVar.set('任务id： ')
            self.missionNameVar.set('任务书名： ')
            self.missionRangeVar.set('任务范围： ')
            self.missionNextTimeVar.set('下次任务时间： ')
            self.missionStateVar.set('任务状态： ')
            self.missionLoopTimeVar.set('剩余迭代次数： ')
            self.missionStateVar.set('完成状态： ')
        elif languageType == 'EN':
            self.windowTitleVar.set('mission detail')
            self.missionIdVar.set('mission id： ')
            self.missionNameVar.set('mission name： ')
            self.missionRangeVar.set('mission range： ')
            self.missionNextTimeVar.set('next time： ')
            self.missionStateVar.set('mission state： ')
            self.missionLoopTimeVar.set('remain loop time： ')
            self.missionStateVar.set('mission state： ')
        else:
            self.windowTitleVar.set('任务详情')
            self.missionIdVar.set('任务id： ')
            self.missionNameVar.set('任务书名： ')
            self.missionRangeVar.set('任务范围： ')
            self.missionNextTimeVar.set('下次任务时间： ')
            self.missionStateVar.set('任务状态： ')
            self.missionLoopTimeVar.set('剩余迭代次数： ')
            self.missionStateVar.set('完成状态： ')



    def window(self, result):
        showWindow = tkinter.Toplevel()
        screenWidth = showWindow.winfo_screenwidth()
        screenHeight = showWindow.winfo_screenheight()
        showWindow.geometry(
            '300x250+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 250) / 2)))
        showWindow.resizable(width=False, height=False)
        showWindow.title(self.windowTitleVar.get())
        showWindow.iconbitmap('images/icon.ico')


        # 显示任务
        showMission = self.missionIdVar.get() + str(result['missionId'])
        missiondLabel = tkinter.Label(showWindow, text=showMission)
        missiondLabel.place(x=30, y=20, anchor='nw')

        # 显示书名
        showBookName = self.missionNameVar.get() + str(result['bookName'])
        bookNameLabel = tkinter.Label(showWindow, text=showBookName)
        bookNameLabel.place(x=30, y=50, anchor='nw')

        # 显示任务范围
        showMissionRange = self.missionRangeVar.get() + str(result['missionRange'])
        missionRangeLabel = tkinter.Label(showWindow, text=showMissionRange)
        missionRangeLabel.place(x=30, y=80, anchor='nw')

        # 显示下次任务时间
        showNextTime = self.missionNextTimeVar.get() + str(result['nextTime'])
        nextTimeLabel = tkinter.Label(showWindow, text=showNextTime)
        nextTimeLabel.place(x=30, y=110, anchor='nw')

        # 显示任务状态
        showMissionState = self.missionStateVar.get() + str(result['state'])
        stateMissionLabel = tkinter.Label(showWindow, text=showMissionState)
        stateMissionLabel.place(x=30, y=140, anchor='nw')

        # 显示剩余迭代次数
        showLoopTime = self.missionLoopTimeVar.get() + str(result['loopTime'])
        loopTimeLabel = tkinter.Label(showWindow, text=showLoopTime)
        loopTimeLabel.place(x=30, y=170, anchor='nw')

        # 显示完成状态
        showIsFinish = self.missionStateVar.get() + str(result['isFinish'])
        isFinishLabel = tkinter.Label(showWindow, text=showIsFinish)
        isFinishLabel.place(x=30, y=200, anchor='nw')
