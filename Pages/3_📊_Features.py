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

st.title('Features 📊')
st.subheader('Number of Transit Agencies in Each State')
state_dist = pd.DataFrame(ntd_data['State'].value_counts())
st.bar_chart(state_dist)

st.subheader('Distribution of Agency Types')
agency_type_dist = pd.DataFrame(ntd_data['Organization Type'].value_counts())
st.bar_chart(agency_type_dist)

# Create bar chart with different fuel types
st.subheader('Fuel Breakdown across the United States')
fuel_counts = pd.Series([ntd_data['Diesel'].sum(), ntd_data['Gasoline'].sum(), ntd_data.iloc[:, 13].sum(), ntd_data['Compressed Natural Gas'].sum(), ntd_data['Bio-Diesel'].sum(), ntd_data['Electric Propulsion'].sum(), ntd_data['Electric Battery'].sum()], index = ['Diesel', 'Gasoline', 'Petroluem Gas','Natural Gas', 'Bio-Diesel', 'Electric Propulsion', 'Electric Battery']) 
st.bar_chart(fuel_counts)

st.subheader('Fuel Usage by State')
states = sorted(merged_data['State'].unique())
state = st.selectbox('Select a state', states)
state_data = merged_data[merged_data['State'] == state]

# create bar chart of fuel types based on state
fuel_count_state = pd.Series([state_data['Diesel'].sum(), state_data['Gasoline'].sum(), state_data.iloc[:, 13].sum(), state_data['Compressed Natural Gas'].sum(), state_data['Bio-Diesel'].sum(), state_data['Electric Propulsion'].sum(), state_data['Electric Battery'].sum()], index = ['Diesel', 'Gasoline', 'Petroluem Gas','Natural Gas', 'Bio-Diesel', 'Electric Propulsion', 'Electric Battery'])
st.bar_chart(fuel_count_state)




# if fuel_count_state['Electric Propulsion'] > fuel_count_state['Diesel']:
#     st.altair_chart(fuel_count_state, color = 'green')
# if fuel_count_state['Electric Propulsion'] > fuel_count_state['Diesel']:
#     st.altair_chart(fuel_count_state, color = 'green')
# else:
#     st.altair_chart(fuel_count_state, color = 'red')