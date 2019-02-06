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
        # 找到目标任务
        for each in list:
            if each['missionId'] == missionId:
                # 获取当前任务状态，防御编程，强制转化
                missionState = int(each['state'])
                # 更改后的任务状态
                stateCode = int(each['state'])
                # 获取当前时间
                currnetTime = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d')
                nextTime = None
                # 对不同的任务状态执行对应操作
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
                    # 判断是否有下一次迭代，如果没有置为never
                    if each['loopTime'] != 0:
                        each['loopTime'] = each['loopTime'] - 1
                    else:
                        stateCode = 0
                else:
                    # 打印debug日志
                    if DEBUG and MISSION_DEBUG:
                        print('{SYS}{W}{MISSION_DEBUG} wrong in compute next time, wrong state code')
                each['nextTime'] = nextTime
                each['state'] = stateCode
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{W}{MISSION_DEBUG} wrong in compute next time, wrong state code')
        return list
