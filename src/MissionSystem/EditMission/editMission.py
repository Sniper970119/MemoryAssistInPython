# -*- coding:utf-8 -*-

from src.Conf.config import *

from src.MissionSystem.EditMission.tools import computeNextMissionTime
from src.MissionSystem.EditMission.tools import editMissionList
from src.MissionSystem.EditMission.tools import finishMission
from src.MissionSystem.EditMission.tools import removeMission
from src.MissionSystem.SaveMission import saveMission


class EditMission():
    def __init__(self, filename='../data/mission.dat'):
        self.computeNextTimeTools = computeNextMissionTime.ComputeNextMissionTime()
        self.editMissionTools = editMissionList.EditMissionList()
        self.finishMissionTools = finishMission.FinishMission()
        self.removeMissionTools = removeMission.RemoveMission()
        self.saveMissionTools = saveMission.SaveMission(filename=filename)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for edit mission')
        pass

    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isEdit=False, isFinish=False, isDelete=False):
        """

        :param list: 需要被编辑的列表
        :param missionId: 任务id
        :param bookName: 书名
        :param missionRange: 任务范围
        :param nextTime: 下次时间
        :param state: 任务状态
        :param loopTime: 迭代次数
        :param isEdit: 执行编辑任务
        :param isFinish: 执行完成任务
        :param isDelete: 执行删除任务
        :return: 编辑后的list
        """
        try:
            if isEdit:
                list = self.editMissionTools.edit(list=list, missionId=missionId, bookName=bookName,
                                                  missionRange=missionRange,
                                                  nextTime=nextTime, state=state, loopTime=loopTime, isFinish=isFinish)
                self.saveMissionTools.saveMission(list)
            elif isFinish:
                list = self.finishMissionTools.finish(list=list, missionId=missionId)
                list = self.computeNextTimeTools.compute(list=list, missionId=missionId)
                self.saveMissionTools.saveMission(list)
            elif isDelete:
                list = self.removeMissionTools.remove(list=list, missionId=missionId)
                self.saveMissionTools.saveMission(list)
            else:
                pass
            pass
        except:
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{W}{MISSION_DEBUG} can not edit mission')


# 测试任务编辑系统
if __name__ == '__main__':
    from src.MissionSystem.LoadMission import loadMission

    l = loadMission.LoadMission("F:\python17\pythonPro\MemortAssit\data\mission.dat")
    list = l.loadMission()
    print(list)
    print()
    e = EditMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    # 测试更改完成状态
    # e.edit(list, '000025', isFinish=True)
    # 测试更改
    # e.edit(list, '000025', isEdit=True, bookName='bookTest')
    # 测试删除
    e.edit(list, '000025', isDelete=True)
    print(list)
