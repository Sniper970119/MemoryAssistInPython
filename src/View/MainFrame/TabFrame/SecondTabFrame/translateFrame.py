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

        # 调用子组件
        self.printInputText()

        self.printOutputText()

        self.printTanlateButton()

        tab.add(self.secondTabFrame, text='文本翻译')

    def printInputText(self):
        """
        绘制输入文本
        :return:
        """
        self.inputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('黑体', 16))
        self.inputText.place(x=60, y=30, anchor='nw')

    def printOutputText(self):
        """
        绘制输出文本
        :return:
        """
        self.outputText = tkinter.Text(self.secondTabFrame, width=45, height=5, font=('黑体', 16))
        self.outputText.config(state='disabled')
        self.outputText.place(x=60, y=200, anchor='nw')

    def printTanlateButton(self):
        """
        绘制翻译按钮
        :return:
        """
        def translateText():
            """
            翻译按钮事件
            :return:
            """
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG} user select translate')
            text = self.inputText.get("0.0", "end").encode('utf-8')
            if text == '':
                return
            translateResult = translateInBaidu.Translate().translate(text)
            self.outputText.config(state='normal')
            self.outputText.delete('1.0', 'end')
            self.outputText.insert('insert', translateResult)
            self.outputText.config(state='disabled')

        def autoTranslate(event):
            """
            输入栏enter 翻译快捷键事件
            :param event:
            :return:
            """
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG} user press enter')
            translateText()

        def changeLine(event):
            """
            换行事件，因为这里shift+enter 后一个enter会被认为是换行，但是不会激活自动翻译 = =
            所以这里不做任何操作，就可以进行换行
            :param event:
            :return:
            """

            # self.inputText.insert('insert', '\n')
            pass

        def selectText(event):
            """
            全选文本，即ctrl+a 的全选
            :param event:
            :return:
            """
            self.inputText.tag_add(tkinter.SEL, "1.0", tkinter.END)
            return 'break'
        # 翻译按钮
        translateButton = tkinter.Button(self.secondTabFrame, text='翻 译', bg='red', width=7,
                                         activebackground='firebrick', fg='ghostwhite', activeforeground='ghostwhite',
                                         command=translateText)
        # 添加在输入文本上的各种快捷键
        self.inputText.bind("<Shift-Return>", changeLine)
        self.inputText.bind("<Return>", autoTranslate)
        self.inputText.bind("<Control-Key-a>", selectText)
        self.inputText.bind("<Control-Key-A>", selectText)
        translateButton.place(x=600, y=120, anchor='nw')

        def copyToShearPlate():
            """
            复制翻译后的文本到剪切板
            :return:
            """
            if DEBUG and VIEW_DEBUG:
                print('{USR}{VIEW_DEBUG} user select copy to shear plate')
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            # 这里因为编码问题，用来debug展示的字符编码和复制到剪切板的字符编码不一样，所以分来
            translateResultUseToShow = self.outputText.get("0.0", "end").encode('utf-8')
            # 这里去掉text默认的最后一个的换行符，使剪切板的文本为用户需要翻译的准确翻译
            translateResultUseToCopy = self.outputText.get("0.0", "end")[:-1].encode('gbk')
            win32clipboard.SetClipboardData(win32con.CF_TEXT, translateResultUseToCopy)
            win32clipboard.CloseClipboard()
            pass
        # 复制到剪切板按钮
        copyToShearPlateButton = tkinter.Button(self.secondTabFrame, text='复 制', bg='red', width=7,
                                                activebackground='firebrick', fg='ghostwhite',
                                                activeforeground='ghostwhite',
                                                command=copyToShearPlate)
        copyToShearPlateButton.place(x=570, y=290, anchor='nw')


        def deleteAll():
            self.outputText.config(state='normal')
            self.outputText.delete('1.0', 'end')
            self.outputText.config(state='disabled')

        # 清空按钮
        deleteAllButton = tkinter.Button(self.secondTabFrame, text='清 空', bg='red', width=7,
                                                activebackground='firebrick', fg='ghostwhite',
                                                activeforeground='ghostwhite',
                                                command=deleteAll)
        deleteAllButton.place(x=630, y=290, anchor='nw')
