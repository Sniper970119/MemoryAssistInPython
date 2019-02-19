# -*- coding:utf-8 -*-
import binascii
import pickle

from src.Client.Conf.config import *



class EncodeText():
    """
    编码文件类，将需要保存的列表序列化并加密。实际操作类。
    """
    def encodeing(self, data):
        """
        将列表加密
        :param data: 需要加密的列表
        :return: 加密后的结果
        """
        try:
            # 首先将列表序列化
            byte_data = pickle.dumps(data)
            # 进制转换加密
            encodeText = binascii.b2a_hex(byte_data)
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} list has been encode successfully')
            return encodeText
        except Exception, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-SaveMission-encodeText',
                '|data': data,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None
