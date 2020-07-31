# Chapter 3.1: Estimated Infections vs Confirmed Cases

import pandas as pd
import requests
import plotly.express as px
from urllib.request import urlopen
import json
import datetime
from datetime import timedelta
from functions import clean_county_deaths, clean_county_cases

response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
response2 = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

if response.status_code != 200 or response2.status_code != 200:
    print('ERROR')
# Checking that the download was successful

deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/'+
            'master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv', dtype = {'FIPS': 'string'})
# reading the csv file from github that contains the deaths by county from 1/22/20 - the current day

deaths_df = clean_county_deaths(deaths_df)
confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv', dtype = {'FIPS': 'string'})
# reading the csv file from github that contains the cases by county from 1/22/20 - the current day

confirmed_df = clean_county_cases(confirmed_df)
confirmed_df['cases/pop'] = confirmed_df.iloc[:,-18] / confirmed_df['Population']
deaths_df['Infection_Estimates'] = (deaths_df.iloc[:,-1] * 100) / deaths_df['Population'] 

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig = px.choropleth(deaths_df, geojson=counties, scope="usa", locations='FIPS', color= 'Infection_Estimates',
                        color_continuous_scale = 'Viridis',
                        range_color=(0, 0.05))
fig.update_layout(title_text = 'Estimated percent of population infected by County')
fig.show()

This map of the US counties displays the estimated infection rate in the US if a death rate of 1% is applied to the reported death count. Due to the average 18 day delay between infection and death, this graph displays case estimates 18 days prior to the current date. Each county's estimated case count has been standardized by its population, based on 2019 Census data. The scale reflects the percent of the population infected by COVID 19. 

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig = px.choropleth(confirmed_df, geojson=counties, scope="usa", locations='FIPS', color= 'cases/pop',
                        color_continuous_scale='Viridis',
                        range_color=(0, 0.05))
fig.update_layout(title_text = 'Percent of population with confirmed cases by County')
fig.show()

This map displays the number of reported cases by county, standardized by population. This is also a representation of case counts 18 days ago to match Figure 1. County populations based on Census data were again used to standardize the confirmed case count. The scale reflects the percent of the population infected by COVID 19. 

