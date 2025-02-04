import streamlit as st
import pandas as pd

file_path = r'C:\Users\frede\Galaxy_dev\test_data\outputs\directed_lines_stops.csv'
df = pd.read_csv(file_path, sep=';')

st.map(data=df, latitude='stop_latitude', longitude='stop_longitude', size=1000)


