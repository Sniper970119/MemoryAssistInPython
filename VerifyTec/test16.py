import random
import string
import re

# salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
# print(salt)
address = '127.0.0.1:123454'
address = re.findall('(.*?):',address)[0]
print(address)
