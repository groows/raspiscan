#!/usr/bin/python3

#### Libraries ####
from datetime import datetime
import time, os, pygame
from pygame.locals import *
import picamera
import http.client

#### Functions ####

def connected():
    conn = http.client.HTTPConnection("www.google.de")
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def make_foto():

    camera = picamera.PiCamera()
    camera.hflip = True
    camera.vflip = True
    camera.resolution = (1024, 768)
    
    camera.start_preview(alpha=200)
    camera.capture('~/Desktop/Pictures/script_shot.jpg')
    camera.stop_preview()
    camera.close()

#### MAIN PROGRAM ####


try:
    if 1 == 1:
        make_foto()
    else:
        print("not connected")


finally:
    os.system('clear')
#    sense.clear()
#    pygame.display.quit()
