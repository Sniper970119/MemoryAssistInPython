# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.View.MainFrame.TabFrame.FirstTabFrame import firstTabFrame
from src.Client.View.MainFrame.TabFrame.SecondTabFrame import translateFrame
from src.Client.View.MainFrame.TabFrame.ThirdFrame import reciterFrame


class TabFrame():
    """
    tab框架的主框架。
    """
    def __init__(self, rootFrame):
        """

        :param rootFrame: 根框架
        """
        self.tab = ttk.Notebook(rootFrame, height=350, width=700)

        self.tab.place(x=0, y=50, anchor='nw')

        # 调用子组件
        firstTabFrame.FirstTabFrame(tab=self.tab)
        translateFrame.TranslateFrame(tab=self.tab)
        reciterFrame.ReciterFrame(tab=self.tab)



    def getFrame(self):
        return self.tab
