import time
import subprocess
#import pyautogui
#import shlex
#import requests
import json

#pyautogui.typewrite("ngrok http 3000")
#import os

#print(time.localtime(time.time())[5])
#https://stackoverflow.com/questions/18406165/creating-a-timer-in-python
from subprocess import Popen, PIPE

# Set up the echo command and direct the output to a pipe
#host = input("Enter a host to ping: ")

#proc = Popen(['ngrok','http','4000'], stdout=PIPE)
#proc = Popen(['ping', '-c 2', host], stdout=PIPE)
#output = proc.stdout.readline()
#time.sleep(2)

#print (proc.communicate()[0])
# print(proc.stdout.readline())
#print(output.strip())
#proc.terminate()
#time.sleep(20)
#proc = subprocess.Popen(['ngrok http 3000'], shell=True)
#time.sleep(10)

proc = Popen(['ngrok','http','4000'], stdout=PIPE)
time.sleep(20)
proc.terminate()



localhost_url = "http://localhost:4040/status" #Url with tunnel details
#tunnel_url = requests.get(localhost_url).text #Get the tunnel information
#j = json.loads(tunnel_url)

#print(j)

#run_command('ping -c 2  www.google.com')
#run_command('ngrok http 3000')

print('Woke up mofo')


'''



def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print (output.strip())
    rc = process.poll()
    return rc
'''