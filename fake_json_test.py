import datetime
import os, sys
import json
import requests
from datetime import date
import time
from collections import defaultdict, Counter
import socket

MY_PATH = 'new_database.sqlite3'

#Python script to triage network an
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect (('www.theuselessweb.com', 80))

print("Socket Info and IP Address:", s)

def system_configs():
	"""Prints system information IP address, disk info and uname"""
	os.system('ipconfig')
	os.system('df -h')
	os.system('uname')

system_configs()

username_dict = defaultdict(int)

r = requests.get("\nhttps://jsonplaceholder.typicode.com/users", verify=False)

user_dict = ["Leanne Graham", "Clementina DuBuque", "Glenna Reichert", "Kurtis Weissnat"]

user_list = [(name, count) for name, count in username_dict.items()]
print(user_list)

json_data = r.json()

json_response = json.loads(r.text)

#user_list =

print (r.text)

curr_date = (time.time())

#connnect to database
con = sqlite3.connect(MY_PATH)
con.execute('CREATE TABLE IF NOT EXISTS ')

sys.exit(0)
#con.execute('CREATE TABLE IF NOT EXISTS new_table' )
#con.execute('CREATE TABLE new_table')
