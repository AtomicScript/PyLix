"""
XOR TRUTH TABLE
0 x 0 = 0
0 x 1 = 1
1 x 0 = 1
1 x 1 = 0
"""

def xorEncryption():
    plaintext = input("PlainText >>: ")
    key = input("Key >>: ")
    n = len(plaintext)
    ciphertext = ''

    for i in range(n):
        t = plaintext[i]
        # len(key) : prevents you from running off the end of the key.
        k = key[i%len(key)]
        x = ord(k) ^ ord(t)
        r = str(chr(x))
        ciphertext += r
        print(t, k, x, r)
    return ciphertext

def xorDecryption(cipher):
    key = input("Enter secret key>>: ")
    n = len(cipher)
    plaintext = ''

    for i in range(n):
        t = cipher[i]
        # len(key) : prevents you from running off the end of the key.
        k = key[i%len(key)]
        x = ord(t) ^ ord(k)
        r = str(chr(x))
        plaintext += r
        print(t, k, x, r)
    return plaintext

ciphertext = xorEncryption()
plaintext = xorDecryption(ciphertext)

print('ciphertext = '+ str(ciphertext))
print('plaintext = '+ str(plaintext))
