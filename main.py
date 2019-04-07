# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools.showEdit import ShowEdit
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail
# from src.Client.SystemTools.ConfFileRead.configFileRead import ConfigFileRead
#
# a = ConfigFileRead().readFile('USER_CODE', 'user_code')
# print(a == '')
# # print()
# SendEmail().send()

ShowEdit().window()