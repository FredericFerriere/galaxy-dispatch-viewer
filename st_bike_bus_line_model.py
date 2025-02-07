import os

import streamlit as st

import model as m
import constants as co
import pdk_layer_builder

st.write('bike + bus Line model')

if 'bike_bus_line_model' not in st.session_state:
    bike_bus_line_model = m.Model(m.ModelType.BIKE_BUS)
    bike_bus_line_model.load_data(os.path.join(co.ROOT_PATH, 'bike_bus_line'))
    st.session_state.bike_bus_line_model = bike_bus_line_model
cur_model = st.session_state.bike_bus_line_model

cw_layer = pdk_layer_builder.get_warehouse_layer()
parcel_layer = pdk_layer_builder.get_parcel_layer()
round_layers = pdk_layer_builder.get_rounds_layer(cur_model)
all_layers = [cw_layer, parcel_layer] + round_layers

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

