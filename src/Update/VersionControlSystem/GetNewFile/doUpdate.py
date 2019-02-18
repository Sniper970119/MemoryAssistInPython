# -*- coding:utf-8 -*-

from src.Update.Conf.config import *
from src.Update.VersionControlSystem.GetNewFile.Tools import getUpdateFile, getIndexFile, unZipFile


class GetNewFile():
    def __init__(self, filePath='update.zip'):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((SERVER_IP, SERVER_FILE_PORT))
            self.getUpdateFileTools = getUpdateFile.GetUpdateFile(self.s)
            self.getIndexFileTools = getIndexFile.GetIndexFile(self.s)
            self.unZipFileTools = unZipFile.UnZipFile(filePath)

            self.getIndexFileTools.getFile()
            self.getUpdateFileTools.get()
            self.unZipFileTools.un_zip()
        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'VersionControlSystem-GetNewFile-doUpdate',
                '|wrongMessage': msg
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()



if __name__ == '__main__':
    GetNewFile()