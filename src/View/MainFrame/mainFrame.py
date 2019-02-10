# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.View.MainFrame.TabFrame import tabFrame


class MainFrame():
    def __init__(self):
        # 添加主页面
        rootWindow = tkinter.Tk()
        screenWidth = rootWindow.winfo_screenwidth()
        screenHeight = rootWindow.winfo_screenheight()
        rootWindow.geometry('700x500+' + str(int((screenWidth - 700) / 2)) + '+' + str(int((screenHeight - 500) / 2)))
        rootWindow.resizable(width=False, height=False)
        rootWindow.title('MemoryAssist v0.1')
        rootWindow.iconbitmap('images/icon.ico')

        # 添加主框架
        if DEBUG and VIEW_DEBUG:
            rootFrame = tkinter.Frame(rootWindow, height=500, width=700, bg='red')
        else:
            rootFrame = tkinter.Frame(rootWindow, height=500, width=700)

        rootFrame.place(x=0, y=0, anchor='nw')

        # 调用子组件
        tabFrame.TabFrame(rootFrame=rootFrame)

        rootWindow.mainloop()
