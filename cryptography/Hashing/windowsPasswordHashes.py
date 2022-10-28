import hashlib
# cracking
# notes --> windows hashes use NT HASH

# MICROSOFT ALGORITHM
def microAlg(password):
    # encodes in unicode --> run it though MD54 = NT hash
    encoded_password = password.encode("utf-16le")
    nt_hashed_password = hashlib.new('md4', encoded_password).hexdigest()
    print(f'{password} >> encoded : {encoded_password} >> NT hash : {nt_hashed_password}')
    return nt_hashed_password

# CRACKING MICROSOFT ALGORTITHM
def crackingNTH(password, guess):
    for c in '0123456789':
        p = guess + c
        ep = p.encode("utf-16le")
        nthp = hashlib.new('md4', ep).hexdigest()
        print(f'{p} >> NT hash : {nthp}')
        if hashed_password == nthp:
            print("Password FOUND")
            print(f'{p} >> NT hash : {nthp}')
            break


password = 'P@sw0rd992'
guess = 'P@sw0rd99'
hashed_password = microAlg(password)
hashed_guess = crackingNTH(hashed_password, guess)
