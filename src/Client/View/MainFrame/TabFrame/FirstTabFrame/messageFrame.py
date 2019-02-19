# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.MissionSystem import missionSystem


class MessageFrame():
    """
    负责显示 显示当日任务信息的GUI界面，以及用户完成任务信息的响应。
    """
    def __init__(self, firstTabFrame=None):
        """

        :param firstTabFrame: 当前Frame的父容器
        """
        self.missionSystemTools = missionSystem.MissionSystem()
        # 初始化框架
        if DEBUG and VIEW_DEBUG:
            self.messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600, bg='yellow')
        else:
            self.messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600)

        self.messageFrame.place(x=0, y=00, anchor='nw')

        # 初始化框架内容
        self.dataList = []
        self.tree = ttk.Treeview(self.messageFrame, columns=['1', '2', '3', '4', '5'], show='headings', height=17)
        # 绘制表格
        self.printMessage()
        # 调用心跳线程更新
        self.threadUpdate()
        MessageFrame.needReprint = False

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
        isFinish = tkinter.messagebox.askyesno(title='完成任务', message='已完成当前任务')
        if isFinish:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                # 调用用户操作记录函数，记录用户此次操作
                self.logUserAction('treeview has been double click at ', item_text[0])
                # 标记任务已完成
                missionSystem.MissionSystem().editMission(missionId=item_text[0], isFinish=True)
                self.removeData(item_text[0])
            pass
        # 调用用户操作记录函数，记录用户此次操作
        self.logUserAction('user select  ', str(isFinish))
        if DEBUG and VIEW_DEBUG:
            print('{USR}{VIEW_DEBUG} user select ' + str(isFinish))
        pass

    def removeData(self, id):
        """
        从treeview中移除id
        :param id: 需要被移除的id
        :return:
        """
        if DEBUG and VIEW_DEBUG:
            print('{SYS}{MESSAGE_FRAME} current remove from treeview id is ' + id)
        # 先删除所有点
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for each in self.dataList:
            if each['missionId'] != id:
                # 转换成列表，方便插入treeview
                dataInList = [each['missionId'], each['bookName'], each['missionRange'], each['state'],
                              each['nextTime']]
                self.tree.insert('', 'end', values=dataInList)

    def updataData(self):
        """
        从treeview更新
        :return:
        """
        while (True):
            # 心跳线程每隔一秒检查是否需要重绘
            time.sleep(1)
            if MessageFrame.needReprint:
                # 将重绘标记置False
                MessageFrame.needReprint = False
                # 读取任务列表
                self.getList()
                if DEBUG and VIEW_DEBUG:
                    print('{SYS}{MESSAGE_FRAME} reprint treeview')
                # 先删除所有点
                x = self.tree.get_children()
                for item in x:
                    self.tree.delete(item)
                for each in self.dataList:
                    dataInList = [each['missionId'], each['bookName'], each['missionRange'], each['state'],
                                  each['nextTime']]
                    self.tree.insert('', 'end', values=dataInList)

    def printMessage(self):
        """
        主绘制函数，负责绘制treeview
        :return:
        """
        self.tree.column('1', width=110, anchor='center')
        self.tree.column('2', width=110, anchor='center')
        self.tree.column('3', width=110, anchor='center')
        self.tree.column('4', width=110, anchor='center')
        self.tree.column('5', width=110, anchor='center')
        self.tree.heading('1', text='任务id')
        self.tree.heading('2', text='书名')
        self.tree.heading('3', text='任务范围')
        self.tree.heading('4', text='任务进度')
        self.tree.heading('5', text='下次任务')
        self.tree.place(x=0, y=0, anchor='nw')
        self.tree.bind("<Double-Button-1>", self.treeviewClick)
        self.getList()

    def getList(self):
        self.dataList = missionSystem.MissionSystem().todayMission
        for li in self.dataList:
            # 转换成列表，方便插入treeview
            dataInList = [li['missionId'], li['bookName'], li['missionRange'], li['state'], li['nextTime']]
            self.tree.insert('', 'end', values=dataInList)

        # 向表格中添加测试数据
        if DEBUG and VIEW_DEBUG:
            pass

    def threadUpdate(self):
        t = threading.Thread(target=self.updataData)
        t.setDaemon(True)  # 设置为守护线程
        if DEBUG and VIEW_DEBUG:
            print('{SYS}{MISSION_DEBUG} update thread has been ran')
        t.start()

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
