# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.LoadMission.tools import decodeText
from src.MissionSystem.LoadMission.tools import loadMissionFile

class LoadMission():
    def __init__(self, filename='../data/mission.dat'):
        # 初始化解密工具
        self.decodeTools = decodeText.DecodeText()
        # 初始化读取工具
        self.loadTools = loadMissionFile.LoadMissionFile(fileName=filename)
        if DEBUG and MISSION_DEBUG:
            print('{MISSION_DEBUG}{*LOAD_MISSION*} ready for load mission')

    def loadMission(self):
        """
        读取任务文件
        :return:
        """
        # 获取加密文件内容
        encodeText = self.loadTools.loadFile()
        # 解密加密内容
        list = self.decodeTools.decodeing(encodeText)

        return list


# 进行读取文件的子系统测试
if __name__ == '__main__':
    l = LoadMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    data = l.loadMission()
    # print(data)
