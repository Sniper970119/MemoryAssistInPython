# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.View.MainFrame.TabFrame import tabFrame
from src.Client.View.MainFrame.SearchFrame import searchFrame


class MainFrame():
    def __init__(self):
        # 添加主页面
        rootWindow = tkinter.Tk()
        screenWidth = rootWindow.winfo_screenwidth()
        screenHeight = rootWindow.winfo_screenheight()
        rootWindow.geometry('700x500+' + str(int((screenWidth - 700) / 2)) + '+' + str(int((screenHeight - 500) / 2)))
        rootWindow.resizable(width=False, height=False)
        rootWindow.title('MemoryAssist v1.0')
        rootWindow.iconbitmap('images/icon.ico')

        # 添加主框架
        if DEBUG and VIEW_DEBUG:
            rootFrame = tkinter.Frame(rootWindow, height=500, width=700, bg='red')
        else:
            rootFrame = tkinter.Frame(rootWindow, height=500, width=700)

        rootFrame.place(x=0, y=0, anchor='nw')

        # 调用子组件
        tabFrame.TabFrame(rootFrame=rootFrame)
        searchFrame.SearchFrame(rootFrame=rootFrame)

        rootWindow.mainloop()
