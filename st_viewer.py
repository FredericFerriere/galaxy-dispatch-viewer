import os

import streamlit as st

st.set_page_config(layout='wide')

from data import clients as cs, parcels as ps
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
    "Maps": [st.Page('views/st_client_parcels.py', title='View Delivery Data'),
             st.Page('views/st_van_model.py', title='View Van Model Data'),
             st.Page('views/st_bike_model.py', title='View Bike Model Data'),
             st.Page('views/st_bike_bus_zoned_model.py', title='View Bike + Bus Zoned Model Data'),
             st.Page('views/st_bike_bus_line_model.py', title='View Bike + Bus Line Model Data'),
             st.Page('views/st_bike_bus_hub_model.py', title='View Bike + Bus Hub Model Data'),
             st.Page('views/st_bike_bus_zoned_line_model.py', title='View Bike + Bus Zoned Line Model Data'),
             st.Page('views/st_van_bike_bus_ulw_model.py', title='View Van + Bike + Bus ULW Model Data'),
             st.Page('views/st_model_comparison.py', title='Model Comparison')]
})

pg.run()