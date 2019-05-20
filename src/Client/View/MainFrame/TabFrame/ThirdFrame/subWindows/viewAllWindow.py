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
        elif languageType == 'EN':
            self.windowTitleVar.set('view all（double click to view detail）')
            self.recitationIdVar.set('recitation id')
            self.questionVar.set('question')
            self.answerVar.set('answer')
            self.weightVar.set('weight')
        else:
            self.windowTitleVar.set('查看全部（双击查看详情）')
            self.recitationIdVar.set('问题id')
            self.questionVar.set('问题')
            self.answerVar.set('答案')
            self.weightVar.set('权重')

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
            item_text = self.tree.item(item, "values")
            # print('对id为'+item_text[0]+'执行双击操作')
            messageFrame.MessageFrame.showAssignQuestion(item_text[0])
            self.addWindow.after(300, self.addWindow.destroy)
            # 调用用户操作记录函数，记录用户此次操作
            self.logUserAction('recitation treeview has been double click at ', item_text[0])
        pass


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
