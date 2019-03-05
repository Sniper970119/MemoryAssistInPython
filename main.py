# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.SystemTools.ConfFileRead.configFileRead import ConfigFileRead

a = ConfigFileRead().readFile('USER_CODE', 'user_code')
print(a == '')
# print()
