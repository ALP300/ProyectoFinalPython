# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
datos= pd.read_csv('ATP.csv')
print(datos.head())
datos.set_index("Location",inplace= True)
print("-----------------------Melbourne--------------------------")
print(datos.loc['Melbourne'])
print("-------------------Atlanta y Surface----------------------")
print(datos.loc['Atlanta','Surface'])
print("-------------SELECCIÓN AMPLIA----------------------")
print(datos.loc[['Atlanta','Melbourne'],['Series','Court']])
print("------------------SELECCIÓN CON RANGO-----------------")
print(datos.loc[['Atlanta','Melbourne'], 'Series':'Round'])
print("---------------------SELECCIÓN SOLO DE GRAND SLAM---------------")
print(datos.loc[datos['Series'].str.endswith("Slam")])


