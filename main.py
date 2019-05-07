# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools.showEdit import ShowEdit
from src.Client.recitationSystem.recitationSystem import RecitationSystem
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail

if __name__ == '__main__':
    m = RecitationSystem()
    # 添加
    # m.addRecitation('question1', 'answer1', weight=10)
    # m.addRecitation('question2', 'answer2', weight=20)
    # 获取一条
    # print(m.loadRecitation())
    print(m.getOneRecitation())