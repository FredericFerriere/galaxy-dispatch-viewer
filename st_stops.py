import streamlit as st
import pandas as pd

directed_lines = r'C:\Users\frede\Galaxy_dev\test_data\outputs\directed_lines_stops.csv'
stops_df = pd.read_csv(directed_lines, sep=';')

st.map(data=stops_df, latitude='stop_latitude', longitude='stop_longitude', size=1000)


