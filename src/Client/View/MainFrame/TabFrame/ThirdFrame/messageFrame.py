# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.recitationSystem import recitationSystem


class MessageFrame():
    def __init__(self, thirdTabFrame=None):
        """

        :param thirdTabFrame: 当前Frame的父容器
        """
        self.recitationIdVar = tkinter.StringVar()
        self.weightVar = tkinter.StringVar()
        self.questionVar = tkinter.StringVar()
        self.answerVar = tkinter.StringVar()
        self.nextQuestionVar = tkinter.StringVar()
        self.hintVar = tkinter.StringVar()
        self.language()
        # 初始化当前问题提示次数
        self.hintTime = 0
        # 初始化当前问题提示次数
        self.currentQuestionWeight = 0
        # 初始化当前显示的问题id
        self.currentQuestionId = '000000'
        self.answer = ''
        # 获取工具对象
        self.recitationSystemTools = recitationSystem.RecitationSystem()
        # 初始化框架
        if DEBUG and VIEW_DEBUG:
            self.messageFrame = tkinter.Frame(thirdTabFrame, height=350, width=550, bg='yellow')
        else:
            self.messageFrame = tkinter.Frame(thirdTabFrame, height=350, width=550)

        self.messageFrame.place(x=0, y=00, anchor='nw')
        self.printFrame()
        # 初始化第一次问题
        self.showRandomQuestion()
        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.recitationIdVar.set('问题id：')
            self.weightVar.set('问题权重：')
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')
            self.nextQuestionVar.set('下个问题')
            self.hintVar.set('需要提示')
        elif languageType == 'EN':
            self.recitationIdVar.set('Id：')
            self.weightVar.set('Weight：')
            self.questionVar.set('Question：')
            self.answerVar.set('Answer：')
            self.nextQuestionVar.set('Next question')
            self.hintVar.set('See hint')
        else:
            self.recitationIdVar.set('问题id：')
            self.weightVar.set('问题权重：')
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')
            self.nextQuestionVar.set('下个问题')
            self.hintVar.set('需要提示')

    def printFrame(self):
        """
        绘制消息框架
        :return:
        """
        # id
        idText1 = tkinter.Label(self.messageFrame, text=self.recitationIdVar.get(), width=15, height=2, anchor='nw')
        idText1.place(x=20, y=0, anchor='nw')
        self.idText2 = tkinter.Label(self.messageFrame, width=15, height=2, anchor='nw')
        self.idText2.place(x=120, y=0, anchor='nw')
        # weight
        weightText1 = tkinter.Label(self.messageFrame, text=self.weightVar.get(), width=15, height=2, anchor='nw')
        weightText1.place(x=220, y=0, anchor='nw')
        self.weightText2 = tkinter.Label(self.messageFrame, width=15, height=2, anchor='nw')
        self.weightText2.place(x=320, y=0, anchor='nw')
        # 输入提示框
        inputText1 = tkinter.Label(self.messageFrame, text=self.questionVar.get(), width=15, height=2, anchor='nw')
        inputText1.place(x=20, y=40, anchor='nw')
        self.inputText2 = tkinter.Label(self.messageFrame, width=60, height=4, wraplength=420, justify='left',
                                        anchor='nw')
        self.inputText2.place(x=120, y=40, anchor='nw')
        # 输出提示框
        outputText1 = tkinter.Label(self.messageFrame, text=self.answerVar.get(), width=15, height=2, anchor='nw')
        outputText1.place(x=20, y=120, anchor='nw')
        self.outputText2 = tkinter.Label(self.messageFrame, width=60, height=8, wraplength=420, justify='left',
                                         anchor='nw')
        self.outputText2.place(x=120, y=120, anchor='nw')
        # 下一个问题按钮
        nextQuestionButton = tkinter.Button(self.messageFrame, text=self.nextQuestionVar.get(), width=10, height=1,
                                            command=self.showRandomQuestion)
        nextQuestionButton.place(x=350, y=280, anchor='nw')
        # 提示按钮
        hintButton = tkinter.Button(self.messageFrame, text=self.hintVar.get(), width=10, height=1,
                                    command=self.showHint)
        hintButton.place(x=450, y=280, anchor='nw')

        pass

    def showAssignQuestion(self, recitationId):
        """
        显示指定的问题
        :return:
        """
        # 记录用户点击事件
        self.logUserAction('user choose question detail', str(recitationId))
        mission = self.recitationSystemTools.searchRecitation(recitationId=recitationId)

        self.idText2.config(text=mission['recitationId'])
        self.weightText2.config(text=mission['weight'])
        self.inputText2.config(text=mission['question'])
        self.outputText2.config(text=mission['answer'])
        # 重新初始化重复次数
        self.hintTime = 0
        # 初始化id 以及记录当前权重
        self.currentQuestionId = mission['recitationId']
        self.currentQuestionWeight = mission['weight']
        self.answer = mission['answer']
        pass

    def showRandomQuestion(self):
        """
        点击下一问题按钮的动作(随机
        :return:
        """
        # 记录用户点击事件
        self.logUserAction('user choose next question')
        mission = self.recitationSystemTools.getOneRecitation()
        # 判断用户是否为点击过提示就下一题，即判断用户已经会本题
        if self.hintTime == 0:
            if self.currentQuestionWeight > 8:
                # 会背后权重-3
                self.recitationSystemTools.editRecitation(self.currentQuestionId, weight=self.currentQuestionWeight - 3,
                                                          isEdit=True)
            else:
                # 非人为干预情况下最低为5
                self.recitationSystemTools.editRecitation(self.currentQuestionId, weight=5, isEdit=True)
        # 处理点击过提示，对当前信息权值进行增加
        else:
            # 如果提示次数小于3次，则认为有印象，少量增加权重
            if self.hintTime < 3:
                self.recitationSystemTools.editRecitation(self.currentQuestionId, weight=self.currentQuestionWeight + 2,
                                                          isEdit=True)
            else:
                self.recitationSystemTools.editRecitation(self.currentQuestionId, weight=self.currentQuestionWeight + 5,
                                                          isEdit=True)
        self.idText2.config(text=mission['recitationId'])
        self.weightText2.config(text=mission['weight'])
        self.inputText2.config(text=mission['question'])
        self.outputText2.config(text='')
        # 重新初始化重复次数
        self.hintTime = 0
        # 初始化id 以及记录当前权重
        self.currentQuestionId = mission['recitationId']
        self.currentQuestionWeight = mission['weight']
        self.answer = mission['answer']

        pass

    def showHint(self):
        """
        点击提示按钮的动作
        :return:
        """
        # 记录用户点击事件
        self.logUserAction('user choose hint')
        self.hintTime = self.hintTime + 1
        if self.hintTime == 1:
            self.outputText2.config(text=self.subString(self.answer, 10))
        elif self.hintTime == 2:
            self.outputText2.config(text=self.subString(self.answer, 30))
        elif self.hintTime == 3:
            self.outputText2.config(text=self.subString(self.answer, 80))
        elif self.hintTime == 4:
            self.outputText2.config(text=self.subString(self.answer, 150))
        elif self.hintTime == 5:
            self.outputText2.config(text=self.subString(self.answer, 250))
        else:
            self.outputText2.config(text=self.answer)
        pass

    def subString(self, text, length):
        """
        处理涉及到中文字符串的截取
        :param text:  文本
        :param length: 截取长度
        :return:
        """
        if length >= len(text):
            return text
        result = ''
        i = 0
        p = 0
        while True:
            ch = ord(text[i])
            # 1111110x
            if ch >= 252:
                p = p + 6
            # 111110xx
            elif ch >= 248:
                p = p + 5
            # 11110xxx
            elif ch >= 240:
                p = p + 4
            # 1110xxxx
            elif ch >= 224:
                p = p + 3
            # 110xxxxx
            elif ch >= 192:
                p = p + 2
            else:
                p = p + 1
            if p >= length:
                break
            else:
                i = p
        return text[0:i]

    def logUserAction(self, action, message=None):
        """
        用户动作记录
        :param action: 动作
        :param message: 需要携带的额外信息
        :return:
        """
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
