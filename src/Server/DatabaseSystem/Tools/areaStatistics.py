# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class AreaStatistics():
    """
    用户ip地区统计
    """

    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["MemoryAssist"]
        self.totalCol = mydb["total_user"]
        self.weeklyCol = mydb["weekly_user"]
        pass

    def statistics(self):
        """
        统计用户ip地区
        :return: 周统计地区字典和全部地区统计字典
        """
        weekly_area = {}
        total_area = {}
        ip_cache = {}
        for each in self.weeklyCol.find():
            ips = each['user_ip']
            for ip in ips:
                # user_ip = ip.keys()[0]
                user_ip = ip
                # 将ip转换回来
                user_ip = user_ip.replace('\\', '.')
                # 获取ip信息
                message = self.handleRequest(user_ip)
                # 将ip存入缓存，节省下次调用
                ip_cache[user_ip] = message
                # 修改地区字典
                if message in weekly_area:
                    weekly_area[message] = weekly_area[message] + 1
                else:
                    weekly_area[message] = 1
            pass

        for each in self.totalCol.find():
            ips = each['user_ip']
            for ip in ips:
                # user_ip = ip.keys()[0]
                user_ip = ip
                # 将ip转换回来
                user_ip = user_ip.replace('\\', '.')
                if user_ip in ip_cache:
                    print('find cache')
                    message = ip_cache[user_ip]
                else:
                    message = self.handleRequest(user_ip)
                if message in total_area:
                    total_area[message] = total_area[message] + 1
                else:
                    total_area[message] = 1
            pass
        return weekly_area, total_area
        pass

    def handleRequest(self, ip):
        """
        处理ip
        :param ip: 需要识别的ip
        :return: ip的地区
        """
        # ip = '124.93.200.212'
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + str(ip)
        print(url)
        r = requests.get(url)
        print(r.status_code)
        distMessage = json.loads(r.text)
        ipMessage = ''
        # 处理编码
        reload(sys)
        sys.setdefaultencoding("utf-8")
        # 解析字典，生成信息
        if r.text.find('country') != -1:
            ipMessage = '国家:' + str(distMessage['data']['country'])
        if r.text.find('area') != -1:
            ipMessage = ipMessage + '\t地区：' + str(distMessage['data']['area'])
        if r.text.find('region') != -1:
            ipMessage = ipMessage + '\t省份：' + str(distMessage['data']['region'])
        if r.text.find('city') != -1:
            ipMessage = ipMessage + '\t城市：' + str(distMessage['data']['city'])
        return ipMessage
