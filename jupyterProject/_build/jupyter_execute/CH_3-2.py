# Results: LA Counties Estimated Infections and Rate of Detection

import pandas as pd
import plotly.express as px
%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

try:
    df = pd.read_csv('https://lacdph.shinyapps.io/covid19_surveillance_dashboard/_w_355748cc/session/7b519430b33e061672e690e7aa06a2c1/download/download3?w=355748cc')
    df.to_csv('LA_Backup.csv', index = False)
except:
    df = pd.read_csv('LA_Backup.csv', index_col = False )
    print("Using LA backup file.")

index_val = len(df.index) 
df = df.sort_index(ascending=False, axis=0)
df = df.reset_index()

for ind in df.index:
    if (int(ind)+18) > index_val-1:
        df.loc[ind, 'total_infections'] = 0
    else:
        df.loc[ind, 'total_infections'] = df.loc[ind+18, 'total_deaths'] * 100

df = df[0:-18]

fig, ax = plt.subplots()
ax.plot(df['date_use'], df['total_infections'], label='Estimated Infections')
ax.plot(df['date_use'], df['total_cases'], label='Confirmed cases')
ax.set_xlabel('days')
ax.set_ylabel('total infections at 1%')
plt.xticks(np.arange(0, 110, step=21)) 
ax.legend()
plt.show()

df = df[15:-1]
df['detection_rate'] = df['total_cases'] / df['total_infections']

df.hist(column='detection_rate', bins=10)
plt.show()

