# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools.showEdit import ShowEdit
from src.Client.recitationSystem.recitationSystem import RecitationSystem
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Client.SystemTools.LoadFiles import loadFiles

if __name__ == '__main__':
    list1 = loadFiles.LoadFiles('./data/recitation.dat').loadFiles(missionType='recitation')
    print(list1)
    # m = RecitationSystem()
    # 添加
    # m.addRecitation('注意', '', weight=0)
    # m.addRecitation('question2', 'answer2', weight=20)
    # 获取一条
    # print(m.loadRecitation())
    # m.editRecitation(recitationId='000001',
    #                  answer='由于某种原因，最好不要将所有的背诵清空，请保留本条，本条权重已经设为0，不会在提问中出现（只会在只剩本条时出现），那么就请从右侧添加背诵开始吧~',weight=0,isEdit=True)
    # print(m.getOneRecitation())
    # print(type(configFileRead.ConfigFileRead().readFile('EMAIL', 'email_code'))
    # str = '''
    # 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈'''
    # print(len(str))



    pass