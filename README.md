# sat_image_to_building

Goal: Take portion of sat image where user indicates building and return way that contains building

The end result will be be quicker mapping of buildings and increased detail.

# Implementation
Similar to Scanaerial, call python script from inside JOSM, process image and return a way in JOSM that is tagged as a building.

- Connection to JOSM: ext_tools
- image processing: currently investigating
- satellite images: Bing  Possibly ESRI, Mapbox and Digital Globe at later date

# Installation
## Requirements
- JOSM
- ext_tools JOSM plug in
- python opencv
- python requests

## Setup
- Install JOSM
- Install ext_tools plug in using JOSM
- Install required python libraries
- Download sat_image_to_building script and place it in ext_tools directory
 - /home/user/.local/share/JOSM/plugins/ext_tools/scanaerial-master/sat_image_to_building.py on Debian
- Add new tool to ext_tools in JOSM 
 - name: sat_image_to_building
 - CmdLine: path/sat_image_to_building {lat} {long} {TZoom}

## Usage
- Call from menu using tools > sat_image_to_building or set up hotkey(s) in JOSM Preferences

# License
To be decided later
