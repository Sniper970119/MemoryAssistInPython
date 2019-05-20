# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class AddRecitationToList():
    """
    该类负责将背诵任务添加到列表，属于实际操作类
    """

    def addRecitation(self, list, recitationId, question, answer, weight=10):
        """
        添加任务
        :param list:  目标list
        :param recitationId: 任务id（string
        :param question: 书名
        :param answer: 任务范围
        :param weight: 权重
        :return: 插入后的list
        """
        # 首先将列表备份，以便添加失败时返回最近正常的点
        backupList = list[:]
        try:
            # 构造任务字典
            recitationDir = {
                'recitationId': str(recitationId).zfill(6),
                'question': question,
                'answer': answer,
                'weight': int(weight)
            }
            # 将任务字典添加到列表中
            list.append(recitationDir)
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} mission has been add to list successfully, id is ' + str(recitationId))
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
                '|file': 'RecitationSystem-addRecitation-addRecitationToList',
                '|list': list,
                '|recitationId': recitationId,
                '|question': question,
                '|answer': answer,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return backupList
