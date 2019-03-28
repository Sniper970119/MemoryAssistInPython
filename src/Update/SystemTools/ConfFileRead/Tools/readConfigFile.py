# -*- coding:utf-8 -*-


from src.Update.Conf.config import *


class ReadConfigFile():
    """
    该类负责读取配置文件，属于实际操作类
    """

    def __init__(self, fileName='./conf/main.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def readConfigFile(self, configMainName, configSubName):
        """

        :param configMainName:配置信息主属性名
        :param configSubName:配置信息副属性名
        :return:配置信息（str）
        """
        try:
            # 读取配置文件
            self.config.readfp(open(self.fileName))
            message = self.config.get(configMainName, configSubName)
            # 打印debug日志
            if DEBUG and SYSTEM_TOOLS_DEBUG:
                print('{SYS}{MISSION_DEBUG} config has been load from file successfully')
            return str(message)
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|configMainName': configMainName,
                '|configSubName': configSubName,
                '|file': 'SystemTools-ConfFileRead-readConfigFile',
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None


# 配置文件读取测试
if __name__ == '__main__':
    l = ReadConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\main.ini')
    print(l.readConfigFile('VERSION', 'version'))
