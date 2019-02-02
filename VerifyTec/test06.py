# -*- coding:utf-8 -*-
import binascii
import pickle

f = open('F:\python17\pythonPro\MemortAssit\data\mission.dat', 'wb')
dic = {'age': 23, 'job': 'student'}
# 首先将列表序列化
byte_data = pickle.dumps(dic)
# 进制转换加密
encodeText = binascii.b2a_hex(byte_data)
print(encodeText)
encodeText = '哈哈哈'.encode('utf-8')
print(type(encodeText))
f.write(encodeText)
f.close()
