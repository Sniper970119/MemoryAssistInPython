# -*- coding:utf-8 -*-


from src.Client.Conf.config import *

from src.Client.SearchSystem import searchSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSearchResultTools import showMission, showWord


class ShowCN():
    def show(self):
        """
        切换中文
        :return:
        """
        configFileRead.ConfigFileRead(fileName='./conf/user.ini').saveFile('LANGUAGE', 'language', 'CN')
        print("显示中文")
        pass
