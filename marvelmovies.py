import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="The Marvel Universe",
                   page_icon=":clapper:",
                   layout="wide"
                   )

st.header("The Marvel Universe")
marvel = pd.read_csv(marvelmovies.csv)


#----SIDE BAR----
st.sidebar.header("What Marvel movie?")
option = st.sidebar.selectbox(
    'Select a movie!',
     [marvel.Title])
