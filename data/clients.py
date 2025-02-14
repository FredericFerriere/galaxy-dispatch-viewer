import os
import pandas as pd

import streamlit as st

import constants as co
from data import client as c


class Clients:
    client_dict = {}

    @classmethod
    def load_data(cls, file_path):
        df = pd.read_csv(file_path, sep=';')
        for _, row in df.iterrows():
            Clients.client_dict[row['client_id']] = c.Client(row['client_id'], row['client_name'],
                                                             row['latitude'], row['longitude'])

    @staticmethod
    def get_clients():
        if 'clients' not in st.session_state:
            all_clients = Clients()
            all_clients.load_data(os.path.join(co.ROOT_PATH, 'clients.csv'))
            st.session_state.clients = all_clients
        return st.session_state.clients