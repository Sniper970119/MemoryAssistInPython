# -*- coding:utf-8 -*-
from src.Conf.config import *


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
        inputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('Arial', 16))
        inputText.place(x=60, y=30, anchor='nw')

    def printOutputText(self):
        outputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('Arial', 16))
        outputText.place(x=60, y=200, anchor='nw')

    def printTanlateButton(self):
        translateButton = tkinter.Button(self.secondTabFrame, text='翻 译', bg='red', width=7,
                                         activebackground='firebrick', fg='ghostwhite', activeforeground='ghostwhite')
        translateButton.place(x=550, y=160, anchor='nw')
