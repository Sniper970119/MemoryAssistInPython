# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.MissionSystem import missionSystem
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
        self.missionNameHintVar = tkinter.StringVar()
        self.missionNameExampleVar = tkinter.StringVar()
        #
        self.missionRangeHintVar = tkinter.StringVar()
        self.missionRangeExampleVar = tkinter.StringVar()
        #
        self.missionStateHintVar = tkinter.StringVar()
        self.missionStateExampleVar = tkinter.StringVar()
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
        self.wrongNameTitleVar = tkinter.StringVar()
        self.wrongNameMessageVar = tkinter.StringVar()
        #
        self.wrongRangeTitleVar = tkinter.StringVar()
        self.wrongRangeMessageVar = tkinter.StringVar()
        #
        self.wrongStateTitleVar = tkinter.StringVar()
        self.wrongStateMessageVar = tkinter.StringVar()
        #
        self.wrongLoopTimeTitleVar = tkinter.StringVar()
        self.wrongLoopTimeMessageVar = tkinter.StringVar()
        #
        self.wrongFinishStateTitleVar = tkinter.StringVar()
        self.wrongFinishStateMessage1Var = tkinter.StringVar()
        self.wrongFinishStateMessage2Var = tkinter.StringVar()
        #
        self.ifGoOnTitleVar = tkinter.StringVar()
        self.ifGoOnMessageVar = tkinter.StringVar()
        # button
        self.editButtonVar = tkinter.StringVar()

        self.language()
        self.missionSystemTools = missionSystem.MissionSystem()

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('编辑任务')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('任务id')
            self.missionIdExampleVar.set('例如：输入 000001 或者 1')
            #
            self.missionNameHintVar.set('书名')
            self.missionNameExampleVar.set('背的书名（记得先把任务 id 填了哦~）')
            #
            self.missionRangeHintVar.set('任务范围')
            self.missionRangeExampleVar.set('输入任务范围 例如：p1~p6')
            #
            self.missionStateHintVar.set('状态代码')
            self.missionStateExampleVar.set('0，1，2，3，4，5，6，7 分别为不再提示、          \n当天、次日、两天后、四天后、                               \n七天后、十五天后、和循环记忆                                 ')
            #
            self.missionLoopTimeHintVar.set('循环次数')
            self.missionLoopTimeExamlpeVar.set('15天后再重复的次数，默认为5      ')
            #
            self.missionMissionStateHintVar.set('是否完成')
            self.missionMissionStateExampleVar.set('0 代表未完成 1 代表完成     ')
            # error message
            self.wrongIdTitleVar.set('错误的id')
            self.wrongIdMessageVar.set('请输入正确的任务id（非数字）')
            #
            self.wrongNameTitleVar.set('错误的书名')
            self.wrongNameMessageVar.set('请输入正确的书名（空白的书名）')
            #
            self.wrongRangeTitleVar.set('错误的任务范围')
            self.wrongRangeMessageVar.set('请输入正确的任务范围（空白的任务范围）')
            #
            self.wrongStateTitleVar.set('错误的任务状态')
            self.wrongStateMessageVar.set('输入正确的任务状态编码（范围错误）')
            #
            self.wrongLoopTimeTitleVar.set('错误的迭代次数')
            self.wrongLoopTimeMessageVar.set('请输入正确的迭代次数（非数字）')
            #
            self.wrongFinishStateTitleVar.set('错误的完成状态')
            self.wrongFinishStateMessage1Var.set('输入正确的完成状态编码（范围错误）')
            self.wrongFinishStateMessage2Var.set('请输入正确的完成状态编码（非数字）')
            #
            self.ifGoOnTitleVar.set('是否继续编辑')
            self.ifGoOnMessageVar.set('确认后不可恢复，确认信息正确有效')
            # button
            self.editButtonVar.set('确认编辑')
        elif languageType == 'EN':
            self.windowTitleVar.set('edit mission')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('mission id')
            self.missionIdExampleVar.set('eg：input 000001 or 1')
            #
            self.missionNameHintVar.set('mission name')
            self.missionNameExampleVar.set('mission name(mission id first~)')
            #
            self.missionRangeHintVar.set('mission range')
            self.missionRangeExampleVar.set('mission range.eg：p1~p6')
            #
            self.missionStateHintVar.set('state code')
            self.missionStateExampleVar.set('0,1,2,3,4,5,6,7 respectively never \nappear,today,1,2,4,7,15 days\nlater、and appear circle')
            #
            self.missionLoopTimeHintVar.set('loop time')
            self.missionLoopTimeExamlpeVar.set('loop time after 15 days,defaults 5')
            #
            self.missionMissionStateHintVar.set('is finish')
            self.missionMissionStateExampleVar.set('1 stand for true,and 0 opposite')
            # error message
            self.wrongIdTitleVar.set('wrong id')
            self.wrongIdMessageVar.set('please input the current mission id（your input is not a number）')
            #
            self.wrongNameTitleVar.set('wrong mission name')
            self.wrongNameMessageVar.set('please input the current mission name（your input is null）')
            #
            self.wrongRangeTitleVar.set('wrong mission range')
            self.wrongRangeMessageVar.set('please input current mission range（your input is null）')
            #
            self.wrongStateTitleVar.set('wrong mission code')
            self.wrongStateMessageVar.set('please input current mission code（your input is in wrong range）')
            #
            self.wrongLoopTimeTitleVar.set('wrong loop time')
            self.wrongLoopTimeMessageVar.set('please input current loop time（your input is not a number）')
            #
            self.wrongFinishStateTitleVar.set('wrong state code')
            self.wrongFinishStateMessage1Var.set('please input current state cpde（your input is in wrong range）')
            self.wrongFinishStateMessage2Var.set('please input current state code（your input is in not a number）')
            #
            self.ifGoOnTitleVar.set('Edit')
            self.ifGoOnMessageVar.set("if you choose ok,information will be change and can't recover")
            # button
            self.editButtonVar.set('edit')
        else:
            self.windowTitleVar.set('编辑任务')
            # 分别为 提示任务id  id举例（输入栏瞎编的提示）
            self.missionIdHintVar.set('任务id')
            self.missionIdExampleVar.set('例如：输入 000001 或者 1')
            #
            self.missionNameHintVar.set('书名')
            self.missionNameExampleVar.set('背的书名（记得先把任务 id 填了哦~）')
            #
            self.missionRangeHintVar.set('任务范围')
            self.missionRangeExampleVar.set('输入任务范围 例如：p1~p6')
            #
            self.missionStateHintVar.set('状态代码')
            self.missionStateExampleVar.set('0，1，2，3，4，5，6，7 分别为不再提示、          \n当天、次日、两天后、四天后、                               \n七天后、十五天后、和循环记忆                                 ')
            #
            self.missionLoopTimeHintVar.set('循环次数')
            self.missionLoopTimeExamlpeVar.set('15天后再重复的次数，默认为5      ')
            #
            self.missionMissionStateHintVar.set('是否完成')
            self.missionMissionStateExampleVar.set('0 代表未完成 1 代表完成     ')
            # error message
            self.wrongIdTitleVar.set('错误的id')
            self.wrongIdMessageVar.set('请输入正确的任务id（非数字）')
            #
            self.wrongNameTitleVar.set('错误的书名')
            self.wrongNameMessageVar.set('请输入正确的书名（空白的书名）')
            #
            self.wrongRangeTitleVar.set('错误的任务范围')
            self.wrongRangeMessageVar.set('请输入正确的任务范围（空白的任务范围）')
            #
            self.wrongStateTitleVar.set('错误的任务状态')
            self.wrongStateMessageVar.set('输入正确的任务状态编码（范围错误）')
            #
            self.wrongLoopTimeTitleVar.set('错误的迭代次数')
            self.wrongLoopTimeMessageVar.set('请输入正确的迭代次数（非数字）')
            #
            self.wrongFinishStateTitleVar.set('错误的完成状态')
            self.wrongFinishStateMessage1Var.set('输入正确的完成状态编码（范围错误）')
            self.wrongFinishStateMessage2Var.set('请输入正确的完成状态编码（非数字）')
            #
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

        self.missionId = tkinter.StringVar()
        self.bookName = tkinter.StringVar()
        self.missionRange = tkinter.StringVar()
        self.nextTime = tkinter.StringVar()
        self.state = tkinter.StringVar()
        self.loopTime = tkinter.StringVar()
        self.isFinish = tkinter.StringVar()

        def findMission(event):
            missionId = idEntry.get()
            missionDir = self.missionSystemTools.searchMission(missionId)
            self.bookName.set(missionDir['bookName'])
            self.missionRange.set(missionDir['missionRange'])
            self.nextTime.set(missionDir['nextTime'])
            self.state.set(missionDir['state'])
            self.loopTime.set(missionDir['loopTime'])
            self.isFinish.set(missionDir['isFinish'])
            pass

        # 任务id获取
        idLabel = tkinter.Label(self.addWindow, text=self.missionIdHintVar.get(), font=('Arial', 12), width=15, height=2)
        idLabel.place(x=-20, y=50, anchor='nw')

        idTLabel = tkinter.Label(self.addWindow, text=self.missionIdExampleVar.get(), font=('Arial', 8), width=30, height=1,
                                 foreground='DimGray', justify='left')
        idTLabel.place(x=70, y=85, anchor='nw')

        idEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        idEntry.place(x=100, y=55, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中,如果按下tab，则执行任务查找
        idEntry.bind('<KeyPress-Tab>', findMission)

        # 书名获取
        nameLabel = tkinter.Label(self.addWindow, text=self.missionNameHintVar.get(), font=('Arial', 12), width=15, height=2)
        nameLabel.place(x=-20, y=100, anchor='nw')

        # 空格是为了拉距离...
        nameTLabel = tkinter.Label(self.addWindow, text=self.missionNameExampleVar.get(), font=('Arial', 8), width=40, height=1,
                                   foreground='DimGray', justify='left')
        nameTLabel.place(x=60, y=135, anchor='nw')

        nameEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                  textvariable=self.bookName)
        nameEntry.place(x=100, y=105, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中
        nameEntry.bind('<ButtonPress-1>', findMission)

        # 任务范围获取
        missionRangeLabel = tkinter.Label(self.addWindow, text=self.missionRangeHintVar.get(), font=('Arial', 12), width=15, height=2)
        missionRangeLabel.place(x=-20, y=150, anchor='nw')

        missionRangeTLabel = tkinter.Label(self.addWindow, text= self.missionRangeExampleVar.get(), font=('Arial', 8), width=30,
                                           height=1,
                                           foreground='DimGray')
        missionRangeTLabel.place(x=70, y=185, anchor='nw')

        missionRangeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                          textvariable=self.missionRange)
        missionRangeEntry.place(x=100, y=155, anchor='nw')

        # 状态获取
        stateLabel = tkinter.Label(self.addWindow, text=self.missionStateHintVar.get(), font=('Arial', 12), width=15, height=2)
        stateLabel.place(x=-20, y=200, anchor='nw')

        # 空格为为了拉gui显示的距离
        stateTLabel = tkinter.Label(self.addWindow,
                                    text=self.missionStateExampleVar.get(),
                                    font=('Arial', 8), width=50, height=3,
                                    foreground='DimGray', justify='left')
        stateTLabel.place(x=35, y=235, anchor='nw')

        stateEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                   textvariable=self.state)
        stateEntry.place(x=100, y=205, anchor='nw')

        # 循环次数获取
        loopTimeLabel = tkinter.Label(self.addWindow, text=self.missionLoopTimeHintVar.get(), font=('Arial', 12), width=15, height=2)
        loopTimeLabel.place(x=-20, y=280, anchor='nw')

        loopTimeTLabel = tkinter.Label(self.addWindow, text=self.missionLoopTimeExamlpeVar.get(), font=('Arial', 8), width=35,
                                       height=1,
                                       foreground='DimGray')
        loopTimeTLabel.place(x=70, y=315, anchor='nw')

        loopTimeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                      textvariable=self.loopTime)
        loopTimeEntry.place(x=100, y=285, anchor='nw')

        # 完成状态获取
        isFinishLabel = tkinter.Label(self.addWindow, text= self.missionMissionStateHintVar.get(), font=('Arial', 12), width=15, height=2)
        isFinishLabel.place(x=-20, y=330, anchor='nw')

        isFinishTLabel = tkinter.Label(self.addWindow, text=self.missionMissionStateExampleVar.get(), font=('Arial', 8), width=30,
                                       height=1,
                                       foreground='DimGray')
        isFinishTLabel.place(x=80, y=365, anchor='nw')

        isFinishEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                      textvariable=self.isFinish)
        isFinishEntry.place(x=100, y=335, anchor='nw')

        def editMission():
            """
            确认添加按钮的事件
            :return:
            """

            # 输入的任务id检查
            id = idEntry.get()
            try:
                id = int(idEntry.get())
            except:
                messagebox.showwarning(title=self.wrongIdTitleVar.get(), message=self.wrongIdMessageVar.get())
                return
            # 书名检查
            if self.bookName.get() is '':
                messagebox.showwarning(title=self.wrongNameTitleVar.get(), message=self.wrongNameMessageVar.get())
                return
            # 任务范围检查
            if self.missionRange.get() is '':
                messagebox.showwarning(title=self.wrongRangeTitleVar.get(), message=self.wrongRangeMessageVar.get())
                return
            # 任务状态检查
            state = self.state.get()
            try:
                state = int(self.state.get())
                if state > 7 or state < 0:
                    messagebox.showwarning(title=self.wrongStateTitleVar.get(), message=self.wrongStateMessageVar.get())
                    return
            except:
                messagebox.showwarning(title=self.wrongStateTitleVar.get(), message=self.wrongStateMessageVar.get())
                return
            # 输入的迭代次数检查
            time = self.loopTime.get()
            try:
                time = int(self.loopTime.get())
            except:
                messagebox.showwarning(title=self.wrongLoopTimeTitleVar.get(), message=self.wrongLoopTimeMessageVar.get())
                return
            # 完成状态检查
            finish = self.isFinish.get()
            try:
                finish = int(self.isFinish.get())
                if finish != 1 and finish != 0:
                    messagebox.showwarning(title=self.wrongFinishStateTitleVar.get(), message=self.wrongFinishStateMessage1Var.get())
                    return
            except:
                messagebox.showwarning(title=self.wrongFinishStateTitleVar.get(), message=self.wrongFinishStateMessage2Var.get())
                return
            # 用户再次确认
            if messagebox.askokcancel(title=self.ifGoOnTitleVar.get(), message=self.ifGoOnMessageVar.get()):
                # 调用添加任务工具
                self.missionSystemTools.editMission(missionId=id, bookName=self.bookName.get(),
                                                    missionRange=self.missionRange.get(),
                                                    state=state, loopTime=time,
                                                    isEdit=True)
                if finish == 1:
                    self.missionSystemTools.editMission(missionId=idEntry.get(), isFinish=True)
                # 关闭窗口
                self.addWindow.after(300, self.addWindow.destroy)
                # 将messageFrame的重绘变量置为True
                messageFrame.MessageFrame.needReprint = True
                #记录用户操作
                self.logUserAction('user click edit mission button')
                if DEBUG and VIEW_DEBUG:
                    print('{USR}{MESSAGE_FRAME} now user click edit mission button')

        # 按钮
        addButton = tkinter.Button(self.addWindow, text=self.editButtonVar.get(), command=editMission, width=8)
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
