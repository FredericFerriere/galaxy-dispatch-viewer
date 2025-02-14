import streamlit as st
import pandas as pd

parcels_path = r'C:\Users\frede\Galaxy_dev\test_data\inputs\parcels_preprocessed.csv'
parcels = pd.read_csv(parcels_path, sep=';')

st.map(data=parcels, latitude='latitude', longitude='longitude', size=10)


