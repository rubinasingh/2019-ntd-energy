import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu

# header = st.container()
# dataset = st.container()
# features = st.container()
# map = st.container()
# # model = st.container()

# with st.sidebar:
#     selected = option_menu(
#         menu_title = "Navigate",
#         options = ["Home", "Dataset", "Features", "Maps", "Contact"],
#         icons = ["🏠", "🔎", "📊", "📍", "📞"]

#         # if selected == "Home"
#         #     st.write("Home")
#         # if selected == "Dataset"
#         #     st.write("Dataset")
#         # if selected == "Features"
#         #     st.write("Features")
#         # if selected == "Map"
#         #     st.write("Map")
#         # if selected == "Model"
#         #     st.write("Model")
#         # if selected == "Contact"
#         #     st.write("Contact")
#     )

# Customize
# st.markdown(
#     """
#     <style>
#      .main {
#      background-color: #F5F5DC;

#      }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Code we want to only run once
@st.cache_data
def get_data(filename):
    ntd_data = pd.read_excel(filename, sheet_name = 'Agency Totals')
    return ntd_data

@st.cache_data
def get_city_data(filename):
    city_data = pd.read_excel(filename)
    return city_data


with header:
    st.title('Welcome to CET 522 Final Project')
    text = 'In this project, we aim to identify the current state of fleet electrification in the United States based on the National Transit Database.'
    st.write(text, text_align = 'center')




# population density map
# fuel types by city
# political leanings of each state
# scatter plot of population density vs # of transportation agencies
# heat map ?

