import hashlib

def compareHashes(t1, t2):
    if t1 == t2:
        print('Hashes match')

def hashMD5(text):
    hashed_string = hashlib.md5(text.encode('utf-8')).hexdigest()
    return hashed_string

def hashSHA1(text):
    hashed_string = hashlib.sha1(text.encode('utf-8')).hexdigest()
    return hashed_string

# SHA-2
def hashSHA256(text):
    hashed_string = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return hashed_string

# SHA-2
def hashSHA512(text):
    hashed_string = hashlib.sha512(text.encode('utf-8')).hexdigest()
    return hashed_string


text = 'This is the traffic status information'

hashed_text1 = hashMD5(text)
hashed_text2 = hashSHA1(text)
hashed_text3 = hashSHA256(text)
hashed_text4 = hashSHA512(text)

print(f'MD5 : {hashed_text1}')
print(f'SHA1 : {hashed_text2}')
print(f'SHA256 : {hashed_text3}')
print(f'SHA518 : {hashed_text4}')
