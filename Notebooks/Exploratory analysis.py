import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r"C:\The-Price-Of-Everything\Data\Raw")

# Load and clean CPI
df_cpi = pd.read_csv("CPIAUCSL.csv")
df_cpi['observation_date'] = pd.to_datetime(df_cpi['observation_date'])
df_cpi = df_cpi.dropna()

# Load and clean Wages
df_wages = pd.read_csv("AHE.csv")
df_wages['observation_date'] = pd.to_datetime(df_wages['observation_date'])
df_wages = df_wages.dropna()

# Plot both on same graph
fig, ax1 = plt.subplots(figsize=(12, 6))

# CPI on left axis
ax1.plot(df_cpi['observation_date'], 
         df_cpi['CPIAUCSL'], 
         color='blue', label='CPI')
ax1.set_ylabel('CPI', color='blue')

# Wages on right axis
ax2 = ax1.twinx()
ax2.plot(df_wages['observation_date'], 
         df_wages['CES0500000003'], 
         color='red', label='Wages')
ax2.set_ylabel('Wages', color='red')

plt.title('CPI vs Wages Over Time')
fig.legend(loc='upper left')
plt.show()
