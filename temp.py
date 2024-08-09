# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import pandas as pd
datos = pd.read_csv('ATP3.csv', encoding='ISO-8859-1')
print(datos.info())
print(datos.head())
print(datos.iloc[0:5])
#REGLONES SALTEADOS
print(datos.iloc[[0,3,8,200],])
#COLUMNAS
print(datos.iloc[:,0:2])
print(datos.iloc[[0,3,6,24],[0,5,6]])
#RANGOS DE REGLONES Y COLUMNAS
print(datos.iloc[0:5,5:8])