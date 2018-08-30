# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:54:57 2018

@author: kaoyuant
"""



#import wikipedia
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd

req = requests.get('https://en.wikipedia.org/wiki/Results_of_the_Malaysian_general_election,_2018_by_parliamentary_constituency')

soup = BeautifulSoup(req.text, 'html.parser')
table = soup.find_all(lambda tag: tag.name=='table') 
out=[]
result=pd.DataFrame()
for j in range(2,18):
    rows = table[j].findAll(lambda tag: tag.name=='tr')
    td=rows[2].find_all('td')
    if len(td)==9:
        my=pd.DataFrame(out).transpose()
        result=result.append(my)
        out=[x.text for x in td]

    if len(td)==2:
            out=out+[x.text for x in td]
    #my=pd.DataFrame(out).transpose()
    #result=result.append(my)
    for i in range(3,len(rows)): 
        td=rows[i].find_all('td')
        if len(td)==9:
            my=pd.DataFrame(out).transpose()
            result=result.append(my)
            out=[x.text for x in td]

        if len(td)==2:
            out=out+[x.text for x in td]
    
my=pd.DataFrame(out).transpose()
result=result.append(my)

result=result.rename(columns={0:'No',1:'Constituency',2:'Winner',3:'Votes',4:'Majority',5:'Opponent 1',
                              6:'Votes Opponent 1',7:'Incumbent',8:'Incumbent Majority',9:'Opponent 2',
                              10:'Votes Opponent 2',11:'Opponent 3',12:'Votes Opponent 3', 13:'Opponent 4',
                              14:'Votes Opponent 4',15:'Opponent 5',16:'Votes Opponent 5'})

result.to_csv(r"C:\Users\david\github\Malaysian-Elections-GE14-2018\data\results2018.csv")