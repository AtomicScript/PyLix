# padding is used when the last block cannot be filled so bytes are added to fill it
# NOTE COME BACK TO THIS LATER I DONT FULLY UNDERSTAND IT
from Crypto.Cipher import AES
import hashlib

# from page 94
iv = "1111222233334444"
key =  'Sixteen byte key'

# adds padding thats divisale by 16 [if 10 it will add 6 padds to make it 16]
def padding(plaintext):
    padbytes = 16 - len(plaintext) % 16
    pad = padbytes * chr(padbytes)
    return plaintext + pad


def remove_padding(PLAINTEXT):
    l = len(PLAINTEXT)  # example length is 16
    x = ord(PLAINTEXT[l-1]) # ord of 15
    print(x)
    if x > 16 or x < 1:
        return "PADDING ERROR"
    if PLAINTEXT[l-x:] != chr(x)*x:
        return "PADDING ERROR"
    return PLAINTEXT


def encr(PLAINTEXT):
    obj = AES.new(key, AES.MODE_CBC, iv)
    new_plaintext = padding(PLAINTEXT)
    print(new_plaintext)
    ciphertext = obj.encrypt(new_plaintext)
    return ciphertext


def decr(CIPHERTEXT):
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(PLAINTEXT)
    return plaintext
