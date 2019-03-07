import requests
import json

import simplejson as simplejson

url = 'http://ip.taobao.com/service/getIpInfo.php?ip=219.242.98.111'
r = requests.get(url)
mes = r.text
# a = dict(r.text)
a = json.loads(r.text)
b = a['data']['country'] + a['data']['area'] + a['data']['region'] + a['data']['city']+ a['data']['isp']
print(b)
