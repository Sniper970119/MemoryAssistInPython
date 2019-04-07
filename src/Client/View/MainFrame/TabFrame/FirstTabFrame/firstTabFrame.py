# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import messageFrame
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import selectFrame


class FirstTabFrame():
    """
    第一个Tab框架，负责显示任务信息等GUI界面。
    """

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
        messageFrame.MessageFrame(firstTabFrame=self.firstTabFrame)
        selectFrame.SelectFrame(firstTabFrame=self.firstTabFrame)

        # 语言自定义
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            tab.add(self.firstTabFrame, text='我的计划')
        elif languageType == 'EN':
            tab.add(self.firstTabFrame, text='my plan')
        else:
            tab.add(self.firstTabFrame, text='我的计划')
