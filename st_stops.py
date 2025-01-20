import streamlit as st
import pandas as pd

file_path = r'C:\Users\frede\Galaxy_dev\test_data\outputs\clients.csv'
df = pd.read_csv(file_path, sep=';')

st.map(data=df, latitude='latitude', longitude='longitude', size=2000)


