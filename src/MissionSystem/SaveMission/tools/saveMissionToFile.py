# -*- coding:utf-8 -*-
from src.Conf.config import *


class SaveMissionToFile():
    def __init__(self, fileName='../data/mission.dat'):
        self.fileName = fileName
        self.missionFile = open(fileName, 'wb')


    def saveToFile(self, data):
        """
        保存加密数据到文件
        :param data: 加密数据
        :return:
        """
        self.missionFile.write(data)
        self.missionFile.close()
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} file has been write in file successfully')
        pass
