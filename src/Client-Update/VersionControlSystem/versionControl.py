# -*- coding:utf-8 -*-
from src.Client.VersionControlSystem.JudgeNeedUpdate import judgeNeedUpdate
from src.Client.VersionControlSystem.GetNewFile import doUpdate

class VersionControl():
    def __init__(self):
        self.judgeNeedUpdateTools = judgeNeedUpdate.JudgeNeedUpdate()


    def handle(self):
        if self.judgeNeedUpdateTools.judge():
            doUpdate.GetNewFile()
