import streamlit as st
import pydeck as pdk

import data.clients as cs
import constants as co
import data.parcels as ps
import pdk_layer_builder


cw_layer = pdk_layer_builder.get_warehouse_layer(list(cs.Clients.client_ids()))
parcel_layer = pdk_layer_builder.get_parcel_layer(list(ps.Parcels.parcel_ids()))
all_layers = [cw_layer, parcel_layer]

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)