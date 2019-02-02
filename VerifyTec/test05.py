# -*- coding:utf-8 -*-
import binascii
# from idna import unichr
#
# key = 0xff
#
#
# def encrypt(src):
#     return ''.join([unichr(ord(x) ^ key) for x in src]).encode('utf-8').encode('hex').upper()
#
#
# def decrypt(src):
#     return ''.join([unichr(ord(x) ^ key) for x in src.decode('hex').decode('utf-8')])
#
#
# a = u'中国'
# print(encrypt(a))
# print(decrypt(encrypt(a)))

text = '这是一个文本'
print(text)
print(text.encode())
print(binascii.b2a_hex(text.encode()))
print(binascii.a2b_hex(binascii.b2a_hex(text.encode())))
print(binascii.a2b_hex(binascii.b2a_hex(text.encode())).decode())
