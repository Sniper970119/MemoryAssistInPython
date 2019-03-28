# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class EditMissionList():
    """
    负责编辑任务，实际操作类
    """
    def edit(self, list, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
             isFinish=None):
        """
        编辑任务
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
        # 首先将列表备份，以便添加失败时返回最近正常的点
        backupList = list[:]
        try:
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
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-EditMission-editMissionList',
                '|list': list,
                '|missionId': missionId,
                '|bookName': bookName,
                '|missionRange': missionRange,
                '|nextTime': nextTime,
                '|state': state,
                '|loopTime': loopTime,
                '|isFinish': isFinish,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return backupList

