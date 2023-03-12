import streamlit as st
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import openpyxl

st.set_page_config(
    page_title = "Welcome to U.S. Transit Fleets Energy Status"
    #page_icon = "⚡️"
)

st.title("Welcome to our CET 522 Project")
st.sidebar.success("Select a page above.")


# Code we want to only run once
# @st.cache_data
@st.experimental_memo  # replacement for @st.cache_data
def get_data(filename):
    ntd_data = pd.read_excel(filename, sheet_name = 'Agency Totals')
    return ntd_data

# @st.cache_data
@st.experimental_memo  # replacement for @st.cache_data
def get_city_data(filename):
    city_data = pd.read_excel(filename)
    return city_data


# population density map
# fuel types by city
# political leanings of each state
# scatter plot of population density vs # of transportation agencies
# heat map ?

