# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.ThirdFrame import selectFrame


class ReciterFrame():
    def __init__(self, tab):
        """

        :param tab: tab 为当前frame的父容器
        """
        if DEBUG and VIEW_DEBUG:
            self.firstTabFrame = tkinter.Frame(tab, height=350, width=700, bg='Thistle')
        else:
            self.firstTabFrame = tkinter.Frame(tab, height=350, width=700)

        self.firstTabFrame.place(x=0, y=30, anchor='nw')

        # 调用子组件
        selectFrame.SelectFrame(firstTabFrame=self.firstTabFrame)

        # 语言自定义
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            tab.add(self.firstTabFrame, text='我的背诵')
        elif languageType == 'EN':
            tab.add(self.firstTabFrame, text='recitation')
        else:
            tab.add(self.firstTabFrame, text='我的背诵')
