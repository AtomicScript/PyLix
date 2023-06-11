import hashlib

hash1 = '5875f2524bbe45f3504236b75a9a483d'
hash2 = '0342db37d0a08a6ea2284584876cced0'


def twoDigitMicroCrack():
    find = False
    for i in range(0,99):
        digit = str(i)
        ep = digit.encode('utf-16le')
        nthp = hashlib.new('md4', ep).hexdigest()
        # print(f'trying {digit} : {nthp}')
        if nthp == hash1:
            print("PASSWORD FOUND")
            print(f'password = {digit}')
            find = True
            break
        if find:
            break


def SDigitMicroCrack():
    find = False
    for i in range(0,9999999):
        digit = str(i)
        ep = digit.encode('utf-16le')
        nthp = hashlib.new('md4', ep).hexdigest()
        if nthp == hash2:
            print("PASSWORD FOUND")
            print(f'password = {digit}')
            find = True
            break
        if find:
            break



twoDigitMicroCrack()    # 37
SDigitMicroCrack()      # 4512672
