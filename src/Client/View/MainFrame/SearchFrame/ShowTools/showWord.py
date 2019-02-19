# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class ShowWord():
    """
    搜索栏显示查词结果的GUi部分
    """
    def __init__(self):
        pass

    def window(self, result):
        showWindow = tkinter.Toplevel()
        screenWidth = showWindow.winfo_screenwidth()
        screenHeight = showWindow.winfo_screenheight()
        showWindow.geometry(
            '300x300+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 300) / 2)))
        showWindow.resizable(width=False, height=False)
        showWindow.title('单词详情')
        showWindow.iconbitmap('images/icon.ico')

        # 显示单词
        showWord = '原词： ' + str(result['word'].encode('utf-8'))
        wordLabel = tkinter.Label(showWindow, text=showWord)
        wordLabel.place(x=30, y=20, anchor='nw')

        # 显示音标/拼音
        showPron = '音标/拼音： ' + str(result['pron'].encode('utf-8'))
        pronLabel = tkinter.Label(showWindow, text=showPron)
        pronLabel.place(x=30, y=50, anchor='nw')

        # 显示翻译
        showTranslation = '翻译： ' + str(result['translation'].encode('utf-8'))
        translationLabel = tkinter.Label(showWindow, text=showTranslation)
        translationLabel.place(x=30, y=80, anchor='nw')

        # 显示例句
        showEg = '例句： '
        egLabel = tkinter.Label(showWindow, text=showEg)
        egLabel.place(x=30, y=110, anchor='nw')

        # 显示例句
        showFirstOrig = result['sentenceOneOrig']
        firstOrigLabel = tkinter.Label(showWindow, text=showFirstOrig, wraplength=220, justify='left', height=2)
        firstOrigLabel.place(x=50, y=140, anchor='nw')

        # 显示例句
        showFirstTrans = result['sentenceOneTrans']
        firstTransLabel = tkinter.Label(showWindow, text=showFirstTrans)
        firstTransLabel.place(x=50, y=185, anchor='nw')

        # 显示例句
        showSecondOrig = result['sentenceTwoOrig']
        secondOrigLabel = tkinter.Label(showWindow, text=showSecondOrig, wraplength=220, justify='left', height=2)
        secondOrigLabel.place(x=50, y=215, anchor='nw')

        # 显示例句
        showSecondOrig = result['sentenceTwoTrans']
        secondTransLabel = tkinter.Label(showWindow, text=showSecondOrig)
        secondTransLabel.place(x=50, y=260, anchor='nw')
        pass
