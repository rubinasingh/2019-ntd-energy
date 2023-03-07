import streamlit as st
import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model = st.container()

# Customize
st.markdown(
    """
    <style>
     .main {
     background-color: #F5F5DC;

     }

    </style>
    """,
    unsafe_allow_html=True
)

# Code we want to only run once
@st.cache_data
def get_data(filename):
    ntd_data = pd.read_excel(filename, sheet_name = 'Agency Totals')
    return ntd_data

with header:
    st.title('Welcome to CET 522 Final Project')
    st.text('In this project, we aim to identify the current state of fleet electrification in the United States')
    st.text('TEST')

with dataset:
    st.header('National Transit Database')
    ntd_data = get_data('Data/Fuel and Energy.xlsm')
    st.write(ntd_data.head())

    st.subheader('State Distribution on the NTD Dataset')
    state_dist = pd.DataFrame(ntd_data['State'].value_counts())
    st.bar_chart(state_dist)


with features:
    st.header('Features I Created')
    st.markdown('* **first feature:**')
    st.markdown('* **second feature:**')

with model:
    st.header('Model')
    sel_col, disp_col = st.columns(2)

    max_depth = sel_col.slider('What do you want to do?', min_value = 10, max_value = 100, value = 20, step = 10)
    n_estimators = sel_col.selectbox('How many estimators shoudl there be?', options = [100, 200, 300], index = 0)
    input_feature = sel_col.text_input('Which feature shoudl be used?', 'State')
    
    # Random Forest Model
    # regr = RandomForestRegressor(max_depth = max_depth, n_estimators = number_of_trees)
    # x = ntd_data[[input_feature]]
    # y = ntd_data[['trip_distance']]

    # regr.fit(x, y)
    # prediction = regr.predict(y)

    disp_col.subheader('Mean Absolute Error: ')
    # disp_col.write(mean_absolute_error(y, prediction))
    disp_col.subheader('Mean Squared Error: ')
    # disp_col.write(mean_squared_error(y, prediction))
    disp_col.subheader('R Squared Error: ')
    # disp_col.write(r2_score(y, prediction))

