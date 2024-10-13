# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.info())
print(datos.head())
print(datos.iloc[0:10])
#REGLONES SALTEADOS
print(datos.iloc[[0,3,6,24,50,45],])
#COLUMNAS
print(datos.iloc[:,0:2])
print(datos.iloc[[0,3,6,24],[0,5,6]])
#Rangos de reglones y columnas
print(datos.iloc[0:5,5:8])