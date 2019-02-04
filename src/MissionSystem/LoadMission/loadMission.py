# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.LoadMission.tools import decodeText
from src.MissionSystem.LoadMission.tools import loadMissionFile


class LoadMission():
    def __init__(self, filename='../data/mission.dat'):
        self.fileName = filename
        # 初始化解密工具
        self.decodeTools = decodeText.DecodeText()
        # 初始化读取工具
        self.loadTools = loadMissionFile.LoadMissionFile(fileName=filename)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for load mission')

    def loadMission(self):
        """
        读取任务文件,读取失败直接删除该文件
        :return:
        """
        try:
            # 获取加密文件内容
            encodeText = self.loadTools.loadFile()
            # 解密加密内容
            list = self.decodeTools.decodeing(encodeText)
            return list
        except:
            print('except')
            os.remove(self.fileName)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{W}{MISSION_DEBUG} can not load mission,file has been delete')
        return None


# 进行读取文件的子系统测试
if __name__ == '__main__':
    l = LoadMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    data = l.loadMission()
    print(data)
