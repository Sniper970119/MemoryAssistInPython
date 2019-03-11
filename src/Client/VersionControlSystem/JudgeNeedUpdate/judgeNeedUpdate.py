# -*- coding:utf-8 -*-
from src.Client.MessageTransferSystem.VersionControl.versionControl import VersionControl


class JudgeNeedUpdate():
    def __init__(self):
        pass

    def judge(self):
        return VersionControl().judge()
