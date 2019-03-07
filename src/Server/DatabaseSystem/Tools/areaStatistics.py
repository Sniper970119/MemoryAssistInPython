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
        weekly_area = []
        total_area = []
        for each in self.weeklyCol.find():
            ips = each['user_ip']
            for ip in ips:
                user_ip = ip.keys()[0]
                # 将ip转换回来
                user_ip = user_ip.replace('\\', '.')
                # 获取ip信息
                message = self.handleRequest(user_ip)
                # 修改地区字典
                if message in weekly_area:
                    weekly_area[message] = weekly_area[message] + 1
                else:
                    weekly_area[message] = 1
            pass

        for each in self.totalCol.find():
            ips = each['user_ip']
            for ip in ips:
                user_ip = ip.keys()[0]
                # 将ip转换回来
                user_ip = user_ip.replace('\\', '.')
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
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + str(ip)
        r = requests.get(url)
        distMessage = json.loads(r.text)
        # 解析字典，生成信息
        ipMessage = '国家:' + str(distMessage['data']['country']) + '地区：' + distMessage['data']['area'] + '省份：' + \
                    distMessage['data']['region'] + '城市' + distMessage['data']['city']
        return ipMessage
