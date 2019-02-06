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
        # 转换任务id，防御编程
        missionId = str(missionId).zfill(6)
        # 遍历任务列表找到目标任务
        for each in list:
            if each['missionId'] == missionId:
                # 从列表中删除任务
                list.remove(each)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been delete successfully,id is '+missionId)
        return list