# -*- coding:utf-8 -*-


from src.Client.Conf.config import *


class LoadConfigFile():
    """
    该类负责读取配置文件，属于实际操作类
    """
    def __init__(self, fileName='../conf/mission.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def loadConfigFile(self):
        """
        读取配置文件
        :return:下个id（int）
        """
        try:
            # 读取配置文件
            self.config.readfp(open(self.fileName))
            missionId = self.config.get('MISSION', 'missionId')
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} config has been load from file successfully')
            return int(missionId)
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-AddMission-loadConfigFile',
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
    l = LoadConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini')
    print(l.loadConfigFile())
