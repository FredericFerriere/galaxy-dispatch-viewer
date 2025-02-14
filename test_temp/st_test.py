import streamlit as st
import pandas as pd

source_target_path = r'C:\Users\frede\Galaxy_dev\test_data\outputs\source_target.csv'
source_target_df = pd.read_csv(source_target_path, sep=';')

num_parcels = len(source_target_df)
st.write('Nombre de colis: {}'.format(num_parcels))

selected_parcels = st.dataframe(source_target_df, on_select="rerun", selection_mode = "multi-row")
print('parcels: {}'.format(selected_parcels.selection))

map_data = []

for row_num in selected_parcels.selection['rows']:
  row = source_target_df.iloc[row_num]
  map_data.append({'type':'warehouse',
                   'latitude':row['client_latitude'],
                   'longitude':row['client_longitude'],
                   'color':(255,0,0),
                   'size':10})
  map_data.append({'type': 'warehouse_stop',
                   'latitude': row['source_stop_latitude'],
                   'longitude': row['source_stop_longitude'],
                   'color': (125, 0, 0),
                   'size': 10})
  map_data.append({'type': 'delivery',
                   'latitude': row['delivery_latitude'],
                   'longitude': row['delivery_longitude'],
                   'color': (0, 0, 255),
                   'size': 10})
  map_data.append({'type': 'delivery_stop',
                   'latitude': row['target_stop_latitude'],
                   'longitude': row['target_stop_longitude'],
                   'color': (0, 0, 125),
                   'size': 10})


map_df = pd.DataFrame(data=map_data)

st.map(data=map_df, latitude='latitude', longitude='longitude', color='color')
