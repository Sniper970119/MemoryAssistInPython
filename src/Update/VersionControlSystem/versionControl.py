# -*- coding:utf-8 -*-
from src.Update.Conf.config import *
from src.Update.VersionControlSystem.GetNewFile import doUpdate
from src.Update.VersionControlSystem.JudgeNeedUpdate import judgeNeedUpdate


class VersionControl():
    def __init__(self):
        self.judgeNeedUpdateTools = judgeNeedUpdate.JudgeNeedUpdate()

    def handle(self):
        """
        版本控制一级系统
        :return:
        """
        if self.judgeNeedUpdateTools.judge():
            if messagebox.askokcancel(title='是否更新', message='检测到有新版本，是否更新'):
                doUpdate.GetNewFile()
