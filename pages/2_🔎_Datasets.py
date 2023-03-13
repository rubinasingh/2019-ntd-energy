import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('Dataset 🔎')

st.image('Data/CET 522 Project ER Diagram.png', caption='E/R Diagram for NTD data table and U.S. Cities data table.'
                                                        ' Attributes are simplified for readability purposes.')

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

# join tables
st.header('National Transit Database + City Data')
st.write('City data provided by [simplemaps](https://simplemaps.com/data/us-cities)')
merged_data = pd.merge(ntd_data, city_data, on="City")

st.write(merged_data.head())



