# -*- coding:utf-8 -*-
import datetime
import time

localtime = time.asctime(time.localtime(time.time()))
t = time.gmtime()
print(t.tm_year)
print ("时间：" + localtime)

# 格式化日期
print (time.strftime("%Y-%m-%d", time.localtime()))
time_ = '2019-02-01'
a1 = datetime.datetime.strptime(time_, '%Y-%m-%d')
a2 = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d')

print('s_time is:', a1 + datetime.timedelta(days=1))
print('s_time is:', a1)
print('e_time is:', a2)
print(a2.strftime("%Y-%m-%d"))
print(a1 - a2)

currentDate = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d').strftime(
    "%Y%m%d")
print(currentDate)
