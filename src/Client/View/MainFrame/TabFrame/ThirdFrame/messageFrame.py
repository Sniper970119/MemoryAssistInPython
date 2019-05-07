# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.recitationSystem import recitationSystem


class MessageFrame():
    def __init__(self, thirdTabFrame=None):
        """

        :param thirdTabFrame: 当前Frame的父容器
        """
        self.missionIdVar = tkinter.StringVar()
        self.missionNameVar = tkinter.StringVar()
        self.missionRangeVar = tkinter.StringVar()
        self.missionStateCodeVar = tkinter.StringVar()
        self.missionNextTimeCodeVar = tkinter.StringVar()
        self.messageBoxTitleVar = tkinter.StringVar()
        self.messageBoxMessageVar = tkinter.StringVar()
        self.language()
        # 获取工具对象
        self.recitationSystemTools = recitationSystem.RecitationSystem()
        # 初始化框架
        if DEBUG and VIEW_DEBUG:
            self.messageFrame = tkinter.Frame(thirdTabFrame, height=350, width=550, bg='yellow')
        else:
            self.messageFrame = tkinter.Frame(thirdTabFrame, height=350, width=550)

        self.messageFrame.place(x=0, y=00, anchor='nw')
        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.missionIdVar.set('任务id')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.missionStateCodeVar.set('任务进度')
            self.missionNextTimeCodeVar.set('下次任务')
            self.messageBoxTitleVar.set('完成任务')
            self.messageBoxMessageVar.set('已完成当前任务')
        elif languageType == 'EN':
            self.missionIdVar.set('mission id')
            self.missionNameVar.set('mission name')
            self.missionRangeVar.set('mission range')
            self.missionStateCodeVar.set('mission state')
            self.missionNextTimeCodeVar.set('next time')
            self.messageBoxTitleVar.set('finish mission')
            self.messageBoxMessageVar.set('mission has been finished')
        else:
            self.missionIdVar.set('任务id')
            self.missionNameVar.set('任务名')
            self.missionRangeVar.set('任务范围')
            self.missionStateCodeVar.set('任务进度')
            self.missionNextTimeCodeVar.set('下次任务')
            self.messageBoxTitleVar.set('完成任务')
            self.messageBoxMessageVar.set('已完成当前任务')

    def printFrame(self):

        pass