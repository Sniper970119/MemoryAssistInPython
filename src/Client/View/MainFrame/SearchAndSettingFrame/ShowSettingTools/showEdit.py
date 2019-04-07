# -*- coding:utf-8 -*-
from src.Client.Conf.config import *

from src.Client.SearchSystem import searchSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSearchResultTools import showMission, showWord
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools.Util import showCN, showEN


class ShowEdit():
    """
    本类负责显示设置页面的具体显示以及提交操作。
    """

    def __init__(self):
        self.windowTitleVar = tkinter.StringVar()
        self.languageSettingVar = tkinter.StringVar()
        self.acceptButtonVar = tkinter.StringVar()
        self.language()
        pass

    def language(self):
        """
        语言切换，暂时不做外部调用（即每次重启生效）
        :return:
        """
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        if languageType == 'CN':
            self.windowTitleVar.set('设置')
            self.languageSettingVar.set('语言设置（部分页面将在下次启动时生效）')
            self.acceptButtonVar.set('确定')
        elif languageType == 'EN':
            self.windowTitleVar.set('edit')
            self.languageSettingVar.set('language setting (some page need to restart)')
            self.acceptButtonVar.set('OK')
        else:
            self.windowTitleVar.set('设置')
            self.languageSettingVar.set('语言设置（部分页面将在下次启动时生效）')
            self.acceptButtonVar.set('确定')

    def window(self):
        """
        负责绘制具体的设置页面
        :return:
        """
        showWindow = tkinter.Toplevel()
        screenWidth = showWindow.winfo_screenwidth()
        screenHeight = showWindow.winfo_screenheight()
        showWindow.geometry(
            '300x250+' + str(int((screenWidth - 300) / 2)) + '+' + str(int((screenHeight - 250) / 2)))
        showWindow.resizable(width=False, height=False)
        showWindow.title(self.windowTitleVar.get())
        showWindow.iconbitmap('images/icon.ico')

        def settingHandle():
            """
            负责点击确定按钮后的提交操作
            :return:
            """
            # print(varSelect)
            if varSelect.get() == 'CN':
                showCN.ShowCN().show()
            elif varSelect.get() == 'EN':
                showEN.ShowEN().show()
            showWindow.after(300, showWindow.destroy)
            pass

        varSelect = tkinter.StringVar()
        languageType = configFileRead.ConfigFileRead(fileName='./conf/user.ini').readFile("LANGUAGE", 'language')
        varSelect.set(languageType)

        languageLabel = tkinter.Label(showWindow, text=self.languageSettingVar.get())
        languageLabel.place(x=20, y=20, anchor='nw')
        radioButtonCN = tkinter.Radiobutton(showWindow, text='简体中文', variable=varSelect, value="CN")
        radioButtonCN.place(x=50, y=50, anchor='nw')
        radioButtonEN = tkinter.Radiobutton(showWindow, text='English', variable=varSelect, value='EN')
        radioButtonEN.place(x=150, y=50, anchor='nw')

        settingButton = tkinter.Button(showWindow, textvariable=self.acceptButtonVar, command=settingHandle, width=8, height=1)
        settingButton.place(x=210, y=200, anchor='nw')

        pass
