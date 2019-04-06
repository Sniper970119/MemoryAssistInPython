# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.SystemTools.ConfFileRead import configFileRead
from src.Client.MessageTransferSystem.MarkUser import markUser

# 主界面
if __name__ == '__main__':
    """
    程序开始前的准备
    """
    # 对登录次数进行更新
    configFileReadTools = configFileRead.ConfigFileRead(fileName="./conf/user.ini")
    logTime = configFileReadTools.readFile('USER_CODE', 'user_time')
    logTime = int(logTime)
    logTime = str(logTime + 1)
    configFileReadTools.saveFile('USER_CODE', 'user_time', logTime)
    # 尝试向服务器请求用户识别码或者想服务器发送当前登录次数
    markUserTools = markUser.MarkUser()
    markUserTools.judge()
    """
    调用主窗口
    """
    mainFrame.MainFrame()
    # f = open('./../data/mission.dat')
    # print(f.read())

"""
打包用语句 
"""
# sphinx-apidoc -o ./source ../src

# pyinstaller mainS.py -i ./images/icon.ico

# pyinstaller mainC.py -i ./images/icon.ico -w -n run

#