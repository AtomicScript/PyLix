# needed to import it
# Use module Crypto.Cipher.PKCS1_OAEP instead
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# generate the key
def genKey():
    # generate a key
    keyPair = RSA.generate(2048)

    # Public key and private key
    pubKey = keyPair.publickey().exportKey("PEM")
    privKey = keyPair.exportKey("PEM")

    with open("keys/private_key.pem", "wb") as file:
        file.write(privKey)

    with open("keys/public_key.pem", "wb") as file:
        file.write(pubKey)


# encrypting a PLAINTEXT
def encrypting(PLAINTEXT):
    # encrypting
    key = RSA.import_key(open('keys/public_key.pem').read())
    encryptor = PKCS1_OAEP.new(key)
    CIPHERTEXT = encryptor.encrypt(PLAINTEXT)
    return CIPHERTEXT


# encrypting a CIPHERTEXT
def decrypting(CIPHERTEXT):
    key = RSA.import_key(open('keys/private_key.pem').read())
    cipher = PKCS1_OAEP.new(key)
    PLAINTEXT = cipher.decrypt(CIPHERTEXT)
    return PLAINTEXT


# PLAINTEXT
MSG = b"encrypt this message"
genKey()
CIPHERTEXT = encrypting(MSG)
print(CIPHERTEXT)
PLAINTEXT = decrypting(CIPHERTEXT)
print(PLAINTEXT.decode('utf-8'))
