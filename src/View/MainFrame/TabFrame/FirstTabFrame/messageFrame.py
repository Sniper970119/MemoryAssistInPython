# -*- coding:utf-8 -*-

from src.Conf.config import *


class MessageFrame():

    def __init__(self, firstTabFrame):
        """

        :param firstTabFrame: 当前Frame的父容器
        """
        # 初始化框架
        if DEBUG and VIEW_DEBUG:
            self.messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600, bg='yellow')
        else:
            self.messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600)

        self.messageFrame.place(x=0, y=00, anchor='nw')

        # 初始化框架内容
        self.dataList = []
        self.tree = ttk.Treeview(self.messageFrame, columns=['1', '2', '3', '4', '5'], show='headings', height=15)
        # 绘制表格
        self.printMessage()

    # 定义鼠标双击事件
    def treeviewClick(self, event):
        """
        定义鼠标在treeview上的双击事件
        :param event:
        :return:
        """
        if DEBUG:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                print('{USR}{VIEW_DEBUG} treeview has been double click at ' + item_text[0])
        isFinish = tkinter.messagebox.askyesno(title='完成任务', message='已完成当前任务')
        if isFinish:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                self.removeData(item_text[0])
            pass
        if DEBUG:
            print('{USR}{VIEW_DEBUG} user select ' + str(isFinish))
        pass

    def removeData(self, id):
        """
        从treeview中移除id
        :param id: 需要被移除的id
        :return:
        """
        if DEBUG:
            print('{SYS}{MESSAGE_FRAME} current delete id is ' + id)
        # 先删除所有点
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for each in self.dataList:
            if each['missionId'] != id:
                # 转换成列表，方便插入treeview
                dataInList = [each['missionId'], each['bookName'], each['missionRange'], each['missionState'],
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

        # 向表格中添加测试数据
        if DEBUG:
            for i in range(1, 21):
                # 先封装成字典，方便后期删除
                dir = {
                    'missionId': str(i).zfill(4),
                    'bookName': 'bookName' + str(i).zfill(2),
                    'missionRange': 'missionRange' + str(i).zfill(2),
                    'nextTime': 'nextTime' + str(i).zfill(2),
                    'missionState': 'state' + str(i).zfill(2),
                    'loopTime': 5,
                    'isFinish': False
                }
                self.dataList.append(dir)
            print(len(self.dataList))
            for li in self.dataList:
                # 转换成列表，方便插入treeview
                dataInList = [li['missionId'], li['bookName'], li['missionRange'], li['missionState'], li['nextTime']]
                self.tree.insert('', 'end', values=dataInList)
