# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.ThirdFrame import selectFrame, messageFrame


class ReciterFrame():
    def __init__(self, tab):
        """

        :param tab: tab 为当前frame的父容器
        """
        if DEBUG and VIEW_DEBUG:
            self.thirdTabFrame = tkinter.Frame(tab, height=350, width=700, bg='Thistle')
        else:
            self.thirdTabFrame = tkinter.Frame(tab, height=350, width=700)

        self.thirdTabFrame.place(x=0, y=30, anchor='nw')

        # 调用子组件
        selectFrame.SelectFrame(thirdTabFrame=self.thirdTabFrame)
        self.messageFrame = messageFrame.MessageFrame(thirdTabFrame=self.thirdTabFrame)

        # 语言自定义
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            tab.add(self.thirdTabFrame, text='我的背诵')
        elif languageType == 'EN':
            tab.add(self.thirdTabFrame, text='recitation')
        else:
            tab.add(self.thirdTabFrame, text='我的背诵')

    # def showQuestion(self, recitationId):
    #     self.messageFrame.showAssignQuestion(recitationId)
