# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.View.MainFrame.TabFrame.FirstTabFrame import firstTabFrame


class TabFrame():

    def __init__(self, rootFrame):
        """

        :param rootFrame: 根框架
        """
        self.tab = ttk.Notebook(rootFrame, height=350, width=700)

        self.tab.place(x=0, y=50, anchor='nw')

        # 调用子组件
        firstTabFrame.FirstTabFrame(tab=self.tab)



    def getFrame(self):
        return self.tab
