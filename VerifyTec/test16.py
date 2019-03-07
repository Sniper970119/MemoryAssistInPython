import random
import string
import re

# salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
# print(salt)
address = "('127.0.0.1', 63087)"
address = re.findall('\'(.*?)\'', address)[0]
address = address.replace('.', '\\')
print(address)


# import pymongo
#
# myclient = pymongo.MongoClient("localhost:27017")
# mydb = myclient["MemoryAssist"]
# totalCol = mydb["total_user"]
# weeklyCol = mydb["weekly_user"]
# dictInTotal = {
#                 'user_code': '123456',
#                 'total_time': '1',
#                 'user_ip': {'127/0/0/1': '1'},
#             }
# totalCol.insert_one(dictInTotal)