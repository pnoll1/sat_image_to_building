#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 01:30:10 2017

@author: pat
"""
import cv2

def sat_image_to_building():
    '''
    takes inputs from josm, runs edge detection and 
    outputs ways back to josm
    '''
#grab sat view from provider (likely bing maps)

# Reads image from specified path
img = cv2.imread(file)
# cv2.imshow()
# run canny edge detection algorithm
edges = cv2.canny(img,min_val,max_val)  # image, min, max. aperture, bool edge grad.
# post process edges to remove extras
# convert to correct format for osm
# send back to josm