ALPHA ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decryptCC(ciphertext, shift):
    length = len(ciphertext)
    str_out = ''

    for i in range(length):
        c = ciphertext[i]
        loc = ALPHA.find(c)
        new_location = (loc + shift)%26
        str_out += ALPHA[new_location]

    return str_out



ciphertext = input("Enter the ciphertext = ").upper()
for i in range(0, 27):
    text = decryptCC(ciphertext, i)
    print(f"Shift {i}, Plaintext = {text}")

print("Hidden: ")
print(decryptCC(ciphertext, 16))
