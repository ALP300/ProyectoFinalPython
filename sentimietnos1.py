# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 19:54:05 2024

@author: aitor
"""

import pandas as pd
from textblob import TextBlob
import seaborn as sns
df= pd.read_csv('nyt.csv')
df['polaridad']=df['content'].apply(lambda x: TextBlob(x).sentiment.polarity)
print(df['polaridad'].head(5))