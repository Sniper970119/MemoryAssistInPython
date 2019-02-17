# coding=utf-8
import re
import socket
import threading
import time
import sys
import os
import struct

import re
import os
import tempfile


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1', 9000))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting client connection...')
    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    # conn.settimeout(500)
    conn.send(b'Hi, Welcome to the server!')
    while 1:
        fileinfo_size = struct.calcsize('128si2s')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize, pwd = struct.unpack('128si2s', buf)
            print("pwd : " + bytes.decode(pwd))
            # 判定密码是否正确
            file_path = './test.properties'
            property = Properties(file_path)  # 读取文件
            if property.get("pwd") == bytes.decode(pwd):
                print("password validate success!")
            else:
                print("password validate error")
                break
            # 删除byte转为str后的\x00  用strip也可以
            newFileName = bytes.decode(filename).rstrip('\x00')
            # 得到文件路径前缀
            dirPrefix = property.get(newFileName)
            if dirPrefix == None or dirPrefix == "":
                dirPrefix = property.get("defaultDir")
            new_filename = os.path.join(dirPrefix, '' + newFileName)
            print('file new name is {0}, filesize if {1}'.format(new_filename, filesize))

            recvd_size = 0  # 定义已接收文件的大小
            fp = open(new_filename, 'wb')
            print('start receiving...')
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print('end receive...')
        conn.close()
        break


class Properties:
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception:
            # raise Exception
            print("read file exception ...")
        else:
            fopen.close()

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value



if __name__ == '__main__':
    socket_service()
