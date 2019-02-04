# -*- coding:utf-8 -*-

from src.Conf.config import *


class BackupManage():
    def __init__(self, filePath='../data/bkup/'):
        self.filePath = filePath
        pass

    def manage(self):
        files = os.listdir(self.filePath)
        minFileName = None
        minFileTime = 0
        # 保持7个备份
        if len(files) > 7:
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} backup file need to delete')
            for file in files:
                if minFileTime == 0:
                    minFileTime = os.path.getctime(self.filePath + '/' + file)
                    minFileName = file
                else:
                    if minFileTime > os.path.getctime(self.filePath + '/' + file):
                        minFileTime = os.path.getctime(self.filePath + '/' + file)
                        minFileName = file
            self.deleteBackupFile(minFileName)
        else:
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} backup file do not need to delete')
        pass

    def deleteBackupFile(self, fileName):
        os.remove(self.filePath + fileName)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} backup file has been delete,file name is ' + fileName)
        pass
