import socket
import datetime
import time
from tkinter import messagebox
import ConfigParser
import struct
import zipfile
import shutil
import os

SERVER_IP = 'memoryassist.sniper97.cn'
# SERVER_IP = '140.143.147.128'
# SERVER_IP = '127.0.0.1'
SERVER_FILE_PORT = 9000
SERVER_MES_PORT = 9001

DEBUG = True
SYSTEM_TOOLS_DEBUG = True
VERSION_CONTROL_DEBUG = True
