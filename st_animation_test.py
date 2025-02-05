import time

import pydeck as pdk
import pandas as pd
import streamlit as st

TRIPS_LAYER_DATA = {"waypoints": [
        {
        "coordinates": [-122.39079879999997,37.7664413],"timestamp": 0
        },
        {
        "coordinates": [-122.3908298,37.7667706],"timestamp": 1
        },
        {
        "coordinates": [-122.39271759999997,37.7667484],"timestamp": 2
        }
        ]
    }

#json_file = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf.trips.json"
df = pd.DataFrame.from_dict(TRIPS_LAYER_DATA)
#df.to_csv("df_format.csv")

#df["coordinates"] = df["waypoints"].apply(lambda f: [item["coordinates"] for item in f])
#df["timestamps"] = df["waypoints"].apply(lambda f: [item["timestamp"] - 1554772579000 for item in f])

df.drop(["waypoints"], axis=1, inplace=True)

layer = pdk.Layer(
    "TripsLayer",
    df,
    get_path="coordinates",
    get_timestamps="timestamps",
    get_color=[253, 128, 93],
    opacity=0.8,
    width_min_pixels=5,
    rounded=True,
    trail_length=600,
    current_time=500,
)

view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=11, bearing=0, pitch=45)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
for i in range(3):
    layer.current_time = i
    #r.update()
    time.sleep(1)

st.pydeck_chart(r)

#r.to_html("trips_layer.html")