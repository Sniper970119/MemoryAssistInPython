# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.VersionControlSystem.GetNewFile import doUpdate
from src.Client.VersionControlSystem.JudgeNeedUpdate import judgeNeedUpdate


class VersionControl():
    def __init__(self):
        self.judgeNeedUpdateTools = judgeNeedUpdate.JudgeNeedUpdate()

    def handle(self):
        if self.judgeNeedUpdateTools.judge():
            if messagebox.askokcancel(title='是否更新', message='检测到有新版本，是否更新'):
                doUpdate.GetNewFile()
