# -*- coding:utf-8 -*-
from src.Conf.config import *


class AddMissionToList():

    def addMission(self, list, missionId, bookName, missionRange, nextTime=None, state=1, loopTime=5, isFinish=False):
        """
        添加任务
        :param list:  目标list
        :param missionId: 任务id（string
        :param bookName: 书名
        :param missionRange: 任务范围
        :param nextTime: 下次任务时间
        :param state: 任务状态
        :param loopTime: 剩余迭代次数
        :param isFinish: 任务是否完成
        :return: 插入后的list
        """

        # 如果新建任务时没有指定日期，则生成当前日期
        if nextTime is None:
            nextTime = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d').strftime(
                "%Y-%m-%d")
        # 构造任务字典
        missionDir = {
            'missionId': str(missionId).zfill(6),
            'bookName': bookName,
            'missionRange': missionRange,
            'nextTime': nextTime,
            'state': state,
            'loopTime': loopTime,
            'isFinish': isFinish
        }
        # 将任务字典添加到列表中
        list.append(missionDir)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} mission has been add to list successfully, id is ' + str(missionId))
        return list
