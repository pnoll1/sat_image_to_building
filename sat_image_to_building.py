#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 01:30:10 2017

@author: pat
"""
import cv2
from sys import argv
import requests

def sat_image_to_building():
    '''
    takes inputs from josm, runs edge detection and 
    outputs ways back to josm
    '''
# grab inputs from josm
lat = argv[1]
long = argv[2]
zoom = argv[3]

# grab sat view from provider (likely bing maps)
bing_api_key = ""

# construct request
# https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/lat, long/zoom?mapSize=500,500&key=bing_api_key
img =  requests.get()
# Reads image from specified path
img = cv2.imread(file,0) # 0 arg imports image as gray scale as needed for canny function
# cv2.imshow()
# run canny edge detection algorithm
edges = cv2.canny(img,min_val,max_val)  # image, min, max. aperture, bool edge grad.
# post process edges to remove extras
# filter out areas too small
# filter incomplete ways
# filter shadows
# orthagonalize
# convert to correct format for osm
# send back to josm