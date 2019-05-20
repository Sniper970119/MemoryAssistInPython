# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.recitationSystem import recitationSystem
from src.Client.View.MainFrame.TabFrame.ThirdFrame import messageFrame
from src.Client.SystemTools.ConfFileRead import configFileRead


class ViewAllWindow():
    """
    显示全部任务的GUI界面
    """

    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.recitationIdVar = tkinter.StringVar()
        self.questionVar = tkinter.StringVar()
        self.answerVar = tkinter.StringVar()
        self.weightVar = tkinter.StringVar()
        self.detailVar = tkinter.StringVar()
        self.recitationIdVar = tkinter.StringVar()
        self.weightVar = tkinter.StringVar()
        self.questionVar = tkinter.StringVar()
        self.answerVar = tkinter.StringVar()
        self.deleteVar = tkinter.StringVar()
        self.language()
        self.recitationSystemTools = recitationSystem.RecitationSystem()

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('查看全部（双击查看详情）')
            self.recitationIdVar.set('问题id')
            self.questionVar.set('问题')
            self.answerVar.set('答案')
            self.weightVar.set('权重')
            self.detailVar.set('详情')
            self.deleteVar.set('删除')

            self.recitationIdVar.set('问题id：')
            self.weightVar.set('问题权重：')
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')
        elif languageType == 'EN':
            self.windowTitleVar.set('view all（double click to view detail）')
            self.recitationIdVar.set('recitation id')
            self.questionVar.set('question')
            self.answerVar.set('answer')
            self.weightVar.set('weight')
            self.detailVar.set('detail')
            self.deleteVar.set('delete')

            self.recitationIdVar.set('Id：')
            self.weightVar.set('Weight：')
            self.questionVar.set('Question：')
            self.answerVar.set('Answer：')
        else:
            self.windowTitleVar.set('查看全部（双击查看详情）')
            self.recitationIdVar.set('问题id')
            self.questionVar.set('问题')
            self.answerVar.set('答案')
            self.weightVar.set('权重')
            self.detailVar.set('详情')
            self.deleteVar.set('删除')

            self.recitationIdVar.set('问题id：')
            self.weightVar.set('问题权重：')
            self.questionVar.set('问题描述：')
            self.answerVar.set('答案提示：')

    # 定义鼠标双击事件
    def treeviewClick(self, event):
        """
        定义鼠标在treeview上的双击事件
        :param event:
        :return:
        """
        if DEBUG and VIEW_DEBUG:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                print('{USR}{VIEW_DEBUG} treeview has been double click at ' + item_text[0])
        for item in self.tree.selection():
            detailWindow = tkinter.Toplevel()
            screenWidth = detailWindow.winfo_screenwidth()
            screenHeight = detailWindow.winfo_screenheight()
            detailWindow.geometry(
                '500x350+' + str(int((screenWidth - 500) / 2)) + '+' + str(int((screenHeight - 350) / 2)))
            detailWindow.resizable(width=False, height=False)
            detailWindow.title(self.detailVar.get())
            detailWindow.iconbitmap('images/icon.ico')

            item_text = self.tree.item(item, "values")

            self.recitationDir = self.recitationSystemTools.searchRecitation(item_text[0])
            # id
            idText1 = tkinter.Label(detailWindow, text=self.recitationIdVar.get(), width=15, height=2, anchor='nw')
            idText1.place(x=20, y=0, anchor='nw')
            self.idText2 = tkinter.Label(detailWindow, width=15, height=2, anchor='nw',
                                         text=self.recitationDir['recitationId'])
            self.idText2.place(x=120, y=0, anchor='nw')
            # weight
            weightText1 = tkinter.Label(detailWindow, text=self.weightVar.get(), width=15, height=2, anchor='nw')
            weightText1.place(x=220, y=0, anchor='nw')
            self.weightText2 = tkinter.Label(detailWindow, width=15, height=2, anchor='nw',
                                             text=self.recitationDir['weight'])
            self.weightText2.place(x=320, y=0, anchor='nw')
            # 输入提示框
            inputText1 = tkinter.Label(detailWindow, text=self.questionVar.get(), width=15, height=2, anchor='nw')
            inputText1.place(x=20, y=40, anchor='nw')
            self.inputText2 = tkinter.Label(detailWindow, width=60, height=4, wraplength=370, justify='left',
                                            anchor='nw', text=self.recitationDir['question'])
            self.inputText2.place(x=120, y=40, anchor='nw')
            # 输出提示框
            outputText1 = tkinter.Label(detailWindow, text=self.answerVar.get(), width=15, height=2, anchor='nw')
            outputText1.place(x=20, y=120, anchor='nw')
            self.outputText2 = tkinter.Label(detailWindow, width=60, height=10, wraplength=370, justify='left',
                                             anchor='nw', text=self.recitationDir['answer'])
            self.outputText2.place(x=120, y=120, anchor='nw')
            # 下一个问题按钮
            nextQuestionButton = tkinter.Button(detailWindow, text=self.deleteVar.get(), width=10, height=1,
                                                command=self.deleteRecitation)
            nextQuestionButton.place(x=400, y=300, anchor='nw')
            # 调用用户操作记录函数，记录用户此次操作
            self.logUserAction('recitation treeview has been double click at ', item_text[0])
        pass

    def deleteRecitation(self):
        if self.recitationDir['recitationId'] == '000001':
            return
        # 用户再次确认
        if messagebox.askokcancel(title=self.deleteVar.get(), message=self.deleteVar.get()+str(self.recitationDir['recitationId'])):
            self.recitationSystemTools.editRecitation(recitationId=self.recitationDir['recitationId'], isDelete=True)

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '550x320+' + str(int((screenWidth - 550) / 2)) + '+' + str(int((screenHeight - 320) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title(self.windowTitleVar.get())
        self.addWindow.iconbitmap('images/icon.ico')
        self.tree = ttk.Treeview(self.addWindow, columns=['1', '2', '3', '4'], show='headings',
                                 height=15)

        self.tree.column('1', width=80, anchor='center')
        self.tree.column('2', width=150, anchor='center')
        self.tree.column('3', width=250, anchor='center')
        self.tree.column('4', width=80, anchor='center')
        self.tree.heading('1', text=self.recitationIdVar.get())
        self.tree.heading('2', text=self.questionVar.get())
        self.tree.heading('3', text=self.answerVar.get())
        self.tree.heading('4', text=self.weightVar.get())
        self.tree.bind("<Double-Button-1>", self.treeviewClick)
        self.tree.place(x=0, y=0, anchor='nw')
        list = self.recitationSystemTools.loadRecitation()
        for each in list:
            dataInList = [each['recitationId'], each['question'], each['answer'], each['weight']]
            self.tree.insert('', 'end', values=dataInList)

    def logUserAction(self, action, message=None):

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
