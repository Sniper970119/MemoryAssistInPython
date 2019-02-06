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
        # 获取备份文件列表
        files = os.listdir(self.filePath)
        maxFileName = None
        maxFileTime = 0
        # 寻找最新的备份文件
        for file in files:
            # 初始化为第一个文件最后修改时间的时间戳
            if maxFileTime == 0:
                maxFileTime = os.path.getctime(self.filePath + '/' + file)
                maxFileName = file
            # 寻找最小时间戳
            else:
                if maxFileTime < os.path.getctime(self.filePath + '/' + file):
                    maxFileTime = os.path.getctime(self.filePath + '/' + file)
                    maxFileName = file
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} latest backup file has been chosen' + maxFileName)
        # 返回最小时间戳的文件名
        return maxFileName
