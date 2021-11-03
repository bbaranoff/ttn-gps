#!/usr/bin/env python3
"""
    Test harness for dragino module - sends hello world out over LoRaWAN 5 times
"""
import logging
from datetime import datetime
from time import sleep
import RPi.GPIO as GPIO
from dragino import Dragino
import subprocess


GPIO.setwarnings(False)

# add logfile
logLevel=logging.DEBUG
logging.basicConfig(filename="test.log", format='%(asctime)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s', level=logLevel)


D = Dragino("dragino.ini", logging_level=logLevel)
D.join()
while not D.registered():
    print("Waiting for JOIN ACCEPT")
    sleep(2)
#sleep(10)
getVersion =  subprocess.Popen("/home/pi/coordinates", shell=True, stdout=subprocess.PIPE).stdout
version =  getVersion.read()
for i in range(0, 2):
    D.send(version.decode())
    start = datetime.utcnow()
    while D.transmitting:
        pass
    end = datetime.utcnow()
    print("Sent Hello World message ({})".format(end-start))
    sleep(1)
