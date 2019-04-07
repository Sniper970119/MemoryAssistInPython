# -*- coding:utf-8 -*-


from src.Client.Conf.config import *

from src.Client.SearchSystem import searchSystem
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSearchResultTools import showMission, showWord


class ShowEN():
    def show(self):
        """
        切换英文
        :return:
        """
        configFileRead.ConfigFileRead(fileName='./conf/user.ini').saveFile('LANGUAGE', 'language', 'EN')
        print("显示英文")

        pass
