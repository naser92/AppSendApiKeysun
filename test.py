import hashlib
from cryptography.fernet import Fernet
import json


r = hashlib.md5(b'0015194094')

print (r.hexdigest())
key = Fernet.generate_key()
f = Fernet(key)
b = str(r.hexdigest())
print (b)
token = f.encrypt(b'c9f1b63516f1bd2999c911ca3ec78bd7')
data = {
    "token" : token
}

with open('personal.txt', 'w') as json_file:
    json_file.write(str(token))