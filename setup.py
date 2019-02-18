# coding=utf-8
from esky import bdist_esky
from setuptools import setup
from src.Client.Conf.config import *

# Common settings
# python -m SimpleHTTPServer
exeICON = './images/icon.ico'  # 打包成exe的图标
NAME = "MemoryAssist"  # 打包后显示的文件名
FREEZER = 'cx_Freeze'

# "includes": [""]    #引用额外的包
FREEZER_OPTIONS = {
    "excludes": ["tkinter"],
    "includes": ["pyttsx3.drivers.sapi5", "win32com.server.util"],
    "packages": ["wx"]
}

APP = [bdist_esky.Executable("test_esky.py",  # 出文件入口
                             gui_only=True,  # 不显示cmd窗口
                             icon=exeICON,
                             )]

# show.icon、config.txt：打包后保留的文件
DATA_FILES = [('', ['show.ico', 'config.txt'])]

ESKY_OPTIONS = dict(freezer_module=FREEZER,
                    freezer_options=FREEZER_OPTIONS,
                    enable_appdata_dir=False,
                    bundle_msvcrt=False,
                    )

# Build the app and the esky bundle
setup(name=NAME,
      version=VERSION,
      scripts=APP,
      data_files=DATA_FILES,
      options=dict(bdist_esky=ESKY_OPTIONS),
      )
