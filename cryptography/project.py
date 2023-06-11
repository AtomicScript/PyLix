# generate a key --> hash key --> encyrpt
# AES mode with 256 bits
# Use of SHA-256 for hashing
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import pad, unpad

def hash(text):
    hashed_string = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return hashed_string

def encrypt(plaintext, key):
    encryptor = AES.new(key.encode("utf8"), AES.MODE_CBC)
    # adding padding to fill the rest of the block
    ciphertext = encryptor.encrypt(pad(plaintext, AES.block_size))
    return ciphertext


key =  hash('zu@ac_a3')
PLAINTEXT = 'test 1234'.encode("utf8")

# HASH IS THE KEY
print("#"*23 + " KEY INFO " + "#"*23)
key = key[0:32]
print(key)
print(str(len(key)) + ' bytes key')

print("#"*23 + " Encrypting " + "#"*23)
CIPHERTEXT = encrypt(PLAINTEXT, key)
print(CIPHERTEXT)
