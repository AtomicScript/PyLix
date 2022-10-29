import hashlib

hash = 'c09145ad46b058fba82e4218169c7121'
p = 'password'
found = False

def firstPart(p):
    global found
    h = p
    if found == False:
        # password is hashed 10 times
        for i in range(100):
            h = hashlib.md5(str(h).encode('utf-8')).hexdigest()
            if h == hash:
                print("HASH HAS BEEN FOUND")
                print(f'Password : {p}, Hash : {h}')
                found = True
                break
            print(p, i+1, h)

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
    # Password : 373, Hash : c09145ad46b058fba82e4218169c7121
    for x in range(1000):
        if not found:
            firstPart(x)


secondPart()
