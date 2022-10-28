import hashlib

hash = 'c09145ad46b058fba82e4218169c7121'
def firstPart():
    p = 'password'
    h = p
    # password is hashed 10 times
    for i in range(10):
        h = hashlib.md5(h.encode('utf-8')).hexdigest()
        print(i+1, h)

def hash100(h):
    h = h
    found = False
    for i in range(100):
        h = hashlib.md5(str(h).encode('utf-8')).hexdigest()
        print(h)
        if h == hash:
            print("Hash found")

# WORK ON IT LATER 
def secondPart():
    # 3-digit password hashed 100 times with MD5. Find it from this hash
    # password will be hashed 100 times
    # for each number it will be hashed 100 times
    for x in range(1000):
        for y in range(101):
            h = hashlib.md5(str(x).encode('utf-8')).hexdigest()
            print(x, y, h)


secondPart()
