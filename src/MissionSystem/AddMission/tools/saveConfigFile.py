# -*- coding:utf-8 -*-


from src.Conf.config import *


class SaveConfigFile():
    """
    该类负责保存配置文件，属于实际操作类
    """
    def __init__(self, fileName='../conf/mission.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def saveConfigFile(self, missionId):
        """

        :param missionId: 需要保存的任务id （int 或者 string）
        :return:
        """
        try:
            # 防御编程  若messionId不是string，转换则在这转换
            if type(missionId).__name__ != 'string':
                missionId = str(missionId).zfill(6)
            # 写回配置文件
            self.config.read(self.fileName)
            self.config.set("MISSION", "missionId", missionId)
            self.config.write(open(self.fileName, "r+"))
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} config has been save in file successfully')
        except Exception, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-AddMission-saveConfigFile',
                '|missionId': missionId,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()


# 配置文件读取测试
if __name__ == '__main__':
    s = SaveConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini')
    print(s.saveConfigFile(1))
