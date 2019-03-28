# -*- coding:utf-8 -*-

from src.Client.Conf.config import *


class FinishMission():
    """
    该类负责完成任务，即将任务标记为完成状态。实际操作类。
    """
    def finish(self, list, missionId):
        """
        完成任务
        :param list: 列表
        :param missionId: 完成的任务编号
        :return: list列表
        """
        # 首先将列表备份，以便添加失败时返回最近正常的点
        backupList = list[:]
        try:
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
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-EditMission-finishMission',
                '|list': list,
                '|missionId': missionId,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return backupList


