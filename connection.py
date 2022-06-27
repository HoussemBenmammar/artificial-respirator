import json
import requests
from numpy import random 

def api(mode) :
  requette='http://192.168.125.150:8000/'+mode
  response = requests.get(requette)
  values=[]
  i=0
  if 200 <= response.status_code < 300:  
      mode1=response.json()
      for key in mode1 :
            if i!=len(mode1)-1 :
              if mode1[key]=="/" :
                mode1[key]=0
              if key=="i" :
                mode1[key]=random.randint(1,3)
              a=float(mode1[key])
              values.append(a)
            i=i+1
  else:
    for j in range(9) :
     values.append(0) 
  return(values)  


def api_error() :
    i=0  
    response = requests.get('http://192.168.125.150:8000/error')
    if 200 <= response.status_code < 300:  
      i=1
    else:
      i=2 

def api_gas() :
  response = requests.get('http://192.168.125.150:8000/Gas')
  values=[]
  i=0
  if 200 <= response.status_code < 300:  
      gas=response.json()
      for key in gas :
              values.append(gas[key])
  else:
    for j in range(3) :
     values.append(0) 
  return(values)  
             
def api_vent() :
  response = requests.get('http://192.168.125.150:8000/Vent')
  values=[]
  i=0
  if 200 <= response.status_code < 300:  
      vent=response.json()
      for key in vent :
              values.append(vent[key])
  else:
    for j in range(8) :
     values.append(0) 
  return(values)