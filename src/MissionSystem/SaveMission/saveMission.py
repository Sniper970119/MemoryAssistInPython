# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.SaveMission.tools import encodeText
from src.MissionSystem.SaveMission.tools import saveMissionToFile


class SaveMission():
    def __init__(self, filename='../data/mission.dat'):
        # 初始化加密工具
        self.encodeTools = encodeText.EncodeText()
        # 初始化保存工具
        self.saveTools = saveMissionToFile.SaveMissionToFile(filename)

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
            '任务id': str(i).zfill(4),
            '书名': 'bookName' + str(i).zfill(2),
            '任务范围': 'missionRange' + str(i).zfill(2),
            '任务进度': 'state' + str(i).zfill(2),
            '下次任务': 'nextTime' + str(i).zfill(2)
        }
        dataList.append(dir)
    s = SaveMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    s.saveMission(list=dataList)
