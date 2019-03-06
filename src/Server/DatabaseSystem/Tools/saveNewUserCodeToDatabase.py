# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class SaveNewUserCodeToDataBase():
    def __init__(self, totalCol, weeklyCol):
        self.totalCol = totalCol
        self.weeklyCol = weeklyCol

    def save(self, userCode, userIp):
        """
        执行新存储用户信息
        :param userCode: 用户识别码
        :param userIp: 用户登录ip
        :return:
        """
        try:
            dictInTotal = {
                'user_code': userCode,
                'total_time': '1',
                'user_ip': {userIp: '1'},
            }
            dictInWeekly = {
                'user_code': userCode,
                'weekly_time': '1',
                'user_ip': {userIp: '1'},
            }
            self.totalCol.insert_one(dictInTotal)
            self.weeklyCol.insert_one(dictInWeekly)
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'DatabaseSystem-saveNewUserCodeToDatabase',
                '|wrongMessage': msg,
                '|userCode': userCode,
                '|userIp': userIp
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
        pass
