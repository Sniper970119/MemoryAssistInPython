# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.View.MainFrame.TabFrame.FirstTabFrame import firstTabFrame
from src.View.MainFrame.TabFrame.SecondTabFrame import translateFrame


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



    def getFrame(self):
        return self.tab
