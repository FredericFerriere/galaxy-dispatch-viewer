import streamlit as st
import pydeck as pdk

import constants as co
import pdk_layer_builder


cw_layer = pdk_layer_builder.get_warehouse_layer()
parcel_layer = pdk_layer_builder.get_parcel_layer()
all_layers = [cw_layer, parcel_layer]

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)