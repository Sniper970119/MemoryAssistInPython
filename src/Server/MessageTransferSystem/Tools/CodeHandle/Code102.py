# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.DatabaseSystem.databaseSystem import DatabaseSystem


class Code102():
    def __init__(self):
        self.databaseTools = DatabaseSystem()
        pass

    def respond(self, connect, address):
        """
        响应代码102
        :param connect: 与客户端的连接
        :return:
        """
        try:
            # 向客户端发送连接标记
            connect.send('user_code'.encode('utf-8'))
            userCode = connect.recv(1024)
            connect.send('time'.encode('utf-8'))
            logTime = connect.recv(1024)
            # 将数据更新到数据中
            # -------------------------------------------------------------------------
            self.databaseTools.saveTools(userCode=userCode, address=address, logTime=logTime)
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MessageTransferSystem-CodeHandle-Code102',
                '|wrongMessage': msg,
                '|connect': connect,
                '|address': address
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()