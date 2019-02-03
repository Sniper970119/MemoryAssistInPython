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
        pass

    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isEdit=False, isFinish=False, isDelete=False):
        if isEdit:
            list = self.editMissionTools.edit(list=list, missionId=missionId, bookName=bookName,
                                              missionRange=missionRange,
                                              nextTime=nextTime, state=state, loopTime=loopTime, isFinish=isFinish)
            self.saveMissionTools.saveMission(list)
        elif isFinish:
            list = self.finishMissionTools.finish(list=list, missionId=missionId)
            self.saveMissionTools.saveMission(list)
        elif isDelete:
            list = self.removeMissionTools.remove(list=list, missionId=missionId)
            self.saveMissionTools.saveMission(list)
        else:
            pass
        pass
