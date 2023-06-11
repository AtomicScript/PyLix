# cracking linux hashes
import hashlib, sys
from passlib.hash import sha512_crypt
from pybase64 import b64encode

s = 'penguins'
for i in range(999):
    # PcSL
    ne = sha512_crypt.using(salt=s, rounds=5000).hash(str(i))
    if ne[12] == "P":
         print(i, ne)
    # from github
    if ne[12:16] == 'PcSL':
        print(i, ne)
