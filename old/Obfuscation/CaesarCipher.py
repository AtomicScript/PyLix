
PLAINTEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# finding strings 
print(PLAINTEXT.find('A'))  # should be 0 


def CaesarEncrypter(str_in, shift):
    length = len(str_in)
    str_out = ''

    for i in range(length):
        c = str_in[i]                   # gets each letter 
        loc = PLAINTEXT.find(c)         # get the index of the letter
        # % MODULO OPERATION RETURNS REMAINDER
        new_loc = (loc + shift)%26      # gets the new index by adding shift
        # what if its more than the 26?
        # if new_loc > 26: THIS WONT WORK EXAMPLE SHIFT 40 
        #    new_loc -= 26 #
        str_out += PLAINTEXT[new_loc]   # get the new letter from
        # print 
        print(f"{c} {loc} {new_loc} --> {str_out}")  

    print(f"Obfuscated Version: {str_out}")

def ROT13Encrypter(str_in):
    shift = 13
    CaesarEncrypter(str_in, shift)

# # make sure its upper since PLAINTEXT is all in upper
str_in = input("Text >>: ").upper()
shift = int(input("Shift >>: "))


CaesarEncrypter(str_in, shift)
ROT13Encrypter(str_in)
