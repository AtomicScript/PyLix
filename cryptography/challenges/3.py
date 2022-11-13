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


# will come back to it later
def bruteTwoDigitKey():
    hex_cipher = '70155d5c45415d5011585446424c'
    byte_array = bytearray.fromhex(hex_cipher)
    cipher = byte_array.decode('ascii')
    n = len(cipher)
    # key is two digit so
    for x in '0123456789':
        for y in '0123456789':
            key = x + y
            plaintext = ''
            print(ord(str(key)))


example_cipher = 'snw{fzs'
ex_k = '6'
example = xorDecryption(example_cipher, ex_k)
print(f'Plaintext = {example}')

# lets make brute furcing the key but numbers?
ciphertext = 'khoor'
bruteOneDigitKey(ciphertext)
bruteTwoDigitKey()
