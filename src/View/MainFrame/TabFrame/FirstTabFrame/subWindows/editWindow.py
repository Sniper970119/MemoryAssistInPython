# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.MissionSystem import missionSystem
from src.View.MainFrame.TabFrame.FirstTabFrame import messageFrame


class EditWindow():
    def __init__(self):
        self.missionSystemTools = missionSystem.MissionSystem()

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '300x430+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 430) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title('编辑任务')
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
        idLabel = tkinter.Label(self.addWindow, text='任务id', font=('Arial', 12), width=15, height=2)
        idLabel.place(x=-30, y=50, anchor='nw')

        idTLabel = tkinter.Label(self.addWindow, text='例如：输入 000001 或者 1', font=('Arial', 8), width=30, height=1,
                                 foreground='DimGray', justify='left')
        idTLabel.place(x=55, y=85, anchor='nw')

        idEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat')
        idEntry.place(x=80, y=55, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中,如果按下tab，则执行任务查找
        idEntry.bind('<KeyPress-Tab>', findMission)

        # 书名获取
        nameLabel = tkinter.Label(self.addWindow, text='书名', font=('Arial', 12), width=15, height=2)
        nameLabel.place(x=-30, y=100, anchor='nw')

        # 空格是为了拉距离...
        nameTLabel = tkinter.Label(self.addWindow, text='背的书名（记得先把任务 id 填了哦~）', font=('Arial', 8), width=40, height=1,
                                   foreground='DimGray', justify='left')
        nameTLabel.place(x=55, y=135, anchor='nw')

        nameEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                  textvariable=self.bookName)
        nameEntry.place(x=80, y=105, anchor='nw')

        # 这里是用上一步获取到的id 提前查任务信息，填到entry中
        nameEntry.bind('<ButtonPress-1>', findMission)

        # 任务范围获取
        missionRangeLabel = tkinter.Label(self.addWindow, text='任务范围', font=('Arial', 12), width=15, height=2)
        missionRangeLabel.place(x=-30, y=150, anchor='nw')

        missionRangeTLabel = tkinter.Label(self.addWindow, text='输入任务范围 例如：p1~p6', font=('Arial', 8), width=30,
                                           height=1,
                                           foreground='DimGray')
        missionRangeTLabel.place(x=55, y=185, anchor='nw')

        missionRangeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                          textvariable=self.missionRange)
        missionRangeEntry.place(x=80, y=155, anchor='nw')

        # 状态获取
        stateLabel = tkinter.Label(self.addWindow, text='状态代码', font=('Arial', 12), width=15, height=2)
        stateLabel.place(x=-30, y=200, anchor='nw')

        # 空格为为了拉gui显示的距离
        stateTLabel = tkinter.Label(self.addWindow,
                                    text='0，1，2，3，4，5，6，7 分别为不再提示、          \n当天、次日、两天后、四天后、                               \n七天后、十五天后、和循环记忆                                 ',
                                    font=('Arial', 8), width=50, height=3,
                                    foreground='DimGray', justify='left')
        stateTLabel.place(x=55, y=235, anchor='nw')

        stateEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                   textvariable=self.state)
        stateEntry.place(x=80, y=205, anchor='nw')

        # 循环次数获取
        loopTimeLabel = tkinter.Label(self.addWindow, text='循环次数', font=('Arial', 12), width=15, height=2)
        loopTimeLabel.place(x=-30, y=280, anchor='nw')

        loopTimeTLabel = tkinter.Label(self.addWindow, text='15天后再重复的次数，默认为5      ', font=('Arial', 8), width=35,
                                       height=1,
                                       foreground='DimGray')
        loopTimeTLabel.place(x=55, y=315, anchor='nw')

        loopTimeEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                      textvariable=self.loopTime)
        loopTimeEntry.place(x=80, y=285, anchor='nw')

        # 完成状态获取
        isFinishLabel = tkinter.Label(self.addWindow, text='是否完成', font=('Arial', 12), width=15, height=2)
        isFinishLabel.place(x=-30, y=330, anchor='nw')

        isFinishTLabel = tkinter.Label(self.addWindow, text='0 代表未完成 1 代表完成     ', font=('Arial', 8), width=30,
                                       height=1,
                                       foreground='DimGray')
        isFinishTLabel.place(x=55, y=365, anchor='nw')

        isFinishEntry = tkinter.Entry(self.addWindow, font=('Arial', 12), width=15, bd=5, relief='flat',
                                      textvariable=self.isFinish)
        isFinishEntry.place(x=80, y=335, anchor='nw')

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
                messagebox.showwarning(title='错误的id', message='请输入正确的任务id（非数字）')
                return
            # 书名检查
            if self.bookName.get() is '':
                messagebox.showwarning(title='错误的书名', message='请输入正确的书名（空白的书名）')
                return
            # 任务范围检查
            if self.missionRange.get() is '':
                messagebox.showwarning(title='错误的任务范围', message='请输入正确的任务范围（空白的任务范围）')
                return
            # 任务状态检查
            state = self.state.get()
            try:
                state = int(self.state.get())
                if state > 7 or state < 0:
                    messagebox.showwarning(title='错误的任务状态', message='输入正确的任务状态编码（范围错误）')
                    return
            except:
                messagebox.showwarning(title='错误的任务状态', message='请输入正确的任务状态编码（非数字）')
                return
            # 输入的迭代次数检查
            time = self.loopTime.get()
            try:
                time = int(self.loopTime.get())
            except:
                messagebox.showwarning(title='错误的迭代次数', message='请输入正确的迭代次数（非数字）')
                return
            # 完成状态检查
            finish = self.isFinish.get()
            try:
                finish = int(self.isFinish.get())
                if finish != 1 and finish != 0:
                    messagebox.showwarning(title='错误的完成状态', message='输入正确的完成状态编码（范围错误）')
                    return
            except:
                messagebox.showwarning(title='错误的完成状态', message='请输入正确的完成状态（非数字）')
                return
            # 用户再次确认
            if messagebox.askokcancel(title='是否继续编辑', message='确认后不可恢复，确认信息正确有效'):
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
        addButton = tkinter.Button(self.addWindow, text='确认修改', command=editMission)
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
