import os

import streamlit as st
import pydeck as pdk

import model as m
import constants as co
import pdk_layer_builder

st.write('van model')

if 'van_model' not in st.session_state:
    van_model = m.Model(m.ModelType.VAN)
    van_model.load_data(os.path.join(co.ROOT_PATH, 'van'))
    st.session_state.van_model = van_model
van_model = st.session_state.van_model


cw_layer = pdk_layer_builder.get_warehouse_layer()
parcel_layer = pdk_layer_builder.get_parcel_layer()
round_layers = pdk_layer_builder.get_rounds_layer(van_model)
all_layers = [cw_layer, parcel_layer] + round_layers

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

