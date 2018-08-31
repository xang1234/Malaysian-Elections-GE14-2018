# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:57:22 2018

@author: kaoyuant
"""
import json



file_directory="D:/malaysia_parliamentary_carto_2018.geojson"
json_data=open(file_directory).read()

data= json.loads(json_data)
move_long=4

for i in range(len(data['features'])):
    if int(data['features'][i]['properties']['kodpar'])>= 166: # Move Sabah, Sarawak, WP Labuan
        for k in range(len(data['features'][i]['geometry']['coordinates'])):
            for j in range(len(data['features'][i]['geometry']['coordinates'][k][0])):
                data['features'][i]['geometry']['coordinates'][k][0][j][0]=data['features'][i]['geometry']['coordinates'][k][0][j][0]- move_long
        
    
with open('D:/malaysia_parliamentary_carto_2018_move.geojson', 'w') as outfile:
    json.dump(data, outfile)

