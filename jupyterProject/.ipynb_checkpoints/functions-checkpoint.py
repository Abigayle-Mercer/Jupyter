import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def zero_fill(x):
    x = x[:-2]
    if len(x) < 5:
        return '0' + x
    return x

def logarithmic():
    x = np.linspace(0, 10, 100, endpoint = True)
    y = (np.log(x) + 2) * 10000
    plt.plot(x, y, '-r', label=r'y = log(x)')
    axes = plt.gca()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Logarithmic Curve')
    plt.legend(loc='upper left')
    plt.show()

    
def exponential():
    x = np.linspace(0, 10, 100, endpoint = True)
    y = (np.exp(x))
    plt.plot(x, y, '-r', label=r'y = x^2')
    axes = plt.gca()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exponential Curve')
    plt.legend(loc='upper left')
    plt.show()
    
    
def first(df, index):
    def logistic(x, midpoint=0, rate=.8, maximum=1):
        return maximum / (1 + np.exp(-rate * (x - midpoint)))

    x = np.linspace(-6, 10, 1000)
    y = logistic(x)# + logistic(x, midpoint=6, rate=2, maximum=5)

    def double_log(x, x1, r1, m1, x2, r2, m2):
        return logistic(x, x1, r1, m1) + logistic(x, x2, r2, m2)
    
    popt1, _ = curve_fit(logistic, range(0, index),  df['total_infections'], p0=[0,0,0], maxfev = 5000)

    popt2, _ = curve_fit(double_log, range(0, index), df['total_infections'], p0=[0,0,0,0,0,0])

    xmodel = np.linspace(0, index, index)
    ymodel1 = logistic(xmodel, *popt1)

    ymodel2 = double_log(xmodel, *popt2)

    return np.gradient(ymodel2)

def second(df, index):
    def logistic(x, midpoint=0, rate=.8, maximum=1):
        return maximum / (1 + np.exp(-rate * (x - midpoint)))

    x = np.linspace(-6, 10, 1000)
    y = logistic(x)# + logistic(x, midpoint=6, rate=2, maximum=5)

    def double_log(x, x1, r1, m1, x2, r2, m2):
        return logistic(x, x1, r1, m1) + logistic(x, x2, r2, m2)

    popt1, _ = curve_fit(logistic, range(0, index),  df['total_infections'], p0=[0,0,0], maxfev = 5000)

    popt2, _ = curve_fit(double_log, range(0, index), df['total_infections'], p0=[0,0,0,0,0,0])

    xmodel = np.linspace(0, index, index)
    ymodel1 = logistic(xmodel, *popt1)

    ymodel2 = double_log(xmodel, *popt2)

    first = np.gradient(ymodel2)
    return np.gradient(first)

    
def plot_first_derivitive(df, one, popsize):
    plt.figure(figsize=(12,8))
    plt.plot(df['index'], one / popsize, color='blue', label='death rate cases')
    plt.xlabel('days')
    plt.ylim(-0.002, 0.002)
    plt.ylabel('Infection Rate (number of infections per day)')
    plt.title('Number of estimated new cases per day')
    plt.xticks(np.arange(0, 166, step=22)) 

    
def plot_second_derivitive(df, two,  popsize):
    plt.figure(figsize=(12,8))
    plt.plot(df['index'], two / popsize, color='black', label='death rate cases')
    plt.xticks(np.arange(0, 166, step=22)) 
    plt.xlabel('days')
    plt.ylabel('Change in Infection Rate')
    plt.title('Is the virus spreading faster or slower?')
    plt.ylim(-0.00015, 0.00015)
    plt.axhspan(-0.001, 0, facecolor='b', alpha=0.5)
    plt.axhspan(0, 0.001, facecolor = 'r', alpha = 0.3)



 
    
def clean_cases(cases_df):
    cases_df = cases_df[cases_df['iso3'] == 'USA'] 
    cases_df = cases_df.reset_index()
    cases_df = cases_df.drop('index', axis=1)
    cases_df = cases_df.fillna('0') 
    cases_df = cases_df.fillna('0') 
    cases_df.to_csv('US_Confirmed.csv', index=False)
    cases_df = cases_df.drop(['UID', 'iso2', 'iso3', 'code3', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'FIPS', 'Admin2', 'Province_State'], axis=1)
    return cases_df

def clean_county_cases(confirmed_df):
    pop_df = pd.read_csv('census.csv', dtype = {'FIPS': 'string'} )
    confirmed_df = confirmed_df[confirmed_df['iso3'] == 'USA'] 
    confirmed_df = confirmed_df.reset_index()
    confirmed_df = confirmed_df.drop('index', axis=1)
    confirmed_df = confirmed_df.fillna('0')
    confirmed_df = confirmed_df.drop(['UID', 'Lat', 'Long_', 'iso2', 'iso3', 'code3', 'Combined_Key', 'Province_State', 'Country_Region'], axis=1)
    confirmed_df['FIPS'] = confirmed_df['FIPS'].apply(zero_fill)
    confirmed_df = pd.merge(pop_df, confirmed_df, on='FIPS')
    confirmed_df.to_csv('US_Confirmed.csv', index = False)
    return confirmed_df
    
def clean_deaths(deaths_df):
    deaths_df = deaths_df[deaths_df['iso3'] == 'USA'] 
    deaths_df = deaths_df.reset_index()
    deaths_df = deaths_df.drop('index', axis=1)
    deaths_df = deaths_df.fillna('0') 
    deaths_df.to_csv('US_Deaths.csv', index = False)
    deaths_df = deaths_df.drop(['UID', 'iso2', 'iso3', 'code3', 'Country_Region', 'Lat', 'Long_', 'Combined_Key', 'FIPS', 'Admin2', 'Province_State', 'Population'], axis=1)
    return deaths_df

def clean_county_deaths(deaths_df):
    pop_df = pd.read_csv('census.csv', dtype = {'FIPS': 'string'} )
    deaths_df = deaths_df[deaths_df['iso3'] == 'USA'] 
    deaths_df = deaths_df.reset_index()
    deaths_df = deaths_df.drop('index', axis=1)
    deaths_df = deaths_df.fillna('0') 
    deaths_df = deaths_df.drop(['UID', 'Lat', 'Long_', 'iso2', 'iso3', 'code3', 'Combined_Key',  'Province_State', 'Country_Region', 'Population'], axis=1)
    deaths_df['FIPS'] = deaths_df['FIPS'].apply(zero_fill)
    deaths_df = pd.merge(pop_df, deaths_df, on='FIPS')
    deaths_df.to_csv('US_Deaths.csv', index = False)
    return deaths_df

def calculate_infection(df, x):
    for ind in df.index:
        if (int(ind)+18) > x-1:
            df.loc[ind, 'total_infections'] = df.loc[ind-1, 'total_infections']
        else:
            df.loc[ind, 'total_infections'] = df.iloc[ind+18, 1] * 100

            
def detection_plot(deaths_df, cases_df):
    plt.figure(figsize=(12,8))
    plt.plot(deaths_df['index'], deaths_df['total_infections'], color='blue', label='death rate cases')
    plt.plot(cases_df['index'], cases_df['detection_cases'], color='red', label='detection cases')
    plt.xticks(np.arange(0, 166, step=21)) 
    plt.xlabel('days')
    plt.ylabel('total infections')
    plt.title('Case Estimates Based on a 1% death rate vs 20% detection rate')
    plt.legend()