import streamlit as st
import pandas as pd

def get_data(filename):
    ntd_data = pd.read_excel(filename, sheet_name = 'Agency Totals')
    return ntd_data

# @st.cache_data
@st.experimental_memo  # replacement for @st.cache_data
def get_city_data(filename):
    city_data = pd.read_excel(filename)
    return city_data

ntd_data = get_data('Data/Fuel and Energy.xlsm')
city_data = get_city_data('Data/uscities.xlsx')
city_data = city_data.rename(columns = {'city': 'City', 'lat': 'latitude', 'lng': 'longitude'})
merged_data = pd.merge(ntd_data, city_data, on="City")

merged_data['Diesel'] = merged_data['Diesel'] * 1.155
merged_data['Bio-Diesel'] = merged_data['Bio-Diesel'] * 0.09 # assuming B20 fuel is used
merged_data['Electric Propulsion'] = merged_data['Electric Propulsion'] * 0.031
merged_data['Electric Battery'] = merged_data['Electric Battery'] * 0.031

st.header('Maps 📍')
st.header('Cities included in the National Transit Datset')
st.map(merged_data)

# Map where only the cities with electric propulsion or electric battery > other fuel types are shown:
# Map where only the cities with electric propulsion or electric battery > other fuel types are shown:
st.header('Electric Cities ⚡️')
st.subheader('Cities where fleet fuel source is primarily electric')

# create boolean column for each row:
merged_data['Electric > Others'] = (merged_data['Electric Propulsion'] > merged_data[['Diesel', 'Gasoline', 'Compressed Natural Gas', 'Bio-Diesel']].sum(axis=1)) | (merged_data['Electric Battery'] > merged_data[['Diesel', 'Gasoline', 'Compressed Natural Gas', 'Bio-Diesel']].sum(axis=1))

# Filter the DataFrame to only include rows where 'Electric > Others' is True
filtered_data = data.loc[data['Electric > Others'] == True]

# Use st.map() to map the filtered DataFrame
st.map(filtered_data)
