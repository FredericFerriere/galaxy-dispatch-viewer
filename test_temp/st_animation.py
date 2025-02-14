import time

import streamlit as st

import constants as co
import pdk_layer_builder

data = [(45.93529271387049,6.164920219524343),
        (45.93363293801361,6.18034321635261),
        (45.91495483822621,6.09337877987635),
        (45.9180450463896,6.086077201101151),
        (45.91941171231432,6.063532953281703)
        ]

if 'anim_counter' not in st.session_state:
    st.session_state.anim_counter = 0


while st.session_state.anim_counter<len(data):
    el = data[st.session_state.anim_counter]
    all_layers = [pdk_layer_builder.get_point_layer(el[0], el[1])]
    pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)
    time.sleep(2)
    st.session_state.anim_counter+=1
    st.rerun()

pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, [])
