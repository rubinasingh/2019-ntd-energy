
ntd_data = get_data('Data/Fuel and Energy.xlsm')
city_data = get_city_data('Data/uscities.xlsx')
city_data = city_data.rename(columns = {'city': 'City', 'lat': 'latitude', 'lng': 'longitude'})

# join tables
st.header('National Transit Database + City Data 🔎')
st.write('City data provided by [simplemaps](https://simplemaps.com/data/us-cities)')
merged_data = pd.merge(ntd_data, city_data, on="City")
st.write(merged_data.head())