# -*- coding:utf-8 -*-
import socket
import datetime
import time
import os
import struct
import threading
# import configparser as ConfigParser
import ConfigParser
import random
import string
import pymongo
import re
import smtplib
from email.mime.text import MIMEText
import requests
import json
import sys
import schedule

SERVER_IP = '127.0.0.1'

# 调试模式总开关
DEBUG = True
#
VERSION_CONTROL_DEBUG = True

SYSTEM_TOOLS_DEBUG = True

CODE_HANDLE_DEBUG = True

MEAL_SYSTEM_DEBUG = True

# 邮件授权码
EMILECODE = 'jndmaedgdbkpbigc'