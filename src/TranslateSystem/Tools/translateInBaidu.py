# -*- coding:utf-8 -*-
from src.Conf.config import *

import httplib
import md5
import urllib
import random
import re

appid = '20190210000265097'  # 你的appid
secretKey = 'FN5ZzcxZIt41MWthQexp'  # 你的密钥


class Translate():
    def translate(self, q):
        """
        使用百度翻译进行翻译
        :param q: 需要被翻译的文本（英汉均可）
        :return: 翻译后的文本
        """
        httpClient = None
        myurl = '/api/trans/vip/translate'
        fromLang = 'auto'
        toLang = 'auto'
        salt = random.randint(32768, 65536)

        sign = appid + q + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            res = response.read().encode('latin-1').decode('unicode_escape')
            # 分割返回结果，将unicode转化为中文并输出
            result = re.findall('"dst":"(.*?)"', res)[0]
            if DEBUG and SEARCH_DEBUG:
                print('{SYS}{SEARCH_DEBUG} word has been translate, result is ' + result)
            return result
        except Exception, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'TranslateSystem-Tools-translateInBaidu',
                '|translateText': q,
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None
        finally:
            if httpClient:
                httpClient.close()


if __name__ == '__main__':
    Translate().translate('火车')
