from cryptography.fernet import Fernet
import hashlib

def encry(code):

    key = Fernet.generate_key()
    f = Fernet(key)

    what_b = str.encode(code)
    token = f.encrypt(what_b)

    with open("string.txt", "wb") as f1, open("key.txt", "wb") as f2:
        f1.write(token)
        f2.write(key)


username  = '1010010722236'
r = hashlib.md5(str.encode(username[:10]))
encry(r.hexdigest())
