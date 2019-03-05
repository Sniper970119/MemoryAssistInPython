import random
import string

salt = ''.join(random.sample(string.ascii_letters + string.digits, 32))
print(salt)