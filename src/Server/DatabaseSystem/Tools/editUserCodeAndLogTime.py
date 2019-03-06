# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class EditUserCodeAndLogTime():
    def __init__(self, totalCol, weeklyCol):
        self.totalCol = totalCol
        self.weeklyCol = weeklyCol

    def save(self, userCode, userIp, logTime):
        """
        处理旧用户的登录请求
        :param userCode: 用户识别码
        :param userIp: 用户登录ip
        :param logTime: 登录次数
        :return:
        """
        try:
            # 读取数据
            dataInWeekly = self.weeklyCol.find_one({'user_code': userCode})
            dataInTotal = self.totalCol.find_one({'user_code': userCode})
            # 对登录次数数据进行更改
            dataInWeekly['weekly_time'] = str(int(dataInWeekly['weekly_time']) + int(logTime))
            dataInTotal['total_time'] = str(int(dataInTotal['total_time']) + int(logTime))
            # 对访问ip进行更改
            weeklyIp = dataInWeekly['user_ip']
            if userIp in weeklyIp.keys():
                weeklyIp[userIp] = str(int(weeklyIp[userIp]) + 1)
            else:
                weeklyIp[userIp] = '1'
            totalIp = dataInTotal['user_ip']
            if userIp in totalIp.keys():
                totalIp[userIp] = str(int(totalIp[userIp]) + 1)
            else:
                totalIp[userIp] = '1'
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'DatabaseSystem-editUserCodeAndLogTime',
                '|wrongMessage': msg,
                '|userCode': userCode,
                '|userIp': userIp,
                '|logTime': logTime,
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
        pass

