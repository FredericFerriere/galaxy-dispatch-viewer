import streamlit as st
import pandas as pd

map_data = []

map_data.append({'type':'warehouse',
                   'latitude':45.92317320402719,
                   'longitude':6.161847208616907,
                   'color':(255,0,0)})
map_data.append({'type':'warehouse',
                   'latitude':45.913261165996246,
                   'longitude':6.139788724105191,
                   'color':(255,0,0)})
map_data.append({'type':'warehouse',
                   'latitude':45.90167497412467,
                   'longitude':6.123566725767781,
                   'color':(0,255,0)})


map_df = pd.DataFrame(data=map_data)

st.map(data=map_df, latitude='latitude', longitude='longitude', color='color', size=1000)
