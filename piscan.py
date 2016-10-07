#!/usr/bin/python3

#### Libraries ####
from datetime import datetime
import time, os, pygame
from pygame.locals import *
import picamera
import http.client

### Settings ###
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True
camera.resolution = (1024, 768)

#### Functions ####

def connected():
    conn = http.client.HTTPConnection("www.google.de")
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def make_foto():
    camera.capture('doc_pic.jpg')
    camera.close()


#### MAIN PROGRAM ####


try:
    if connected():
        make_foto()
    else:
        print("not connected")


finally:
    os.system('clear')
#    sense.clear()
#    pygame.display.quit()
