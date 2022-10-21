import hashlib

text = 'This is the traffic status information'

hashed_string = hashlib.sha256(text.encode('utf-8')).hexdigest()

print(hashed_string)
