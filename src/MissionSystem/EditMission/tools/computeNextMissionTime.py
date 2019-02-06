# -*- coding:utf-8 -*-

from src.Conf.config import *


class ComputeNextMissionTime():
    def __init__(self):
        # 定义几种任务状态的常量，分别为，不再提示、新任务、一天后重复、两天后重复···和更多（15天）
        self.NEVER = 0
        self.NEW_MISSION = 1
        self.ONE_DAY = 2
        self.TWO_DAY = 3
        self.FOUR_DAY = 4
        self.SEVEN_DAY = 5
        self.FIFTH_DAY = 6
        self.MORE = 7
        pass

    def compute(self, list, missionId):
        for each in list:
            if each['missionId'] == missionId:
                missionState = int(each['state'])
                currnetTime = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d')
                nextTime = None
                stateCode = int(each['state'])
                if missionState == 0:
                    if DEBUG and MISSION_DEBUG:
                        print('{SYS}{MISSION_DEBUG} this is a mission dead,id is ' + missionId)
                if missionState == 1:
                    nextTime = (currnetTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 2:
                    nextTime = (currnetTime + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 3:
                    nextTime = (currnetTime + datetime.timedelta(days=2)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 4:
                    nextTime = (currnetTime + datetime.timedelta(days=4)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 5:
                    nextTime = (currnetTime + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 6:
                    nextTime = (currnetTime + datetime.timedelta(days=15)).strftime("%Y-%m-%d")
                    stateCode = stateCode + 1
                elif missionState == 7:
                    nextTime = (currnetTime + datetime.timedelta(days=15)).strftime("%Y-%m-%d")
                    if each['loopTime'] != 0:
                        each['loopTime'] = each['loopTime'] - 1
                    else:
                        stateCode = 0
                else:
                    if DEBUG and MISSION_DEBUG:
                        print('{SYS}{W}{MISSION_DEBUG} wrong in compute next time, wrong state code')
                each['nextTime'] = nextTime
                each['state'] = stateCode
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{W}{MISSION_DEBUG} wrong in compute next time, wrong state code')
        return list
