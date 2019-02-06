# -*- coding:utf-8 -*-

from src.Conf.config import *
from src.MissionSystem.SaveMission import saveMission
from src.MissionSystem.LoadMission import loadMission
from src.MissionSystem.BackupMission.tools import backupFile
from src.MissionSystem.BackupMission.tools import backupManage
from src.MissionSystem.BackupMission.tools import chooseRecoverFile


class BackupMission():
    def __init__(self, fileLimit=7, backupFilePath='../data/bkup/mbk/', missionFileName='../data/bkup/mission.dat'):
        # 初始化工具
        self.missionFileName = missionFileName
        self.fileLimit = fileLimit
        self.filePath = backupFilePath
        self.backupFileTools = backupFile.BackupFile()
        self.backupManageTools = backupManage.BackupManage(filePath=backupFilePath)
        self.chooseRecoverFileTools = chooseRecoverFile.ChooseRecoverFile(filePath=backupFilePath)
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
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} save backup file')

        # 保存备份文件
        saveMissionTools.saveMission(list=list)

        # 调用备份管理，管理备份文件
        self.backupManageTools.manage()


    def recover(self):
        """
        从备份文件中回复文件
        :return:
        """
        fileName = self.chooseRecoverFileTools.choose()
        fileName = self.filePath + fileName
        # 获取最新备份文件的文件名
        backupFileNeedToLoad = True  # 循环读取备份文件标记，直到正确读取
        while (backupFileNeedToLoad):
            try:
                loadMissionTools = loadMission.LoadMission(filename=fileName)
                list = loadMissionTools.loadMission()
                # 读取成功则跳出循环
                backupFileNeedToLoad = False
                # 判断文件是否真的读取成功了（读取失败返回None）
                if list is None:
                    # 打印debug日志
                    if DEBUG and MISSION_DEBUG:
                        print('{SYS}{W}{MISSION_DEBUG} load backup file fail, return list is None, file name is '
                              + fileName)
                    # 如果是读取失败将循环标记改回，继续下次读取
                    backupFileNeedToLoad = True
            except:
                # 打印debug日志
                if DEBUG and MISSION_DEBUG:
                    print('{SYS}{W}{MISSION_DEBUG} backup file load fail,name is ' + fileName)

        # 将从配置文件读取的信息保存
        saveMissionTools = saveMission.SaveMission(filename=self.missionFileName)
        saveMissionTools.saveMission(list=list)



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
