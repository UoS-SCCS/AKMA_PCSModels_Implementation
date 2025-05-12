import requests
import subprocess
from json import dumps
from time import sleep
import random
import time


st = time.time()
countReg = 0

for x in range(1):
    
    jsonRequest = {
        "suppFeat" : "132",
        "afId" : "23",
        "aKId" : "3234"
    }
    
        
    cmd = subprocess.Popen(['curl', '-i', '--http2-prior-knowledge', '-X', 'POST', '-d', dumps(jsonRequest), "http://192.168.11.80:8080/3gpp-akma/v1/retrieve", '-H',  "accept: application/json"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
print("\n\n")
print(countReg)
et = time.time()
elapsed_time = et - st
print('Execution time: ', elapsed_time, ' seconds')
    