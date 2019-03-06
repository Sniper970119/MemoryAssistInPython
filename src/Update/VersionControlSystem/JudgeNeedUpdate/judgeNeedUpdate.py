# -*- coding:utf-8 -*-
from src.Update.Conf.config import *
from src.Update.SystemTools.ConfFileRead import configFileRead


class JudgeNeedUpdate():
    def __init__(self):
        try:
            self.configFileReadTools = configFileRead.ConfigFileRead()
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((SERVER_IP, SERVER_MES_PORT))
            print(SERVER_IP)


        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'VersionControlSystem-GetNewFile-judgeNeedUpdate',
                '|wrongMessage': msg
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

    def judge(self):
        # return True
        version = self.configFileReadTools.readFile('VERSION', 'version')
        print(version)
        # 请求码为100时 返回最新版本号
        code = '100'.encode('utf-8')
        self.s.send(code)
        returnData = self.s.recv(1024)
        print(returnData)
        if version == returnData:
            return False, returnData
        else:
            return True, returnData
        pass
