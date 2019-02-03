# -*- coding:utf-8 -*-
from src.Conf.config import *


class EditMissionList():
    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isFinish=None):
        for each in list:
            if each['missionId'] == missionId:
                if bookName != None:
                    each['bookName'] = bookName
                if missionRange != None:
                    each['missionRange'] = bookName
                if nextTime != None:
                    each['nextTime'] = bookName
                if state != None:
                    each['state'] = bookName
                if loopTime != None:
                    each['loopTime'] = bookName
                if isFinish != None:
                    each['isFinish'] = bookName

        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been edit finish successfully id is ' + missionId)
        return list
