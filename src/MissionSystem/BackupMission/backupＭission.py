# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.MissionSystem.SaveMission import saveMission
from src.MissionSystem.LoadMission import loadMission
from src.MissionSystem.BackupMission.tools import backupFile
from src.MissionSystem.BackupMission.tools import backupManage
from src.MissionSystem.BackupMission.tools import chooseRecoverFile


class BackupMission():
    def __init__(self, fileLimit=7, backupFilePath='../data/bkup/mbk/', missionFileName='../data/bkup/mission.dat'):
        self.missionFileName = missionFileName
        self.fileLimit = fileLimit
        self.filePath = backupFilePath
        self.backupFileTools = backupFile.BackupFile()
        self.backupManageTools = backupManage.BackupManage(filePath=backupFilePath)
        self.chooseRecoverFileTools = chooseRecoverFile.ChooseRecoverFile(filePath=backupFilePath)

        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} ready for backup mission')
        pass

    def backup(self, list):
        """
        备份文件
        :param list: 需要备份的列表
        :return:
        """
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
        """
        从备份文件中回复文件
        :return:
        """
        fileName = self.chooseRecoverFileTools.choose()
        fileName = self.filePath + fileName
        # 获取最新备份文件的文件名
        backupFileNeedToLoad = True  # 循环读取备份文件，直到正确读取
        while (backupFileNeedToLoad):
            try:
                loadMissionTools = loadMission.LoadMission(filename=fileName)
                list = loadMissionTools.loadMission()
                backupFileNeedToLoad = False
            except:
                if DEBUG and MISSION_DEBUG:
                    print('{SYS}{W}{MISSION_DEBUG} backup file load fail,name is ' + fileName)

        # 将从配置文件读取的信息保存
        saveMissionTools = saveMission.SaveMission(filename=self.missionFileName)
        saveMissionTools.saveMission(list=list)

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

    b = BackupMission(backupFilePath='F:\python17\pythonPro\MemortAssit\data/bkup/mbk/',
                      missionFileName='F:\python17\pythonPro\MemortAssit\data\mission.dat')
    # 测试备份
    # b.backup(dataList)
    # 测试读取备份
    b.recover()
