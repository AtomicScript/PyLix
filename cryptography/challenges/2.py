# BYTESSS
# In ASCII, each character turns into one byte
# best explaination : https://www.youtube.com/watch?v=8qkxeZmKmOY
from pybase64 import b64encode, standard_b64decode

def base64Decoder(encoded_data):
    print("Decoded Message: \n", str(standard_b64decode(encoded_data)))


# input data
data = input("Input message to decrypt >>: ").encode()
base64Decoder(data)

#Decoded Message:
# b'This is too easy'
