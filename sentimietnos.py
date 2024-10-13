# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:30:04 2024

@author: aitor
"""
promedio= lambda x,y: (x+y)/2
print("Promedio: ", promedio(10,0))

def prom(x,y):
    return (x+y)/2

print(prom(10,0))

import pandas as pd
url = 'https://raw.githubusercontent.com/LilianaC/Pandas/master/EstadosDF%20-%20Sheet1.csv'
df= pd.read_csv(url)
df['TemperaturaK']=df['Temperatura'].apply(lambda x: x+273.15)
print(df['Temperatura'])
print(df['TemperaturaK'])
df['Max']= df['Temperatura'].apply(lambda x:x>30)
print(df['Max'])

import math
df['Temperatura4']= df['TemperaturaK'].apply(lambda x: math.pow(x,2))
print(df['Temperatura4'])