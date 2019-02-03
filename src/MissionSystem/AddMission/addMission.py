# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.AddMission.tools import addMissionToList
from src.MissionSystem.AddMission.tools import loadConfigFile
from src.MissionSystem.AddMission.tools import saveConfigFile
from src.MissionSystem.SaveMission import saveMission


class AddMission():
    def __init__(self, confFileName='../data/mission.dat', dataFileName='../data/mission.dat'):
        # 初始化工具
        self.addMissionTools = addMissionToList.AddMissionToList()
        self.loadConfigTools = loadConfigFile.LoadConfigFile(fileName=confFileName)
        self.saveConfigTools = saveConfigFile.SaveConfigFile(fileName=confFileName)
        self.saveMissionTools = saveMission.SaveMission(filename=dataFileName)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for add mission')
        pass

    def addMission(self, list, bookName, missionRange, missionId=None, nextTime=None, state=1, loopTime=5,
                   isFinish=False):
        """

        :param list:  目标list
        :param missionId: 任务id（string
        :param bookName: 书名
        :param missionRange: 任务范围
        :param nextTime: 下次任务时间
        :param state: 任务状态
        :param loopTime: 剩余迭代次数
        :param isFinish: 任务是否完成
        :return: 添加后的list
        """
        if missionId is None:
            # 读取配置文件并自增+1
            nextMissionId = self.loadConfigTools.loadConfigFile()
            nextMissionId = nextMissionId + 1
            # 写回到配置文件
            self.saveConfigTools.saveConfigFile(nextMissionId)
            missionId = nextMissionId
        # 添加到列表并获取到返回列表
        list = self.addMissionTools.addMission(list=list, missionId=missionId, bookName=bookName,
                                               missionRange=missionRange, nextTime=nextTime, state=state,
                                               loopTime=loopTime,
                                               isFinish=isFinish)
        # 保存到文件
        self.saveMissionTools.saveMission(list)
        return list


# 对添加任务子系统的测试
if __name__ == '__main__':
    list = []
    a = AddMission(confFileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini',
                   dataFileName='F:\python17\pythonPro\MemortAssit\data\mission.dat')
    a.addMission(list=list, bookName='testBook', missionRange='testMission')
