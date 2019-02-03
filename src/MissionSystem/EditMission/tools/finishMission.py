# -*- coding:utf-8 -*-

from src.Conf.config import *


class FinishMission():

    def finish(self, list, missionId):
        """
        完成任务
        :param list: 列表
        :param missionId: 完成的任务编号
        :return: list列表
        """
        for each in list:
            if each['missionId'] == missionId:
                each['isFinish'] = True
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been set finish successfully id is ' + missionId)
        return list
