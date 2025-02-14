import os
import streamlit as st

import pandas as pd

import constants as co
from data import parcel as p


class Parcels:
    parcel_dict = {}

    @classmethod
    def load_data(cls, file_path):
        df = pd.read_csv(file_path, sep=';')
        for _, row in df.iterrows():
            Parcels.parcel_dict[row['parcel_id']] = p.Parcel(row['parcel_id'], row['delivery_latitude'],
                                                             row['delivery_longitude'], row['client_id'])

    @staticmethod
    def get_parcels():
        if 'parcels' not in st.session_state:
            all_parcels = Parcels()
            all_parcels.load_data(os.path.join(co.ROOT_PATH, 'parcels.csv'))
            st.session_state.parcels = all_parcels
        return st.session_state.parcels
