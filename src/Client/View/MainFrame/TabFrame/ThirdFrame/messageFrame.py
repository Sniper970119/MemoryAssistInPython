# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.recitationSystem import recitationSystem


class MessageFrame():
    def __init__(self, thirdTabFrame=None):
        """

        :param thirdTabFrame: 当前Frame的父容器
        """
        self.questionVar = tkinter.StringVar()
        self.answerVar = tkinter.StringVar()
        self.nextQuestionVar = tkinter.StringVar()
        self.hintVar = tkinter.StringVar()
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
        self.printFrame()
        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')
            self.nextQuestionVar.set('下个问题')
            self.hintVar.set('提示')
            self.missionNextTimeCodeVar.set('下次任务')
            self.messageBoxTitleVar.set('完成任务')
            self.messageBoxMessageVar.set('已完成当前任务')
        elif languageType == 'EN':
            self.questionVar.set('Question：')
            self.answerVar.set('Answer：')
            self.nextQuestionVar.set('next question')
            self.hintVar.set('hint')
            self.missionNextTimeCodeVar.set('next time')
            self.messageBoxTitleVar.set('finish mission')
            self.messageBoxMessageVar.set('mission has been finished')
        else:
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')
            self.nextQuestionVar.set('下个问题')
            self.hintVar.set('提示')
            self.missionNextTimeCodeVar.set('下次任务')
            self.messageBoxTitleVar.set('完成任务')
            self.messageBoxMessageVar.set('已完成当前任务')

    def printFrame(self):
        """
        绘制消息框架
        :return:
        """
        # 输入提示框
        self.inputText1 = tkinter.Label(self.messageFrame, text=self.questionVar.get(), width=15, height=2)
        self.inputText1.place(x=20, y=20, anchor='nw')
        # 输出提示框
        self.outputText1 = tkinter.Label(self.messageFrame, text=self.answerVar.get(), width=15, height=2)
        self.outputText1.place(x=20, y=120, anchor='nw')
        # 下一个问题按钮
        self.nextQuestionButton = tkinter.Button(self.messageFrame, text=self.nextQuestionVar.get(), width=10, height=1)
        self.nextQuestionButton.place(x=350, y=280, anchor='nw')
        # 提示按钮
        self.hintButton = tkinter.Button(self.messageFrame, text=self.hintVar.get(), width=10, height=1)
        self.hintButton.place(x=450, y=280, anchor='nw')

        pass
