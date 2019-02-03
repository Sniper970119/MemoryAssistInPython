# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.SaveMission.tools import encodeText
from src.MissionSystem.SaveMission.tools import saveMissionToFile


class SaveMission():
    def __init__(self, filename='../data/mission.dat'):
        # 初始化加密工具
        self.encodeTools = encodeText.EncodeText()
        # 初始化保存工具
        self.saveTools = saveMissionToFile.SaveMissionToFile(fileName=filename)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for save mission')

    def saveMission(self, list):
        """
        保存任务
        :param list: 需要被保存的列表
        :return:
        """
        # 获取加密结果
        encodeText = self.encodeTools.encodeing(list)
        self.saveTools.saveToFile(encodeText)


# 进行文件存储的子系统测试
if __name__ == '__main__':
    dataList = []
    for i in range(1, 21):
        # 先封装成字典，方便后期删除
        dir = {
            'missionId': str(i).zfill(6),
            'bookName':  'bookName' + str(i).zfill(2),
            'missionRange': 'missionRange' + str(i).zfill(2),
            'nextTime': 'nextTime' + str(i).zfill(2),
            'missionState': 'state' + str(i).zfill(2),
            'loopTime': 5,
            'isFinish': False
        }

        dataList.append(dir)
    s = SaveMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    s.saveMission(list=dataList)
