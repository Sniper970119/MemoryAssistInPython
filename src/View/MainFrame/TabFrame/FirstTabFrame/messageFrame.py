# -*- coding:utf-8 -*-

from src.conf.config import *


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
        self.tree = ttk.Treeview(self.messageFrame, columns=['1', '2', '3', '4', '5'], show='headings', height=18)
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
                print('{VIEW_DEBUG}{MESSAGE_FRAME} treeview has been double click at ' + item_text[0])
        isFinish = tkinter.messagebox.askyesno(title='完成任务', message='已完成当前任务')
        if isFinish:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                self.removeData(item_text[0])
            pass
        if DEBUG:
            print('{VIEW_DEBUG}{MESSAGE_FRAME} user select ' + str(isFinish))
        pass

    def removeData(self, id):
        """
        从treeview中移除id
        :param id: 需要被移除的id
        :return:
        """
        if DEBUG:
            print('{VIEW_DEBUG}{MESSAGE_FRAME} current delete id is ' + id)
        # 先删除所有点
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        for each in self.dataList:
            if each['任务id'] != id:
                # 转换成列表，方便插入treeview
                dataInList = [each['任务id'], each['书名'], each['任务范围'], each['任务进度'], each['下次任务']]
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
                    '任务id': str(i).zfill(4),
                    '书名': 'book' + str(i).zfill(2),
                    '任务范围': 'mission' + str(i).zfill(2),
                    '任务进度': 'state' + str(i).zfill(2),
                    '下次任务': 'nextData' + str(i).zfill(2)
                }
                self.dataList.append(dir)
            for li in self.dataList:
                # 转换成列表，方便插入treeview
                dataInList = [li['任务id'], li['书名'], li['任务范围'], li['任务进度'], li['下次任务']]
                self.tree.insert('', 'end', values=dataInList)

