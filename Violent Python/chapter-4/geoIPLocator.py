# import pygeoip
import requests
import json

# IP ADDRESS
test = "139.130.4.5"
# url
url = f'https://geolocation-db.com/jsonp/{test}'

# requests
r = requests.get(url)
# NEEDS TO BE DECODED OR ERROR
content = r.content.decode()
# CLEANING IT
con = content.split("(")[1].strip(")")
# LOADING IT AS A JSON
result = json.loads(con)
# PRINTING OUT THE INFORMATION
print("#### [ESTIMATED LOCATION] ####")
print(f'[+] IPV4: {result["IPv4"]}')
print(f'[+] Country: {result["country_name"]}')
print(f'[+] City: {result["city"]}')
print(f'[+] State: {result["state"]}')
print(f'[+] Lat: {result["latitude"]}')
print(f'[+] Long: {result["longitude"]}')
