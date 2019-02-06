# -*- coding:utf-8 -*-
from src.Conf.config import *


class EditMissionList():

    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isFinish=None):
        missionId = str(missionId).zfill(6)
        for each in list:
            if each['missionId'] == missionId:
                if bookName != None:
                    each['bookName'] = bookName
                if missionRange != None:
                    each['missionRange'] = missionRange
                if nextTime != None:
                    each['nextTime'] = nextTime
                if state != None:
                    each['state'] = state
                if loopTime != None:
                    each['loopTime'] = loopTime
                if isFinish != None:
                    each['isFinish'] = isFinish
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been edit finish successfully id is ' + missionId)

        return list
