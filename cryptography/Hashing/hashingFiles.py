import hashlib

file = 'cryptography/Hashing/tobehashed.txt'

def hfmd5(file):
    with open(file, 'rb') as f:
        content = f.read()
        # hashes the content of the file
        hashed_content = hashlib.md5(content)
        return hashed_content.hexdigest()
    
def hfsha1(file):
    with open(file, 'rb') as f:
        content = f.read()
        # hashes the content of the file
        hashed_content = hashlib.sha1(content)
        return hashed_content.hexdigest()
    
def hfsha256(file):
    with open(file, 'rb') as f:
        content = f.read()
        # hashes the content of the file
        hashed_content = hashlib.sha256(content)
        return hashed_content.hexdigest()

print(hfsha1(file))

