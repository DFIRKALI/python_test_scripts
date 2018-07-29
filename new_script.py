import json
import os
import urllib3

#this is a simple that displays OS informaion and parses some json from an API

http = urllib3.PoolManager()

r = http.requests = ("GET", "https://jsonplaceholder.typicode.com/users/")

print(r.text)

print(os.system('ifconfig'))
print(os.system('df -h'))


