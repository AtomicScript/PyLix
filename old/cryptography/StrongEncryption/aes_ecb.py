from Crypto.Cipher import AES

print("Advanced Encryption Standard - ECB")
key = 'abcdefghijklmnop'
print(f'Length of the key is {len(key)}')
obj = AES.new(key, AES.MODE_ECB)

PLAINTEXT = 'secret message12'
ciphertext = obj.encrypt(PLAINTEXT)

print(f'K{len(key)} + PT{len(PLAINTEXT)} = {len(key) + len(PLAINTEXT)}')
print(f"Plaintext = {PLAINTEXT}")
print(f"Ciphertext = {ciphertext}")
