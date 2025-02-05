import os

import streamlit as st
import pydeck as pdk

import model as m
import constants as co
import pdk_layer_builder

st.write('bike model')

if 'bike_model' not in st.session_state:
    bike_model = m.Model(m.ModelType.BIKE)
    bike_model.load_data(os.path.join(co.ROOT_PATH, 'bike'))
    st.session_state.bike_model = bike_model
bike_model = st.session_state.bike_model


cw_layer = pdk_layer_builder.get_warehouse_layer()
parcel_layer = pdk_layer_builder.get_parcel_layer()
round_layers = pdk_layer_builder.get_rounds_layer(bike_model)
all_layers = [cw_layer, parcel_layer] + round_layers

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

