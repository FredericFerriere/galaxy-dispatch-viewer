import random

import streamlit as st
import pydeck as pdk

import parcels as ps

#warehouse_icon_url = 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Warehouse_Icon.png'
#warehouse_icon_url = 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png'

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

def get_warehouse_layer():
    all_clients = st.session_state.clients

    cw_point = [{'latitude': v.latitude,
                 'longitude': v.longitude,
                 } for v in all_clients.client_dict.values()]
    cw_layer = pdk.Layer(
        'ScatterplotLayer',
        data=cw_point,
        get_position=['longitude', 'latitude'],
        get_radius=50,
        get_color=[0, 0, 0, 255]
    )

    return cw_layer

def get_warehouse_layer_2():
    all_clients = st.session_state.clients

    cw_point = [{'latitude': v.latitude,
                 'longitude': v.longitude,
                 } for v in all_clients.client_dict.values()]
    cw_layer = pdk.Layer(
        'IconLayer',
        data=cw_point,
        get_position=['longitude', 'latitude'],
        get_icon='marker',
        get_size=40,
        icon_atlas='https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png',
        icon_mapping='https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.json',
        get_color=[255, 0, 120],
        pickable=True,
    )

    return cw_layer

def get_parcel_layer():
    all_parcels = st.session_state.parcels

    parcel_point = [{'latitude': v.delivery_latitude,
                 'longitude': v.delivery_longitude,
                 } for v in all_parcels.parcel_dict.values()]

    parcel_layer = pdk.Layer(
        'ScatterplotLayer',
        data=parcel_point,
        get_position=['longitude', 'latitude'],
        get_radius=50,
        get_color=[255, 0, 0, 255]
    )

    return parcel_layer

def get_rounds_layer(current_model):
    random.seed(7878)
    round_layers = []

    for cur_round in current_model.rounds.round_dict.values():
        round_layer = pdk.Layer(
            'PathLayer',
            #            positionFormat= 'XY',
            data=[{'path': [[cur_round.start_longitude, cur_round.start_latitude]]
                           + [[ps.Parcels.parcel_dict[el].delivery_longitude,
                               ps.Parcels.parcel_dict[el].delivery_latitude] for el in cur_round.parcel_ids]
                           + [[cur_round.end_longitude, cur_round.end_latitude]]}],
            get_width=30,
            #            width_scale=20,
            get_path='path',
            get_color=[random.randint(0,255), random.randint(0,255), random.randint(0,255), 255]
        )
        round_layers.append(round_layer)

    return round_layers

def get_point_layer(point_latitude, point_longitude):

    point = [{'latitude': point_latitude,
              'longitude': point_longitude}]

    point_layer = pdk.Layer(
        'ScatterplotLayer',
        data=point,
        get_position=['longitude', 'latitude'],
        get_radius=50,
        get_color=[255, 0, 0, 255]
    )

    return point_layer

