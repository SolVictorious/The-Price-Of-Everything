import numpy as np
import pandas as pd
import os 
import matplotlib as mp

os.chdir(r"C:\Users\fahad\Downloads\Economic Analysis Project")
df = pd.read_csv("CPIAUCSL.csv")

df['observation_date'] = pd.to_datetime(df['observation_date'])
print(df.head())
print(df.info())


df_cleaned = df.dropna()
print(df_cleaned)
df.plot(x='observation_date', y='CPIAUCSL', title='CPI Over Time')

df_2 = pd.read_csv("AHE.csv")

df_2['observation_date'] = pd.to_datetime(df_2['observation_date'])
print(df_2.head())
print(df_2.info())

