# learnt : NO NEED TO / INSTEAD OF ^ XOR UNDOS IT SELF
# weirdly ord has problem when its two digit number...

def xorDecryption(cipher, key):
    n = len(cipher)
    plaintext = ''
    for i in range(n):
        t = cipher[i]
        # len(key) : prevents you from running off the end of the key.
        k = key[i%len(key)]
        x = ord(t) ^ ord(k)
        r = str(chr(x))
        plaintext += r
    return plaintext

def bruteOneDigitKey(cipher):
    n = len(cipher)
    for k in range(1, 10):
        k = str(k)
        plaintext = ''
        for i in range(n):
            t = cipher[i]
            x = ord(k) ^ ord(t)
            plaintext += str(chr(x))
        print(f'{k} : {plaintext}')

# 70155d5c45415d5011585446424c
def bruteTwoDigitKey():
    # WORK ON IT LATER
    hex_cipher = input('>>: ').decode('hex')
    print(t)
    n = 2
    # stackoverflow
    # new_hex_cipher = [hex_cipher[i:i+n] for i in range(0, len(hex_cipher), n)]
    # print(ord(str(i)))
    # text += str(ord(str(i)))




example_cipher = 'snw{fzs'
ex_k = '6'
example = xorDecryption(example_cipher, ex_k)
print(f'Plaintext = {example}')

# lets make brute furcing the key but numbers?
ciphertext = 'khoor'
bruteOneDigitKey(ciphertext)
bruteTwoDigitKey()
