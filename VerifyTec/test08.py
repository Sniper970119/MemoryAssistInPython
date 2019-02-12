# -*- coding:utf-8 -*-
import datetime
import time
import win32clipboard

import win32con


def settext(aString):
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_TE1XT, aString)
        win32clipboard.CloseClipboard()
    except Exception, e:
        wrongFile = open('../data/wrongMessage.dat', 'a+')
        # 获取当前时间
        currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                     '%Y-%m-%d-%H-%M-%S'))
        # 生成报错的错误信息
        wrongMessage = {
            '|currentTime': currentTime,
            '|file': 'MissionSystem-AddMission-saveConfigFile',
            '|wrongMessage': str(e)
        }
        # 存入文件
        wrongFile.write(str(wrongMessage))
        # 增加换行符
        wrongFile.write('\n')
        wrongFile.close()

a = "hello python"
# nextTime = datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), '%Y-%m-%d-%H-%M-%S')
# print(nextTime)
#
settext(a)

