# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.recitationSystem import recitationSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import messageFrame


class EditWindow():
    """
    编辑任务的GUI界面。负责显示编辑任务的GUI以及非法输入拦截。
    """

    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        # 分别为 提示任务id  id举例（输入栏瞎编的提示）
        self.missionIdHintVar = tkinter.StringVar()
        self.missionIdExampleVar = tkinter.StringVar()
        #
        self.questionHintVar = tkinter.StringVar()
        self.questionExampleVar = tkinter.StringVar()
        #
        self.answerHintVar = tkinter.StringVar()
        self.answerExampleVar = tkinter.StringVar()
        #
        self.weightHintVar = tkinter.StringVar()
        self.weightExampleVar = tkinter.StringVar()
        #
        self.missionLoopTimeHintVar = tkinter.StringVar()
        self.missionLoopTimeExamlpeVar = tkinter.StringVar()
        #
        self.missionMissionStateHintVar = tkinter.StringVar()
        self.missionMissionStateExampleVar = tkinter.StringVar()
        # error message
        self.wrongIdTitleVar = tkinter.StringVar()
        self.wrongIdMessageVar = tkinter.StringVar()
        #
        self.wrongQuestionTitleVar = tkinter.StringVar()
        self.wrongQuestionMessageVar = tkinter.StringVar()
        #
        self.wrongAnswerTitleVar = tkinter.StringVar()
        self.wrongAnswerMessageVar = tkinter.StringVar()
        #
        self.wrongWeightTitleVar = tkinter.StringVar()
        self.wrongWeightMessageVar = tkinter.StringVar()
        #
        self.ifGoOnTitleVar = tkinter.StringVar()
        self.ifGoOnMessageVar = tkinter.StringVar()
        # button
        self.editButtonVar = tkinter.StringVar()

        self.language()
        # 临时保存权重，用于对修改范围进行监控
        self.weightCheck = 0
        self.recitationSystemTools = recitationSystem.RecitationSystem()

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('编辑提问任务')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('任务id')
            self.missionIdExampleVar.set('例如：输入 000001 或者 1')
            #
            self.questionHintVar.set('问题')
            self.questionExampleVar.set('需要提问的问题（记得先把任务 id 填了哦~）')
            #
            self.answerHintVar.set('答案')
            self.answerExampleVar.set('提问问题的答案')

            self.weightHintVar.set('权重')
            self.weightExampleVar.set('问题的权重，作为出现次数频率的依据，不建议修改幅度过大，可能影响其他问题出现的频率')
            # error message
            self.wrongIdTitleVar.set('错误的id')
            self.wrongIdMessageVar.set('请输入正确的任务id（非数字）')
            #
            self.wrongQuestionTitleVar.set('错误的问题')
            self.wrongQuestionMessageVar.set('请输入正确的问题（空白或者过长）')
            #
            self.wrongAnswerTitleVar.set('错误的答案')
            self.wrongAnswerMessageVar.set('请输入正确的答案（空白或者过长）')
            # #
            self.wrongWeightTitleVar.set('错误的权重范围')
            self.wrongWeightMessageVar.set('输入正确的权重范围（修改幅度过大）')

            self.ifGoOnTitleVar.set('是否继续编辑')
            self.ifGoOnMessageVar.set('确认后不可恢复，确认信息正确有效')
            # button
            self.editButtonVar.set('确认编辑')
        elif languageType == 'EN':
            self.windowTitleVar.set('edit recitation')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('recitation id')
            self.missionIdExampleVar.set('eg：input入 000001 or 1')
            #
            self.questionHintVar.set('question')
            self.questionExampleVar.set('question(recitation id first~)')
            #
            self.answerHintVar.set('answer')
            self.answerExampleVar.set('the answer of the question')

            self.weightHintVar.set('weight')
            self.weightExampleVar.set(
                'as the basis of frequency, do not modify the number too much,it may cause some problem')
            # error message
            self.wrongIdTitleVar.set('wrong id')
            self.wrongIdMessageVar.set('please input current mission id（your input is not a number）')
            #
            self.wrongQuestionTitleVar.set('wrong question')
            self.wrongQuestionMessageVar.set('please input the current question（your input is null or is too long）')
            #
            self.wrongAnswerTitleVar.set('wrong answer')
            self.wrongAnswerMessageVar.set('please input the current answer（your input is null or is too long）')
            # #
            self.wrongWeightTitleVar.set('wrong weight')
            self.wrongWeightTitleVar.set('please input current weight（your input is out of range）')

            self.ifGoOnTitleVar.set('Edit')
            self.ifGoOnMessageVar.set("if you choose ok,information will be change and can't recover")
            # button
            self.editButtonVar.set('edit')
        else:
            self.windowTitleVar.set('编辑提问任务')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('任务id')
            self.missionIdExampleVar.set('例如：输入 000001 或者 1')
            #
            self.questionHintVar.set('问题')
            self.questionExampleVar.set('需要提问的问题（记得先把任务 id 填了哦~）')
            #
            self.answerHintVar.set('答案')
            self.answerExampleVar.set('提问问题的答案')

            self.weightHintVar.set('权重')
            self.weightExampleVar.set('问题的权重，作为出现次数频率的依据，不建议修改幅度过大，可能影响其他问题出现的频率')
            # error message
            self.wrongIdTitleVar.set('错误的id')
            self.wrongIdMessageVar.set('请输入正确的任务id（非数字）')
            #
            self.wrongQuestionTitleVar.set('错误的问题')
            self.wrongQuestionMessageVar.set('请输入正确的问题（空白或者过长）')
            #
            self.wrongAnswerTitleVar.set('错误的答案')
            self.wrongAnswerMessageVar.set('请输入正确的任答案（空白或者过长）')
            # #
            self.wrongWeightTitleVar.set('错误的权重范围')
            self.wrongWeightTitleVar.set('输入正确的权重范围（修改幅度过大）')

            self.ifGoOnTitleVar.set('是否继续编辑')
            self.ifGoOnMessageVar.set('确认后不可恢复，确认信息正确有效')
            # button
            self.editButtonVar.set('确认编辑')

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '300x430+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 430) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title(self.windowTitleVar.get())
        self.addWindow.iconbitmap('images/icon.ico')

        self.recitationId = tkinter.StringVar()
        self.question = tkinter.StringVar()
        self.answer = tkinter.StringVar()
        self.weight = tkinter.StringVar()

        def findMission(event):
            missionId = idEntry.get()
            missionDir = self.recitationSystemTools.searchRecitation(recitationId=missionId)
            self.recitationId.set(missionDir['recitationId'])
            self.question.set(missionDir['question'])
            self.answer.set(missionDir['answer'])
            self.weight.set(missionDir['weight'])
            self.weightCheck = missionDir['weight']
            self.answerEntry.delete('1.0', 'end')
            self.answerEntry.insert('insert', missionDir['answer'])
            pass

        # 任务id获取
        idLabel = tkinter.Label(self.addWindow, text=self.missionIdHintVar.get(), font=('Arial', 12), width=15,
                                height=2)
        idLabel.place(x=-20, y=20, anchor='nw')

        idTLabel = tkinter.Label(self.addWindow, text=self.missionIdExampleVar.get(), font=('Arial', 8), width=30,
                                 height=1,
                                 foreground='DimGray', wraplength=180, justify='left', anchor='nw')
        idTLabel.place(x=100, y=55, anchor='nw')

        idEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        idEntry.place(x=100, y=25, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中,如果按下tab，则执行任务查找
        idEntry.bind('<KeyPress-Tab>', findMission)

        # 问题获取
        questionLabel = tkinter.Label(self.addWindow, text=self.questionHintVar.get(), font=('Arial', 12), width=15,
                                      height=2)
        questionLabel.place(x=-20, y=70, anchor='nw')

        questionTLabel = tkinter.Label(self.addWindow, text=self.questionExampleVar.get(), font=('Arial', 8),
                                       width=40, height=2,
                                       foreground='DimGray', wraplength=180, justify='left', anchor='nw')
        questionTLabel.place(x=100, y=105, anchor='nw')

        questionEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                      textvariable=self.question)
        questionEntry.place(x=100, y=75, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中
        questionEntry.bind('<ButtonPress-1>', findMission)

        # 状态获取
        weightLabel = tkinter.Label(self.addWindow, text=self.weightHintVar.get(), font=('Arial', 12), width=15,
                                    height=2)
        weightLabel.place(x=-20, y=140, anchor='nw')

        # 空格为为了拉gui显示的距离
        weightTLabel = tkinter.Label(self.addWindow,
                                     text=self.weightExampleVar.get(),
                                     font=('Arial', 8), width=50, height=3,
                                     foreground='DimGray', wraplength=180, justify='left', anchor='nw')
        weightTLabel.place(x=100, y=175, anchor='nw')

        weightEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                    textvariable=self.weight)
        weightEntry.place(x=100, y=145, anchor='nw')

        # 答案获取
        answerLabel = tkinter.Label(self.addWindow, text=self.answerHintVar.get(), font=('Arial', 12), width=15,
                                    height=2)
        answerLabel.place(x=-20, y=220, anchor='nw')

        answerTLabel = tkinter.Label(self.addWindow, text=self.answerExampleVar.get(), font=('Arial', 8),
                                     width=30,
                                     height=1,
                                     foreground='DimGray', wraplength=180, justify='left', anchor='nw')
        answerTLabel.place(x=100, y=255, anchor='nw')

        self.answerEntry = tkinter.Text(self.addWindow, width=20, height=9, font=('Arial', 10))
        self.answerEntry.place(x=100, y=225, anchor='nw')

        def editRecitation():
            """
            编辑按钮的事件
            :return:
            """

            # 输入的任务id检查
            id = idEntry.get()
            answer = self.answerEntry.get("0.0", "end")[:-1]
            try:
                id = int(idEntry.get())
            except:
                messagebox.showwarning(title=self.wrongIdTitleVar.get(), message=self.wrongIdMessageVar.get())
                return
            # 问题检查
            if self.question.get() is '' or len(self.question.get()) > 100:
                messagebox.showwarning(title=self.wrongQuestionTitleVar.get(),
                                       message=self.wrongQuestionMessageVar.get())
                return
            # 答案检查
            print(len(answer))
            if answer is '' or len(answer) > 300:
                messagebox.showwarning(title=self.wrongAnswerTitleVar.get(), message=self.wrongAnswerMessageVar.get())
                return
            # 任务状态检查
            weight = self.weight.get()
            try:
                weight = int(self.weight.get())
                if abs(int(self.weightCheck) - weight) > 20:
                    messagebox.showwarning(title=self.wrongWeightTitleVar.get(),
                                           message=self.wrongWeightMessageVar.get())
                if weight < 5:
                    messagebox.showwarning(title=self.wrongWeightTitleVar.get(),
                                           message=self.wrongWeightMessageVar.get())
                    return
            except:
                messagebox.showwarning(title=self.wrongWeightTitleVar.get(), message=self.wrongWeightMessageVar.get())
                return
            # 用户再次确认
            if messagebox.askokcancel(title=self.ifGoOnTitleVar.get(), message=self.ifGoOnMessageVar.get()):
                # 调用添加任务工具
                self.recitationSystemTools.editRecitation(recitationId=id, question=questionEntry.get(),
                                                          answer=answer,
                                                          weight=weightEntry.get(),
                                                          isEdit=True)
                # 关闭窗口
                self.addWindow.after(300, self.addWindow.destroy)
                # 将messageFrame的重绘变量置为True
                messageFrame.MessageFrame.needReprint = True
                # 记录用户操作
                self.logUserAction('user click edit recitation button')
                if DEBUG and VIEW_DEBUG:
                    print('{USR}{MESSAGE_FRAME} now user click edit recitation button')

        # 按钮
        addButton = tkinter.Button(self.addWindow, text=self.editButtonVar.get(), command=editRecitation, width=8)
        addButton.place(x=200, y=385, anchor='nw')

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
