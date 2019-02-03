# -*- coding:utf-8 -*-
from src.Conf.config import *


class RemoveMission():

    def remove(self, list, missionId):
        """
        删除任务
        :param list: 列表
        :param missionId: 完成的任务编号
        :return: list列表
        """
        for each in list:
            if each['missionId'] == missionId:
                list.remove(each)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been delete successfully,id is '+missionId)
        return list