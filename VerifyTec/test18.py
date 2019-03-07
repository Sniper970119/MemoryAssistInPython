import requests
import json

import simplejson as simplejson

# url = 'http://ip.taobao.com/service/getIpInfo.php?ip=127.0.0.1'
# r = requests.get(url)
# mes = r.text
# # a = dict(r.text)
# a = json.loads(r.text)
# b = a['data']['country'] + a['data']['area'] + a['data']['region'] + a['data']['city']
# print(b)
# print(type(str(a['data']['city'])))
from src.Server.DatabaseSystem.Tools.areaStatistics import AreaStatistics

areaTools = AreaStatistics()
weeklyArea, totalArea = areaTools.statistics()
a = json.dumps(weeklyArea).encode('utf-8').decode('unicode_escape')
print(a)
