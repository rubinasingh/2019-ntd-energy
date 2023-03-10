import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

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

# Make a scatterplot of population density of a city vs. number of transit agencies

#st.write('Scatterplot of', 'Population Density', 'and', 'Number of Transit Agencies')
# x = merged_data['Population Density']



#fig, ax = plt.subplots()
# create a list of fuel_type_no_zero where the values of ntd_data[fuel_type] are not zero
#fuel_type_no_zero = [x for x in ntd_data[fuel_type].values if x!= 0]  
# if ntd_data[fuel_type].values == 0: remove it from the list of fuel_type_no_zero
# ntd_data[fuel_type].values = [x for x in ntd_data[fuel_type].values if x != 0
# exclude zero from ntd_data[fuel_type].values 
#fuel_type_no_zero = ntd_data[fuel_type].replace(0, np.nan)
#ax.hist(ntd_data[fuel_type_no_zero].values)
# ax.set_xlabel(fuel_type)
#st.pyplot()
# fig, ax = plt.subplots()
# ax.hist(fuel_data, bins = 5)
# ax.set_xlabel(fuel_type)
# ax.set_ylabel('Distribution')

#st.pyplot(fig)


#st.write(merged_data.plot.hist(x = fuel_type))

# Make a scatterplot based on user input of two variables
# variable1 = st.selectbox('Select a variable', merged_data.columns)
# variable2 = st.selectbox('Select a variable', merged_data.columns)
# st.write('Scatterplot of', variable1, 'and', variable2)
# st.write(merged_data.plot.scatter(x = variable1, y = variable2))

# Boxplot


