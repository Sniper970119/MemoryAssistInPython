# -*- coding:utf-8 -*-
from src.Conf.config import *


class ShowMission():
    """
    搜索栏显示任务GUI部分。
    """
    def __init__(self):
        pass

    def window(self, result):
        showWindow = tkinter.Toplevel()
        screenWidth = showWindow.winfo_screenwidth()
        screenHeight = showWindow.winfo_screenheight()
        showWindow.geometry(
            '300x250+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 250) / 2)))
        showWindow.resizable(width=False, height=False)
        showWindow.title('任务详情')
        showWindow.iconbitmap('images/icon.ico')

        # 显示任务
        showMission = '任务id： ' + str(result['missionId'])
        missiondLabel = tkinter.Label(showWindow, text=showMission)
        missiondLabel.place(x=30, y=20, anchor='nw')

        # 显示书名
        showBookName = '任务书名： ' + str(result['bookName'])
        bookNameLabel = tkinter.Label(showWindow, text=showBookName)
        bookNameLabel.place(x=30, y=50, anchor='nw')

        # 显示任务范围
        showMissionRange = '任务范围： ' + str(result['missionRange'])
        missionRangeLabel = tkinter.Label(showWindow, text=showMissionRange)
        missionRangeLabel.place(x=30, y=80, anchor='nw')

        # 显示下次任务时间
        showNextTime = '下次任务时间： ' + str(result['nextTime'])
        nextTimeLabel = tkinter.Label(showWindow, text=showNextTime)
        nextTimeLabel.place(x=30, y=110, anchor='nw')

        # 显示任务状态
        showMissionState = '当前任务状态： ' + str(result['state'])
        stateMissionLabel = tkinter.Label(showWindow, text=showMissionState)
        stateMissionLabel.place(x=30, y=140, anchor='nw')

        # 显示剩余迭代次数
        showLoopTime = '剩余迭代次数： ' + str(result['loopTime'])
        loopTimeLabel = tkinter.Label(showWindow, text=showLoopTime)
        loopTimeLabel.place(x=30, y=170, anchor='nw')

        # 显示完成状态
        showIsFinish = '完成状态： ' + str(result['isFinish'])
        isFinishLabel = tkinter.Label(showWindow, text=showIsFinish)
        isFinishLabel.place(x=30, y=200, anchor='nw')


