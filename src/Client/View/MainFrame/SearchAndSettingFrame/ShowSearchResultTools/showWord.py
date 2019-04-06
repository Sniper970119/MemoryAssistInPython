# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead


class ShowWord():
    """
    搜索栏显示查词结果的GUi部分
    """
    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.searchWordVar = tkinter.StringVar()
        self.wordSpellVar = tkinter.StringVar()
        self.wordTranslateVar = tkinter.StringVar()
        self.wordExampleVar = tkinter.StringVar()
        self.languageType = None
        self.language()
        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        这里由于编码问题，下面依然采用单独判断，没有使用tkString
        :return:
        """

        self.languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if self.languageType == 'CN':
            self.windowTitleVar.set('单词详情')
            self.searchWordVar.set('原词： ')
            self.wordSpellVar.set('音标拼音： ')
            self.wordTranslateVar.set('翻译： ')
            self.wordExampleVar.set('例句： ')
        elif self.languageType == 'EN':
            self.windowTitleVar.set('word detail')
            self.searchWordVar.set('word: ')
            self.wordSpellVar.set('phonetic/spell: ')
            self.wordTranslateVar.set('translation: ')
            self.wordExampleVar.set('example: ')
        else:
            self.windowTitleVar.set('单词详情')
            self.searchWordVar.set('原词： ')
            self.wordSpellVar.set('音标/拼音：')
            self.wordTranslateVar.set('翻译： ')
            self.wordExampleVar.set('例句： ')

    def window(self, result):
        showWindow = tkinter.Toplevel()
        screenWidth = showWindow.winfo_screenwidth()
        screenHeight = showWindow.winfo_screenheight()
        showWindow.geometry(
            '300x300+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 300) / 2)))
        showWindow.resizable(width=False, height=False)
        showWindow.title(self.windowTitleVar.get())
        showWindow.iconbitmap('images/icon.ico')

        # 显示单词
        showWord = self.searchWordVar.get() + str(result['word'].encode('utf-8'))
        wordLabel = tkinter.Label(showWindow, text=showWord)
        wordLabel.place(x=30, y=20, anchor='nw')

        # 显示音标/拼音
        if self.languageType == 'CN':
            showPron = '音标/拼音： ' + str(result['pron'].encode('utf-8'))
        elif self.languageType == 'EN':
            showPron = 'phonetic/spell: ' + str(result['pron'].encode('utf-8'))
        else:
            showPron = '音标/拼音： ' + str(result['pron'].encode('utf-8'))
        pronLabel = tkinter.Label(showWindow, text=showPron)
        pronLabel.place(x=30, y=50, anchor='nw')

        # 显示翻译
        if self.languageType == 'CN':
            showTranslation = '翻译： ' + str(result['translation'].encode('utf-8'))
        elif self.languageType == 'EN':
            showTranslation = 'translate: ' + str(result['translation'].encode('utf-8'))
        else:
            showTranslation = '翻译： ' + str(result['translation'].encode('utf-8'))
        translationLabel = tkinter.Label(showWindow, text=showTranslation)
        translationLabel.place(x=30, y=80, anchor='nw')

        # 显示例句
        if self.languageType == 'CN':
            showEg = '例句：'
        elif self.languageType == 'EN':
            showEg = 'example: '
        else:
            showEg = "例句："
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
