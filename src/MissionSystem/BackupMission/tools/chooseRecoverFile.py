# -*- coding:utf-8 -*-

from src.Conf.config import *


class ChooseRecoverFile():
    def __init__(self, filePath='../data/bkup/mbk/'):
        self.filePath = filePath
        pass

    def choose(self):
        """
        选择最新的备份作为备份文件
        :return:
        """
        files = os.listdir(self.filePath)
        maxFileName = None
        maxFileTime = 0
        for file in files:
            if maxFileTime == 0:
                maxFileTime = os.path.getctime(self.filePath + '/' + file)
                maxFileName = file
            else:
                if maxFileTime < os.path.getctime(self.filePath + '/' + file):
                    maxFileTime = os.path.getctime(self.filePath + '/' + file)
                    maxFileName = file
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} latest backup file has been chosen' + maxFileName)
        return maxFileName
