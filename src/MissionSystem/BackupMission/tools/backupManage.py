# -*- coding:utf-8 -*-

from src.Conf.config import *


class BackupManage():
    """
    该类负责备份管理，维护备份文件的个数，属于实际操作类
    """
    def __init__(self, filePath='../data/bkup/mbk/'):
        self.filePath = filePath
        pass

    def manage(self):
        """
        文件管理
        :return:
        """
        try:
            files = os.listdir(self.filePath)
            minFileName = None
            minFileTime = 0
            # 保持7个备份
            if len(files) > 7:
                # 打印debug日志
                if DEBUG and MISSION_DEBUG:
                    print('{SYS}{MISSION_DEBUG} backup file need to delete')
                # 遍历目的中的文件，找出存在时间最长的文件名
                for file in files:
                    # 初始化为第一个目录的修改时间的时间戳
                    if minFileTime == 0:
                        minFileTime = os.path.getctime(self.filePath + '/' + file)
                        minFileName = file
                    else:
                        # 比较时间戳
                        if minFileTime > os.path.getctime(self.filePath + '/' + file):
                            minFileTime = os.path.getctime(self.filePath + '/' + file)
                            minFileName = file
                # 删除时间戳最大的文件
                self.deleteBackupFile(minFileName)
            else:
                # 打印debug日志
                if DEBUG and MISSION_DEBUG:
                    print('{SYS}{MISSION_DEBUG} backup file do not need to delete')
        except Exception, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-BackupMission-backupManage',
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()


    def deleteBackupFile(self, fileName):
        """
        删除旧的备份信息
        :param fileName:
        :return:
        """
        # 删除文件
        os.remove(self.filePath + fileName)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} backup file has been delete,file name is ' + fileName)
        pass
