from padding import encr, decr

PLAINTEXT = "This is simple sentence is forty-seven bytes long."
print(f"LENGTH : {len(PLAINTEXT)}")
c = encr(PLAINTEXT)
print(c)
print(f"NEW LENGTH : {len(c)}")

PLAINTEXT = "this ten !"
print(f"LENGTH : {len(PLAINTEXT)}")
c = encr(PLAINTEXT)
print(c)
print(f"NEW LENGTH : {len(c)}")
