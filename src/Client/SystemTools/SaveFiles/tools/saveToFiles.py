# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class SaveToFile():
    """
    保存文件类，将列表保存到文件。实际操作类
    """
    def __init__(self, fileName='../data/mission.dat'):
        self.fileName = fileName

    def saveToFile(self, data):
        """
        保存加密数据到文件
        :param data: 加密数据
        :return:
        """
        try:
            # 保存到文件
            self.files = open(self.fileName, 'wb')
            self.files.write(data)
            # 关闭文件流
            self.files.close()
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{SYSTEM_TOOLS_DEBUG} files has been write in file successfully')
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'SystemTools-SaveFiles-saveToFile',
                '|data': data,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None



if __name__ == '__main__':
    f = open('../../../../data/mission.dat', 'wb')
    print(f.read())
