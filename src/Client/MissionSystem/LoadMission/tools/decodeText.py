# -*- coding:utf-8 -*-
import binascii
import pickle

from src.Client.Conf.config import *


class DecodeText():
    """
    负责解码文本，将加密的文档解密并解序列化。实际操作类。
    """
    def decodeing(self, data):
        """
        解密
        :param data: 需要被解密的数据
        :return: 解密后的列表
        """
        try:
            # 将文本转换进制
            byte_data = binascii.a2b_hex(data)
            # 反序列化
            list = pickle.loads(byte_data)
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} list has been decode successfully')
            return list
        except Exception as e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-LoadMission-decodeText',
                '|data': data,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None



