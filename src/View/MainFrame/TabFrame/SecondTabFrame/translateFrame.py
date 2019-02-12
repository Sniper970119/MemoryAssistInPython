# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.TranslateSystem.Tools import translateInBaidu


class TranslateFrame():

    def __init__(self, tab):
        """

        :param tab: tab 为当前frame的父容器
        """
        if DEBUG and VIEW_DEBUG:
            self.secondTabFrame = tkinter.Frame(tab, height=350, width=700, bg='plum')
        else:
            self.secondTabFrame = tkinter.Frame(tab, height=350, width=700)

        self.secondTabFrame.place(x=0, y=30, anchor='nw')

        self.printInputText()

        self.printOutputText()

        self.printTanlateButton()

        tab.add(self.secondTabFrame, text='文本翻译')

    def printInputText(self):
        self.inputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('黑体', 16))
        self.inputText.place(x=60, y=30, anchor='nw')

    def printOutputText(self):
        self.outputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('黑体', 16))
        self.outputText.config(state='disabled')
        self.outputText.place(x=60, y=200, anchor='nw')

    def printTanlateButton(self):
        def translateText():
            text = self.inputText.get("0.0", "end").encode('utf-8')
            if text == '':
                return
            translateResult = translateInBaidu.Translate().translate(text)
            self.outputText.config(state='normal')
            self.outputText.delete('1.0', 'end')
            self.outputText.insert('insert', translateResult)
            self.outputText.config(state='disabled')

        def autoTranslate(event):
            translateText()

        def changeLine(event):
            # self.inputText.insert('insert', '\n')
            pass

        def selectText(event):
            self.inputText.tag_add(tkinter.SEL, "1.0", tkinter.END)
            return 'break'

        translateButton = tkinter.Button(self.secondTabFrame, text='翻 译', bg='red', width=7,
                                         activebackground='firebrick', fg='ghostwhite', activeforeground='ghostwhite',
                                         command=translateText)
        self.inputText.bind("<Shift-Return>", changeLine)
        self.inputText.bind("<Return>", autoTranslate)
        self.inputText.bind("<Control-Key-a>", selectText)
        self.inputText.bind("<Control-Key-A>", selectText)
        translateButton.place(x=620, y=120, anchor='nw')

        def copyToShearPlate():
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            # 这里因为编码问题，用来debug展示的字符编码和复制到剪切板的字符编码不一样，所以分来
            translateResultUseToShow = self.outputText.get("0.0", "end").encode('utf-8')
            # 这里去掉text默认的最后一个的换行符，使剪切板的文本为用户需要翻译的准确翻译
            translateResultUseToCopy = self.outputText.get("0.0", "end")[:-1].encode('gbk')
            win32clipboard.SetClipboardData(win32con.CF_TEXT, translateResultUseToCopy)
            win32clipboard.CloseClipboard()
            pass

        copyToShearPlateButton = tkinter.Button(self.secondTabFrame, text='复 制', bg='red', width=7,
                                                activebackground='firebrick', fg='ghostwhite',
                                                activeforeground='ghostwhite',
                                                command=copyToShearPlate)
        copyToShearPlateButton.place(x=620, y=290, anchor='nw')
