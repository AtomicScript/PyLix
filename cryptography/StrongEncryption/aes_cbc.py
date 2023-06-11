from Crypto.Cipher import AES
import hashlib

print("Advanced Encryption Standard - CBC")
# 16-byte key + plaintext = AES encryption
# block = 128 bits

# key sizes = 16, 32, 64, 128, 192, 256
key =  '16 bytes key 123'
print(str(len(key)) + ' bytes key')
obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')

PLAINTEXT = 'secret message12' * 3
ciphertext = obj.encrypt(PLAINTEXT)


print(f'K{len(key)} + PT{len(PLAINTEXT)} = {len(key) + len(PLAINTEXT)}')
print(f"Plaintext = {PLAINTEXT}")
print(f"Ciphertext = {ciphertext}")
