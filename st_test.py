import streamlit as st
import pandas as pd

source_target_path = r'C:\Users\frede\Galaxy\test_data_creator\csv\output\delivery_address_preprocessed.csv'
source_target_df = pd.read_csv(source_target_path, sep=';')

if st.checkbox('show map'):
  st.map(source_target_df[['latitude','longitude']])