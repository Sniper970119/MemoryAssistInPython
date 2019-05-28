# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class RemoveRecitation():
    """
    移除任务类，负责将任务删除。实际操作类
    """
    def remove(self, list, recitationId):
        """
        删除任务
        :param list: 列表
        :param recitationId: 完成的任务编号
        :return: list列表
        """
        # 首先将列表备份，以便添加失败时返回最近正常的点
        backupList = list[:]
        try:
            # 转换任务id，防御编程
            recitationId = str(recitationId).zfill(6)
            # 遍历任务列表找到目标任务
            for each in list:
                if each['recitationId'] == recitationId:
                    # 从列表中删除任务
                    print(each)
                    list.remove(each)
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{RECITATION_DEBUG} recitation has been delete successfully,id is ' + recitationId)
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
                '|file': 'MissionSystem-EditMission-removeMission',
                '|list': list,
                '|missionId': recitationId,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return backupList

