# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead


class Code100():
    def __init__(self):
        pass

    def respond(self, connect):
        """
        响应代码100
        :param connect: 与客户端的连接
        :return:
        """
        try:
            returnCode = str(configFileRead.ConfigFileRead().readFile('VERSION', 'lastest_version'))
            connect.send(returnCode.encode('utf-8'))
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MessageTransferSystem-CodeHandle-Code100',
                '|wrongMessage': msg,
                '|connect': connect
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

