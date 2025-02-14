import streamlit as st

import constants as co
import pdk_layer_builder

def view_rounds(cur_model):

    cw_layer = pdk_layer_builder.get_warehouse_layer()
    parcel_layer = pdk_layer_builder.get_parcel_layer()
    round_layers = pdk_layer_builder.get_rounds_layer(cur_model)
    all_layers = [cw_layer, parcel_layer] + round_layers

    pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

