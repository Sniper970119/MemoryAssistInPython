# -*- coding:utf-8 -*-
from src.Conf.config import *


class LoadMissionFile():
    def __init__(self, fileName='../data/mission.dat'):
        self.fileName = fileName
        pass

    def loadFile(self):
        """
        读取文件
        :return:读取的文件结果
        """
        try:
            # 读取文件，放在这而不放在构造函数中是因为这里可以catch到找不到文件的错误，以便读取备份文件
            self.missionFile = open(self.fileName, 'rb')
            # 读取文件
            fileData = self.missionFile.read()
            # 关闭文件流
            self.missionFile.close()
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} file has been load from file successfully')
            return fileData
        except:
            return None

