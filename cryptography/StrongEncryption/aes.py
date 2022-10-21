from Crypto.Cipher import AES
import hashlib

print("Advanced Encryption Standard")

# 16-byte key + plaintext = AES encryption

key =  '16 bytes key 123'
obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')

PLAINTEXT = 'secret message12'
ciphertext = obj.encrypt(PLAINTEXT)
print(f"Plaintext = {PLAINTEXT}")
print(f"Ciphertext = {ciphertext}")
