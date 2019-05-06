# -*- coding:utf-8 -*-


from src.Client.Conf.config import *


class SaveConfigFile():
    """
    该类负责保存配置文件，属于实际操作类
    """
    def __init__(self, fileName='../conf/recitation.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def saveConfigFile(self, recitationId):
        """

        :param recitationId: 需要保存的任务id （int 或者 string）
        :return:
        """
        try:
            # 防御编程  若recitationId不是string，转换则在这转换
            if type(recitationId).__name__ != 'string':
                recitationId = str(recitationId).zfill(6)
            # 写回配置文件
            self.config.read(self.fileName)
            self.config.set("RECITATION", "recitationId", recitationId)
            self.config.write(open(self.fileName, "r+"))
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{RECITATION_DEBUG} config has been save in file successfully')
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'RECITATIONSystem-AddRecitation-saveConfigFile',
                '|missionId': recitationId,
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
