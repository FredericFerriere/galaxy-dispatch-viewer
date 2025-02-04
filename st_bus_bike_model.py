import os

import streamlit as st
import pydeck as pdk

import model as m
import constants as co
import pdk_layer_builder

st.write('bus + bike model')

if 'bus_bike_model' not in st.session_state:
    bus_bike_model = m.Model(m.ModelType.BIKE)
    bus_bike_model.load_data(os.path.join(co.ROOT_PATH, 'bus_bike'))
    st.session_state.bus_bike_model = bus_bike_model
bus_bike_model = st.session_state.bus_bike_model

def draw_map(initial_lat, initial_lon, all_layers):

    st.pydeck_chart(
        pdk.Deck(
            map_style='road',
            initial_view_state=pdk.ViewState(
                latitude=initial_lat,
                longitude=initial_lon,
                zoom=11,
                pitch=0,
            ),
            layers=all_layers
        )
    )
    return

cw_layer = pdk_layer_builder.get_warehouse_layer()
parcel_layer = pdk_layer_builder.get_parcel_layer()
round_layers = pdk_layer_builder.get_rounds_layer(bus_bike_model)
all_layers = [cw_layer, parcel_layer] + round_layers

draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

