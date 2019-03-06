# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.DatabaseSystem.databaseSystem import DatabaseSystem


class Code101():
    def __init__(self):
        self.databaseTools = DatabaseSystem()
        pass

    def respond(self, connect, address):
        """
        响应代码101
        :param connect: 与客户端的连接
        :return:
        """
        try:
            # 生成随机的32位识别码
            code = ''.join(random.sample(string.ascii_letters + string.digits, 32))
            # 将随机生成码保存到数据库中
            # -------------------------------------------------------------------------
            self.databaseTools.newCode(code, address)
            # 发送随机识别码
            connect.send(code.encode('utf-8'))
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MessageTransferSystem-CodeHandle-Code101',
                '|wrongMessage': msg,
                '|connect': connect,
                '|address': address
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
