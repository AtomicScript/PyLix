"""
DOENST WORK !
XOR TRUTH TABLE
0 x 0 = 0
0 x 1 = 1
1 x 0 = 1
1 x 1 = 0
"""
# plaintext + key + LEN
PLAINTEXT = input("PLAINTEXT >>: ")
key = input("Key >>: ")
n = len(PLAINTEXT)
num = []
# loop through
for i in range(n):
    p = PLAINTEXT[i]
    # len(key) : prevents you from running off the end of the key.
    k = key[i%len(key)]
    x = ord(k) ^ ord(p)
    print(p,ord(p), k, ord(k))
    num.append(x)

print(num)
for i in num:
    print(chr(int(i)))
