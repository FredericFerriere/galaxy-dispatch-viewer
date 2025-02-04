import os

import streamlit as st

import clients as cs
import parcels as ps
import constants as co

if 'clients' not in st.session_state:
    all_clients = cs.Clients()
    all_clients.load_data(os.path.join(co.ROOT_PATH, 'clients.csv'))
    st.session_state.clients = all_clients

if 'parcels' not in st.session_state:
    all_parcels = ps.Parcels()
    all_parcels.load_data(os.path.join(co.ROOT_PATH, 'parcels.csv'))
    st.session_state.parcels = all_parcels

pg = st.navigation({
    "Maps": [st.Page('st_client_parcels.py', title='View Delivery Data'),
             st.Page('st_van_model.py', title='View Van Model Data'),
             st.Page('st_bike_model.py', title='View Bike Model Data'),
             st.Page('st_bus_bike_model.py', title='View Bus + Bike Model Data')]
})

pg.run()