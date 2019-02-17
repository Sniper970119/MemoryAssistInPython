# -*- coding:utf-8 -*-
import os
from tkinter import messagebox
from src.Update.VersionControlSystem import versionControl

# 主界面
if __name__ == '__main__':
    versionControl.VersionControl().handle()
    command = 'MemoryAssist v1.0.exe'
    os.system(command)

