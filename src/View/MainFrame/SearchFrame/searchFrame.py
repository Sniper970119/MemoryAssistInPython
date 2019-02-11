# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.SearchSystem import searchSystem
from src.View.MainFrame.SearchFrame.ShowTools import showWord
from src.View.MainFrame.SearchFrame.ShowTools import showMission


class SearchFrame():
    def __init__(self, rootFrame):
        # 添加顶部框架
        if DEBUG:
            topFrame = tkinter.Frame(rootFrame, height=50, width=700, bg='lightPink')
        else:
            topFrame = tkinter.Frame(rootFrame, height=50, width=700)

        topFrame.place(x=0, y=0, anchor='nw')

        # 定义搜索按钮事件（按钮点击的事件）
        def searchButtonHandle():
            searchText = searchBox.get().encode('utf-8')
            if searchText == '':
                return
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG}search button has been click,and the search text is ' + searchText)
            result, isWord = searchSystem.SearchSystem().search(searchText)
            if isWord:
                showWord.ShowWord().window(result)
            else:
                showMission.ShowMission().window(result)

        # 定义搜索按钮事件（回车的事件）
        def enterSearch(event):
            searchText = searchBox.get().encode('utf-8')
            if searchText == '':
                return
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG}search button has been click,and the search text is ' + searchText)
            result, isWord = searchSystem.SearchSystem().search(searchText)
            if isWord:
                showWord.ShowWord().window(result)
                pass
            else:
                showMission.ShowMission().window(result)
                pass

        # 添加搜索栏
        searchBox = tkinter.Entry(topFrame, font=('Arial', 12), width=35, bd=5, relief='flat')
        searchBox.place(x=130, y=10, anchor='nw')
        # 绑定回车事件
        searchBox.bind("<KeyPress-Return>", enterSearch)

        # 添加搜索按钮
        searchImage = tkinter.PhotoImage(file="./images/search.gif")
        # searchButton = tkinter.Button(topFrame, image=searchImage, command=searchButtonHadle)
        searchButton = tkinter.Button(topFrame, text='搜索', command=searchButtonHandle)
        searchButton.place(x=470, y=8.5, anchor='nw')
