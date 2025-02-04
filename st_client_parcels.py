import streamlit as st
import pydeck as pdk

import constants as co
import pdk_layer_builder




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
all_layers = [cw_layer, parcel_layer]

draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)