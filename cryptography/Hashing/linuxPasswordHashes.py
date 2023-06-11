# Salting is the procedure of adding random characters before hashing
# LINUX PASSWORD HASHING You perform an algorithm that includes 5,000 rounds of SHA-512 hashing
import hashlib, sys
from passlib.hash import sha512_crypt
from pybase64 import b64encode

salt = 'python123'.encode()
encoded_salt = b64encode(salt).decode()
ne = sha512_crypt.using(salt=encoded_salt, rounds=5000).hash("P@sw0rd")
print(ne)
