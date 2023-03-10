import streamlit as st
import pandas as pd
import openpyxl

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
merged_data = pd.merge(ntd_data, city_data, on="City")


st.header('Maps 📍')
st.header('Cities included in the National Transit Datset')
st.map(merged_data)

# Map where only the cities with electric propulsion or electric battery > other fuel types are shown:
# Map where only the cities with electric propulsion or electric battery > other fuel types are shown:
st.header('Electric Cities ⚡️')
st.subheader('Cities where fleet fuel source is primarily electric')
electric_mask = (merged_data['Electric Propulsion'] > 
                 merged_data['Diesel'] + 
                 merged_data['Gasoline'] + 
                 merged_data.iloc[:, 13] +
                   merged_data['Compressed Natural Gas'] + 
                   merged_data['Bio-Diesel']) | (
    merged_data['Electric Battery'] > 
        merged_data['Diesel'] + merged_data['Gasoline'] + 
        merged_data.iloc[:, 13] + 
         merged_data['Compressed Natural Gas'] +
        merged_data['Bio-Diesel'])
st.map(merged_data[electric_mask])