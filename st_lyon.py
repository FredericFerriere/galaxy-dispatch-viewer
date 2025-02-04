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

def get_stops_layer(eligible_stops):
    stops_layer = pdk.Layer(
        'ScatterplotLayer',
        data=eligible_stops,
        get_position=['stop_lon', 'stop_lat'],
        get_radius=20,
        get_color=[255, 0, 0, 255]
    )
    return stops_layer

def get_delivery_layer(eligible_stops):
    delivery_layer = pdk.Layer(
        'ScatterplotLayer',
        data=eligible_stops,
        get_position=['stop_lon', 'stop_lat'],
        get_radius=1500,
        get_color=[255, 0, 0, 10]
    )
    return delivery_layer


def draw_map(initial_lat, initial_lon, all_layers):

    st.pydeck_chart(
        pdk.Deck(
            map_style='road',
            initial_view_state=pdk.ViewState(
                latitude=initial_lat,
                longitude=initial_lon,
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

#col_map, col_routes = st.columns([0.7,0.3])

current_lat = st.number_input('warehouse latitude', value=45.67952307359677)
current_lon = st.number_input('warehouse longitude', value=4.928785699081165)
current_radius = st.number_input('load radius', value=400, step=10)

cw_layer = get_warehouse_layer(current_lat, current_lon)
cw_radius_layer = get_radius_layer(current_lat, current_lon, current_radius)
eligible_stops, eligible_routes = st.session_state.bus_network.reachable_stops(current_lat, current_lon, current_radius)
stops_layer = get_stops_layer(eligible_stops)
delivery_layer = get_delivery_layer(eligible_stops)

all_layers = [cw_layer, cw_radius_layer, stops_layer, delivery_layer]

draw_map(current_lat, current_lon, all_layers)

st.table(eligible_routes)
