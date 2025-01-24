import streamlit as st
import pandas as pd
import pydeck as pdk
import bus_network as bn



def get_warehouse_layer(latitude, longitude):
    cw_point = [{'latitude': latitude, 'longitude': longitude}]
    cw_layer = pdk.Layer(
        'ScatterplotLayer',
        data=cw_point,
        get_position=['longitude', 'latitude'],
        get_radius=10,
        get_color=[0, 0, 0, 255]
    )
    return cw_layer

def get_radius_layer(latitude, longitude, radius):
    cw_point = [{'latitude': latitude, 'longitude': longitude}]
    cw_radius_layer = pdk.Layer(
        'ScatterplotLayer',
        data=cw_point,
        get_position=['longitude', 'latitude'],
        get_radius=radius,
        get_color=[0, 0, 0, 100]
    )
    return cw_radius_layer

def get_stops_layer(latitude, longitude, radius):
    reachable_stops = st.session_state.bus_network.reachable_stops(latitude, longitude, radius)
#    stop_points = [{'latitude': st.session_state.bus_network.bus_stops[stop_id].latitude,
#                    'longitude': st.session_state.bus_network.bus_stops[stop_id].longitude}
#                   for stop_id in reachable_stops]
    stops_layer = pdk.Layer(
        'ScatterplotLayer',
        data=reachable_stops,
        get_position=['stop_lon', 'stop_lat'],
        get_radius=20,
        get_color=[255, 0, 0, 255]
    )
    return stops_layer


def draw_map(cw_lat, cw_lon, cw_radius):
    all_layers = []

    cw_layer = get_warehouse_layer(cw_lat, cw_lon)
    cw_radius_layer = get_radius_layer(cw_lat, cw_lon, cw_radius)
    cw_stops = get_stops_layer(cw_lat, cw_lon, cw_radius)

    all_layers.append(cw_layer)
    all_layers.append(cw_radius_layer)
    all_layers.append(cw_stops)

    st.pydeck_chart(
        pdk.Deck(
            map_style='road',
            initial_view_state=pdk.ViewState(
                latitude=cw_lat,
                longitude=cw_lon,
                zoom=14,
                pitch=0,
            ),
            layers=all_layers
        )
    )
    return

def load_data():
    print('load_data')
    return

def show_inputs():
    print('show_inputs')
    return

bus_network_path = r'C:\Users\frede\Galaxy_dev\Lyon_bus'
if 'bus_network' not in st.session_state:
    bus_net = bn.BusNetwork()
    bus_net.create_from_files(bus_network_path)
    st.session_state.bus_network = bus_net


current_lat = st.number_input('warehouse latitude', value=45.71041)
current_lon = st.number_input('warehouse longitude', value=4.86803)
current_radius = st.number_input('load radius', value=400, step=10)

draw_map(current_lat, current_lon, current_radius)