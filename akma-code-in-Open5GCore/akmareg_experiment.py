import requests
import subprocess
from json import dumps
from time import sleep
import random
import time


st = time.time()

for x in range(250):
    
    jsonRequest = {
        "suppFeat" : "132",
        "afId" : "23",
        "aKId" : "3234"
    }
    
        
    cmd = subprocess.Popen(['curl', '-i', '--http2-prior-knowledge', '-X', 'POST', '-d', dumps(jsonRequest), "http://192.168.11.80:8080/3gpp-akma/v1/retrieve", '-H',  "accept: application/json"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            
    jsonRequestReg = {
    "jsonrpc" : "2.0", 
    "method" : "ue5g.register", 
    "params": {
        "access_type" : 1,
        "no_pdu" : True
        }, 
    "id": 1
    }
    
    cmd2 = subprocess.Popen(['curl', '-v', 'POST', '-H', 'Content-Type: application/json-rpc', '-d', dumps(jsonRequestReg), "http://192.168.254.55:10010/jsonrpc"], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
    
   
   
print("\n\n")
        
et = time.time()
elapsed_time = et - st
print('Execution time: ', elapsed_time, ' seconds')
    
    