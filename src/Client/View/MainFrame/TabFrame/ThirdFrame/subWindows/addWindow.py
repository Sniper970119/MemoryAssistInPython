# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.recitationSystem import recitationSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import messageFrame


class AddWindow():
    """
    添加任务的GUI界面。负责显示添加任务的GUI以及非法输入拦截。
    """

    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.questionVar = tkinter.StringVar()
        self.answerVar = tkinter.StringVar()
        self.weightVar = tkinter.StringVar()
        self.addVar = tkinter.StringVar()
        self.errorTitleVar = tkinter.StringVar()
        self.errorMessage1Var = tkinter.StringVar()
        self.errorMessage2Var = tkinter.StringVar()
        self.errorMessage3Var = tkinter.StringVar()
        self.errorMessage4Var = tkinter.StringVar()
        self.weightExampleVar = tkinter.StringVar()
        self.language()
        self.recitationSystemTools = recitationSystem.RecitationSystem()
        self.addWindow = None

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('添加背诵')
            self.questionVar.set('问题')
            self.answerVar.set('答案')
            self.weightVar.set('权重')
            self.weightExampleVar.set('出现频率权重，要求在10~30之间')
            self.addVar.set('添加')
            self.errorTitleVar.set('添加错误')
            self.errorMessage1Var.set('问题和答案不可为空')
            self.errorMessage2Var.set('权重不在允许范围内或为非数字')
            self.errorMessage3Var.set('问题过长')
            self.errorMessage4Var.set('答案过长')
        elif languageType == 'EN':
            self.windowTitleVar.set('add recitation')
            self.questionVar.set('question')
            self.answerVar.set('answer')
            self.weightVar.set('weight')
            self.weightExampleVar.set('frequency of occurrence,between 10 and 30')
            self.addVar.set('add')
            self.errorTitleVar.set('add error')
            self.errorMessage1Var.set("question name and answer can't be null")
            self.errorMessage2Var.set("weight is not in the right range or it is now a number")
            self.errorMessage3Var.set('问题过长')
            self.errorMessage4Var.set('答案过长')
        else:
            self.windowTitleVar.set('添加背诵')
            self.questionVar.set('问题')
            self.answerVar.set('答案')
            self.weightVar.set('权重')
            self.weightExampleVar.set('出现频率权重，要求在10~30之间')
            self.addVar.set('添加')
            self.errorTitleVar.set('添加错误')
            self.errorMessage1Var.set('问题和答案不可为空')
            self.errorMessage2Var.set('权重不在允许范围内或为非数字')
            self.errorMessage3Var.set('问题过长')
            self.errorMessage4Var.set('答案过长')

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '300x300+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 300) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title(self.windowTitleVar.get())
        self.addWindow.iconbitmap('images/icon.ico')

        questionLabel = tkinter.Label(self.addWindow, text=self.questionVar.get(), font=('Arial', 12), width=15,
                                      height=2)
        questionLabel.place(x=-20, y=20, anchor='nw')

        questionEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        questionEntry.place(x=100, y=25, anchor='nw')

        weightLabel = tkinter.Label(self.addWindow, text=self.weightVar.get(), font=('Arial', 12), width=15, height=2)
        weightLabel.place(x=-20, y=70, anchor='nw')

        weightEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        weightEntry.place(x=100, y=75, anchor='nw')

        weightTLabel = tkinter.Label(self.addWindow, text=self.weightExampleVar.get(), font=('Arial', 8), width=30,
                                     height=2, anchor='nw', foreground='DimGray', wraplength=180, justify='left')
        weightTLabel.place(x=100, y=105, anchor='nw')

        answerLabel = tkinter.Label(self.addWindow, text=self.answerVar.get(), font=('Arial', 12), width=15, height=2)
        answerLabel.place(x=-20, y=140, anchor='nw')

        self.answerEntry = tkinter.Text(self.addWindow, width=20, height=6, font=('Arial', 10))
        self.answerEntry.place(x=100, y=145, anchor='nw')

        def addMission():
            """
            确认添加按钮的事件
            :return:
            """
            # 获取两个任务信息
            question = questionEntry.get()
            answer = self.answerEntry.get("0.0", "end")[:-1]
            weight = weightEntry.get()
            # 检查输入非空，若为空向用户反馈更改
            if question is '' or answer is '':
                messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage1Var.get())
                return

            # 检查问题长度范围范围是否允许
            try:
                if len(question) > 100:
                    messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage3Var.get())
                    return
            except:
                messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage3Var.get())
                return

            # 检查答案长度范围范围是否允许
            try:
                if len(answer) > 300:
                    messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage4Var.get())
                    return
            except:
                messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage4Var.get())
                return
            # 检查权重范围是否允许
            try:
                weight = int(weight)
                if int(weight) < 10 or int(weight) > 30:
                    messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage2Var.get())
                    return
            except:
                messagebox.showwarning(title=self.errorTitleVar.get(), message=self.errorMessage2Var.get())
                return
            # 调用添加任务工具
            self.recitationSystemTools.addRecitation(question=question, answer=answer, weight=weight)
            # 关闭窗口
            self.addWindow.after(300, self.addWindow.destroy)
            # 将messageFrame的重绘变量置为True
            messageFrame.MessageFrame.needReprint = True
            if DEBUG and VIEW_DEBUG:
                print('{USR}{MESSAGE_FRAME} now user click add mission button and system save it')
            pass

        # 按钮
        addButton = tkinter.Button(self.addWindow, text=self.addVar.get(), command=addMission, width=8)
        addButton.place(x=200, y=250, anchor='nw')
