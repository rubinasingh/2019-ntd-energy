import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Dataset 🔎')

def get_data(filename):
    ntd_data = pd.read_excel(filename, sheet_name = 'Agency Totals')
    return ntd_data

@st.cache_data
def get_city_data(filename):
    city_data = pd.read_excel(filename)
    return city_data

ntd_data = get_data('Data/Fuel and Energy.xlsm')
city_data = get_city_data('Data/uscities.xlsx')
city_data = city_data.rename(columns = {'city': 'City', 'lat': 'latitude', 'lng': 'longitude'})

# join tables
st.header('National Transit Database + City Data')
st.write('City data provided by [simplemaps](https://simplemaps.com/data/us-cities)')
merged_data = pd.merge(ntd_data, city_data, on="City")

st.write(merged_data.head())

st.header('Descriptive Statistics')
# Raw data statistics, histograms, scatterplots, heatmaps, box plots

# things we want to show
# population density of a city vs number of transit agencies




# Raw data statistics - count, mean, sandard deviation, min, max, quartiles
# Number of observations over time
# Histogram
# Make a histogram of the fuel type of the users choice (column options = 'Diesel', 'Gasoline', 'Hydrogen', 'Compressed Natural Gas', 'Bio-Diesel', 'Electric Propulsion', 'Electric Battery', 'Other Fuel Type')
fuel_type = st.selectbox('Select a fuel type', options = ['Gasoline', 'Liquefied Petroluem Gas', 'Compressed Natural Gas', 'Bio-Diesel', 'Electric Propulsion', 'Electric Battery'])
# st.write('Scatterplot of', fuel_type)
