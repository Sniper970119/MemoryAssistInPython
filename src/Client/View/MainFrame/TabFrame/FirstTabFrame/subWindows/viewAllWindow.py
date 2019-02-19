# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.MissionSystem import missionSystem


class ViewAllWindow():
    """
    显示全部任务的GUI界面
    """
    def __init__(self):
        self.missionSystemTools = missionSystem.MissionSystem()

    def window(self):
        self.addWindow = tkinter.Toplevel()
        screenWidth = self.addWindow.winfo_screenwidth()
        screenHeight = self.addWindow.winfo_screenheight()
        self.addWindow.geometry(
            '550x320+' + str(int((screenWidth - 550) / 2)) + '+' + str(int((screenHeight - 320) / 2)))
        self.addWindow.resizable(width=False, height=False)
        self.addWindow.title('查看全部')
        self.addWindow.iconbitmap('images/icon.ico')
        self.tree = ttk.Treeview(self.addWindow, columns=['1', '2', '3', '4', '5', '6', '7'], show='headings',
                                 height=15)

        self.tree.column('1', width=80, anchor='center')
        self.tree.column('2', width=80, anchor='center')
        self.tree.column('3', width=80, anchor='center')
        self.tree.column('4', width=80, anchor='center')
        self.tree.column('5', width=80, anchor='center')
        self.tree.column('6', width=80, anchor='center')
        self.tree.column('7', width=80, anchor='center')
        self.tree.heading('1', text='任务id')
        self.tree.heading('2', text='书名')
        self.tree.heading('3', text='任务范围')
        self.tree.heading('4', text='任务进度')
        self.tree.heading('5', text='下次任务')
        self.tree.heading('6', text='循环次数')
        self.tree.heading('7', text='是否完成')
        self.tree.place(x=0, y=0, anchor='nw')
        list = missionSystem.MissionSystem().loadMission()
        for each in list:
            dataInList = [each['missionId'], each['bookName'], each['missionRange'], each['state'], each['nextTime'],
                          each['loopTime'], each['isFinish']]
            self.tree.insert('', 'end', values=dataInList)
