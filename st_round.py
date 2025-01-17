import os

import pandas as pd
import streamlit as st
import pydeck as pdk

import rounds as rs
import parcels as ps


def load_data(parcels_path, rounds_path):
    ps.Parcels.load_data(parcels_path)
    rs.Rounds.load_data(rounds_path)


def display_rounds(rounds_path):

    df_rounds = pd.read_csv(os.path.join(rounds_path, 'rounds.csv'), sep=';')
    all_rounds = st.dataframe(df_rounds, on_select="rerun", selection_mode='single-row')

    all_layers = []

    for row_num in all_rounds.selection.rows:
        row = df_rounds.iloc[row_num]
        round_id = row['round_id']
        cur_round = rs.Rounds.round_dict[round_id]
        # points
        start_point = [{'latitude':cur_round.start_latitude, 'longitude':cur_round.start_longitude}]
        delivery_points = [{'latitude': ps.Parcels.parcel_dict[el].delivery_latitude,
                   'longitude': ps.Parcels.parcel_dict[el].delivery_longitude} for el in cur_round.parcel_ids]
        start_point_layer = pdk.Layer(
            'ScatterplotLayer',
            data=start_point,
            get_position=['longitude', 'latitude'],
            get_radius=100,
            get_color=[255,0,0,255]
        )
        delivery_layer = pdk.Layer(
            'ScatterplotLayer',
            data=delivery_points,
            get_position=['longitude', 'latitude'],
            get_radius=100,
            get_color=[0, 0, 255, 255]
        )
        round_layer = pdk.Layer(
            'PathLayer',
#            positionFormat= 'XY',
            data=[{'path':[[cur_round.start_longitude, cur_round.start_latitude]]
                           +[[el['longitude'], el['latitude']] for el in delivery_points]
                           +[[cur_round.start_longitude, cur_round.start_latitude]]}],
            get_width=20,
#            width_scale=20,
            get_path='path',
            get_color=[255, 0, 255, 255]
        )

        all_layers.append(start_point_layer)
        all_layers.append(delivery_layer)
        all_layers.append(round_layer)

    st.pydeck_chart(
        pdk.Deck(
            map_style='road',
            initial_view_state=pdk.ViewState(
                latitude=45.9,
                longitude=6.13,
                zoom=11,
                pitch=0,
            ),
            layers=all_layers
        )
    )

parcels_path = r'C:\Users\frede\Galaxy_dev\test_data\outputs'
mode_path = r'C:\Users\frede\Galaxy_dev\test_data\outputs\van'

load_data(parcels_path, mode_path)
display_rounds(mode_path)

