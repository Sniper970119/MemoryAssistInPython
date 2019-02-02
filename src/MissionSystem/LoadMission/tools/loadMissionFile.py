# -*- coding:utf-8 -*-
from src.Conf.config import *


class LoadMissionFile():
    def __init__(self, fileName='../data/mission.dat'):
        self.fileName = fileName
        self.missionFile = open(fileName, 'rb')
        pass

    def loadFile(self):
        """
        读取文件
        :return:读取的文件结果
        """
        fileData = self.missionFile.read()
        self.missionFile.close()
        if DEBUG and MISSION_DEBUG:
            print('{MISSION_DEBUG}{LOAD_MISSION_FILE} file has been load from file successfully')
        return fileData

