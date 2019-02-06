# -*- coding:utf-8 -*-
from src.Conf.config import *


class EditMissionList():

    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isFinish=None):
        # 转换任务id，防御编程
        missionId = str(missionId).zfill(6)
        # 遍历任务列表寻找目标任务
        for each in list:
            if each['missionId'] == missionId:
                # 对目标任务进行更新
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
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been edit finish successfully id is ' + missionId)

        return list
