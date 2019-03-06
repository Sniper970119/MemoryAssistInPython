import random
import string
import re

# salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
# print(salt)
address = "('127.0.0.1', 63087)"
address = re.findall('\'(.*?)\'', address)[0]
address = address.replace('\.', '\\.')
print(address)
