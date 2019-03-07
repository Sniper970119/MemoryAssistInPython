# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead


class MarkUser():
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
                '|file': 'MessageTransferSystem-MarkUser-markUser',
                '|wrongMessage': msg
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

    def judge(self):
        """
        读取用户识别码，如果没有识别码向服务器发送请求，如果有识别码，向服务器发送识别码和访问次数。
        :return:
        """
        try:
            userCode = self.configFileReadTools.readFile('USER_CODE', 'user_code')
            print('|'+userCode+'|')
            if userCode == '':
                # 如果当前没有用户识别码，向服务器请求识别码，并写回配置文件
                # 发送代码101 作为向服务器请求新的用户识别码
                code = '101'.encode('utf-8')
                self.s.send(code)
                returnData = self.s.recv(1024)
                # 写回配置文件
                self.configFileReadTools.saveFile('USER_CODE', 'user_code', returnData)
            else:
                # 如果有识别码，则向服务器发送识别码和当前记录的登录次数
                logTime = self.configFileReadTools.readFile('USER_CODE', 'user_time')
                code = '102'.encode('utf-8')
                self.s.send(code)
                returnData = self.s.recv(1024)
                if returnData == 'user_code':
                    # 发送用户识别码
                    self.s.send(userCode.encode('utf-8'))
                returnData = self.s.recv(1024)
                if returnData == 'time':
                    # 发送登录次数，发送成功则将配置文件中的属性清零
                    self.s.send(logTime.encode('utf-8'))
                    self.configFileReadTools.saveFile('USER_CODE', 'user_time', '0')
        except socket.error as msg:
            print('no network')
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'VersionControlSystem-versionControl',
                '|wrongMessage': msg,
                '|没有互联网连接|': '没有互联网连接',
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

