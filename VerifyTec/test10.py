# coding=utf-8
import socket as s
from urlparse import urlparse


def getUrl(url):
    # 通过socket请求url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == '':
        path = '/'
    # 建立socket链接
    client = s.socket(s.AF_INET, s.SOCK_STREAM)
    client.connect((host, 80))

    client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf-8'))
    data = b''
    while True:
        # 一次获取多少数据
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf-8')
    print(data)
    client.close()

if __name__ == '__main__':
    getUrl('http://www.baidu.com')