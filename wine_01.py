import os
os.listdir()
import pandas as pd
import numpy as np

df = pd.read_csv('winequality-red.csv')
df.head(2)
df.head()
df.tail()
df.sample(5)
df.describe()
df.info()
df.shape
df.size
df.columns
df.columns.tolist()
df.head()
df.loc[1]
df.loc[1:3]
df.loc[1,'fixed acidity']
df.loc[3,'chlorides']
df.loc[4,'alcohol']
df.loc[0:1, ['chlorides', 'density']]
df.loc[2:3, ['residual sugar','pH']]




