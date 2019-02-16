# -*- coding:utf-8 -*-

from src.Conf.config import *

from src.MissionSystem.EditMission.tools import computeNextMissionTime
from src.MissionSystem.EditMission.tools import editMissionList
from src.MissionSystem.EditMission.tools import finishMission
from src.MissionSystem.EditMission.tools import removeMission
from src.MissionSystem.SaveMission import saveMission


class EditMission():
    """
    编辑任务子系统。调用类，任务由被调用者完成。
    """
    def __init__(self, filename='../data/mission.dat'):
        # 初始化工具
        self.computeNextTimeTools = computeNextMissionTime.ComputeNextMissionTime()
        self.editMissionTools = editMissionList.EditMissionList()
        self.finishMissionTools = finishMission.FinishMission()
        self.removeMissionTools = removeMission.RemoveMission()
        self.saveMissionTools = saveMission.SaveMission(filename=filename)
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
        :param isEdit: 执行编辑任务标记
        :param isFinish: 执行完成任务标记
        :param isDelete: 执行删除任务标记
        :return: 编辑后的list
        """
        try:
            print('in')
            # 对不同的编辑命令做出不同的响应
            if isEdit:
                # 调用编辑子系统
                list = self.editMissionTools.edit(list=list, missionId=missionId, bookName=bookName,
                                                  missionRange=missionRange,
                                                  nextTime=nextTime, state=state, loopTime=loopTime, isFinish=isFinish)
                self.saveMissionTools.saveMission(list)
            if isFinish:
                # 调用完成子系统
                list = self.finishMissionTools.finish(list=list, missionId=missionId)
                list = self.computeNextTimeTools.compute(list=list, missionId=missionId)
                self.saveMissionTools.saveMission(list)
            if isDelete:
                # 调用删除子系统
                list = self.removeMissionTools.remove(list=list, missionId=missionId)
                self.saveMissionTools.saveMission(list)
        except:
            # 打印debug日志
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
