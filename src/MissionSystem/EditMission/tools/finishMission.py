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
        # 转换任务id，防御编程
        missionId = str(missionId).zfill(6)
        # 遍历任务列表找到目标任务
        for each in list:
            if each['missionId'] == missionId:
                # 完成状态置为True
                each['isFinish'] = True
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been set finish successfully id is ' + missionId)
        return list
