import os
import streamlit as st

import pandas as pd

import data.clients as cs
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
            cs.Clients.get_client(row['client_id']).add_parcel(row['parcel_id'])

    @staticmethod
    def get_parcels():
        if 'parcels' not in st.session_state:
            all_parcels = Parcels()
            all_parcels.load_data(os.path.join(co.ROOT_PATH, 'parcels.csv'))
            st.session_state.parcels = all_parcels
        return st.session_state.parcels

    @staticmethod
    def get_parcel(parcel_id):
        return Parcels.get_parcels().parcel_dict[parcel_id]

    @staticmethod
    def parcel_ids():
        all_parcels = Parcels.get_parcels()
        return list(all_parcels.parcel_dict.keys())
