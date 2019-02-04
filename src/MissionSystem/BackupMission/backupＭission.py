# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.MissionSystem.SaveMission import saveMission
from src.MissionSystem.BackupMission.tools import backupFile
from src.MissionSystem.BackupMission.tools import backupManage
from src.MissionSystem.BackupMission.tools import chooseRecoverFile


class BackupMission():
    def __init__(self, fileLimit=7, filePath='../data/bkup/'):
        self.fileLimit = fileLimit
        self.filePath = filePath
        self.backupFileTools = backupFile.BackupFile()
        self.backupManageTools = backupManage.BackupManage(filePath=filePath)
        self.chooseRecoverFileTools = chooseRecoverFile.ChooseRecoverFile()

        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for backup mission')
        pass

    def backup(self, list):
        # 使用当前时间作为备份文件名
        currentTime = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d').strftime(
            "%Y%m%d")
        fileName = self.filePath + currentTime + '.dat'
        # 由于文件名发生变化，只能在这里初始化保存工具
        saveMissionTools = saveMission.SaveMission(filename=fileName)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} save backup file')
        # 保存
        saveMissionTools.saveMission(list=list)

        # 调用备份管理，管理备份文件
        self.backupManageTools.manage()

        pass

    def recover(self):
        pass


if __name__ == '__main__':
    dataList = []
    for i in range(1, 21):
        # 先封装成字典，方便后期删除
        dir = {
            'missionId': str(i).zfill(6),
            'bookName': 'bookName' + str(i).zfill(2),
            'missionRange': 'missionRange' + str(i).zfill(2),
            'nextTime': 'nextTime' + str(i).zfill(2),
            'missionState': 'state' + str(i).zfill(2),
            'loopTime': 5,
            'isFinish': False
        }

        dataList.append(dir)

    b = BackupMission(filePath='F:\python17\pythonPro\MemortAssit\data/bkup/')
    # 测试备份
    b.backup(dataList)
