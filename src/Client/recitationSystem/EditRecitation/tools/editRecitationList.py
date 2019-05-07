# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class EditRecitationList():
    """
    负责编辑任务，实际操作类
    """

    def edit(self, list, recitationId, question=None, answer=None):
        """
        编辑任务
        :param list:  目标list
        :param recitationId: 任务id（string
        :param question: 书名
        :param answer: 任务范围
        :return: 插入后的list
        """
        # 首先将列表备份，以便添加失败时返回最近正常的点
        backupList = list[:]
        try:
            # 转换任务id，防御编程
            recitationId = str(recitationId).zfill(6)
            # 遍历任务列表寻找目标任务
            for each in list:
                if each['recitationId'] == recitationId:
                    # 对目标任务进行更新
                    if question != None:
                        each['question'] = question
                    if answer != None:
                        each['answer'] = answer
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{RECITATION_DEBUG} mission has been edit finish successfully id is ' + recitationId)

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
                '|file': 'RecitationSystem-EditRecitation-editRecitationList',
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
