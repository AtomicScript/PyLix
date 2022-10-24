

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

example_cipher = 'snw{fzs'
ex_k = '6'
example = xorDecryption(example_cipher, ex_k)
print(f'Plaintext = {example}')

# ciphertext = input("CipherText >>: ")
# key = input("Enter secret key>>: ")
