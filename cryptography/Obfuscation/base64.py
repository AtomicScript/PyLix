# BYTESSS
# In ASCII, each character turns into one byte
# best explaination : https://www.youtube.com/watch?v=8qkxeZmKmOY
from pybase64 import b64encode, standard_b64decode

def base64Encode(data):
    # encode data
    encoded_data = b64encode(data)

    # output data
    print("Encoded Message: \n", str(encoded_data))

    # returns it
    return encoded_data

def base64Decoder(encoded_data):
    print("Decoded Message: \n", str(standard_b64decode(encoded_data)))

# input data
data = input("Input message to encrypt >>: ").encode()
# base64
encoded_data = base64Encode(data)
base64Decoder(encoded_data)
