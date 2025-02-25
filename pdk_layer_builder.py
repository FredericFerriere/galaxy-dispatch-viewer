import random

import streamlit as st
import pydeck as pdk

import data.clients as cs
import data.parcels as ps


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

def get_warehouse_layer(client_ids):

    cw_point = [{'latitude': cs.Clients.get_client(c_id).latitude,
                 'longitude': cs.Clients.get_client(c_id).longitude,
                 } for c_id in client_ids]
    cw_layer = pdk.Layer(
        'ScatterplotLayer',
        data=cw_point,
        get_position=['longitude', 'latitude'],
        get_radius=50,
        get_color=[0, 0, 0, 255]
    )

    return cw_layer


def get_parcel_layer(parcel_ids):
    all_parcels = ps.Parcels.get_parcels()

    parcel_point = [{'latitude': ps.Parcels.get_parcel(p_id).delivery_latitude,
                 'longitude': ps.Parcels.get_parcel(p_id).delivery_longitude,
                 } for p_id in parcel_ids]

    parcel_layer = pdk.Layer(
        'ScatterplotLayer',
        data=parcel_point,
        get_position=['longitude', 'latitude'],
        get_radius=50,
        get_color=[255, 0, 0, 255]
    )

    return parcel_layer

def get_rounds_layer(current_model, round_ids):
    random.seed(7878)
    round_layers = []

    for round_id in round_ids:
        cur_round = current_model.get_round(round_id)
        round_layer = pdk.Layer(
            'PathLayer',
            #            positionFormat= 'XY',
            data=[{'path': [[cur_round.start_longitude, cur_round.start_latitude]]
                           + [[ps.Parcels.get_parcel(el).delivery_longitude,
                               ps.Parcels.get_parcel(el).delivery_latitude] for el in cur_round.parcel_ids]
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

