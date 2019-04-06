# -*- coding:utf-8 -*-
from src.Client.Conf.config import *

from src.Client.SearchSystem import searchSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSearchResultTools import showMission, showWord
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools import showEdit


class SearchFrame():
    """
    搜索子系统，负责调用任务模块以及非法数据的过滤与提示。
    """

    def __init__(self, rootFrame):
        # 添加顶部框架
        if DEBUG:
            topFrame = tkinter.Frame(rootFrame, height=50, width=700, bg='lightPink')
        else:
            topFrame = tkinter.Frame(rootFrame, height=50, width=700)

        topFrame.place(x=0, y=0, anchor='nw')

        errorTitleVar = tkinter.StringVar()
        errorMessageVar = tkinter.StringVar()
        searchButtonVar = tkinter.StringVar()
        settingButtonVar = tkinter.StringVar()
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            errorTitleVar.set('错误的单词')
            errorMessageVar.set('无法解析该单词，请检查拼写')
            searchButtonVar.set('搜索')
            settingButtonVar.set('设置')
        elif languageType == 'EN':
            errorTitleVar.set('wrong word')
            errorMessageVar.set("The word can't be found.Please check the spelling")
            searchButtonVar.set('search')
            settingButtonVar.set('setting')
        else:
            errorTitleVar.set('错误的单词')
            errorMessageVar.set('无法解析该单词，请检查拼写')
            searchButtonVar.set('搜索')
            settingButtonVar.set('设置')


        def searchButtonHandle():
            """
             定义搜索按钮事件（按钮点击的事件）
            :return:
            """
            searchText = searchBox.get().encode('utf-8')
            if searchText == '':
                return
            # 调用用户操作记录函数，记录用户此次操作
            self.logUserAction('search button has been click,and the search text is', searchText)
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG}search button has been click,and the search text is ' + searchText)
            result, isWord = searchSystem.SearchSystem().search(searchText)
            # 处理子系统无法解析单词，返回的None标记，继续向用户进行反馈
            if result is None:
                messagebox.showwarning(title=errorTitleVar.get(), message=errorMessageVar.get())
            else:
                # 窗口显示单词信息或者任务信息
                if isWord:
                    showWord.ShowWord().window(result)
                else:
                    showMission.ShowMission().window(result)

        def enterSearch(event):
            """
             定义搜索按钮事件（回车的事件）
            :param event:
            :return:
            """
            searchText = searchBox.get().encode('utf-8')
            if searchText == '':
                return
            # 调用用户操作记录函数，记录用户此次操作
            self.logUserAction('search button has been click,and the search text is', searchText)
            # 打印debug日志
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG}search button has been click,and the search text is ' + searchText)

            # 调用搜索子系统
            result, isWord = searchSystem.SearchSystem().search(searchText)
            # 处理子系统无法解析单词，返回的None标记，继续向用户进行反馈
            if result is None:
                messagebox.showwarning(title=errorTitleVar.get(), message=errorMessageVar.get())
            else:
                # 窗口显示单词信息或者任务信息
                if isWord:
                    showWord.ShowWord().window(result)
                else:
                    showMission.ShowMission().window(result)

        def settingHandle():
            """
            定义点击设置按钮后的动作
            :return:
            """
            # 打印debug日志
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG}setting button has been click')
            showEdit.ShowEdit().window()

            pass

        # 添加搜索栏
        searchBox = tkinter.Entry(topFrame, font=('Arial', 12), width=35, bd=5, relief='flat')
        searchBox.place(x=130, y=10, anchor='nw')
        # 绑定回车事件
        searchBox.bind("<KeyPress-Return>", enterSearch)

        # 添加搜索按钮
        searchImage = tkinter.PhotoImage(file="./images/search.gif")
        # searchButton = tkinter.Button(topFrame, image=searchImage, command=searchButtonHandle)
        searchButton = tkinter.Button(topFrame, text=searchButtonVar.get(), command=searchButtonHandle)
        searchButton.place(x=470, y=8.5, anchor='nw')

        # 添加设置按钮
        settingImage = tkinter.PhotoImage(file="./images/search.gif")
        # settingButton = tkinter.Button(topFrame, image=settingImage, command=settingHandle)
        settingButton = tkinter.Button(topFrame, text=settingButtonVar.get(), command=settingHandle)
        settingButton.place(x=640, y=8.5, anchor='nw')

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
