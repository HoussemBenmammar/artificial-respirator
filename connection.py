import requests
import json
import os 

response = requests.get('https://api.github.com')
if response.status_code == 200:
    data=response.json()
    #print(data)
    #exec(open("sys-test.py").read())
    os.system('sys-test.py')
elif response.status_code == 404:
    print('Not Found.')