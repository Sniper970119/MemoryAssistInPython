# coding=utf-8
import os
import time

basedir = './'
filelists = []
# 指定想要统计的文件类型
whitelist = ['php', 'py']


# 遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    global filelists
    for parent, dirnames, filenames in os.walk(basedir):
        # for dirname in dirnames:
        #    getFile(os.path.join(parent,dirname)) #递归
        for filename in filenames:
            ext = filename.split('.')[-1]
            # 只统计指定的文件类型，略过一些log和cache文件
            if ext in whitelist:
                filelists.append(os.path.join(parent, filename))


# 统计一个文件的行数
def countLine(fname):
    count = 0
    for file_line in open(fname).xreadlines():
        # if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1
    print fname + '----', count
    return count


if __name__ == '__main__':
    startTime = time.clock()
    getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print '总行数:', totalline
    print '完成时间: %0.2f s' % (time.clock() - startTime)
