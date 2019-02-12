# -*- coding:utf-8 -*-
import win32clipboard

import win32con


def settext(aString):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_TEXT, aString)
    win32clipboard.CloseClipboard()

a = "hello python"
settext(a)

