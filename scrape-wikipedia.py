# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:54:57 2018

@author: kaoyuant
"""



import wikipedia
import requests
from bs4 import BeautifulSoup
import time
import numpy as np


req = requests.get('https://en.wikipedia.org/wiki/Results_of_the_Malaysian_general_election,_2018_by_parliamentary_constituency')

soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find_all(lambda tag: tag.name=='table') 
rows = table[2].findAll(lambda tag: tag.name=='tr')
out=[]
for i in range(len(rows)): 
    td=rows[i].find_all('td')
    out=out+[x.text for x in td]