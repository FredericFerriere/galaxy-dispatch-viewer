
import pandas as pd
import streamlit as st

import data.model as m


st.title('Model Metrics')
models = [m.Model.get_model('van'),
          m.Model.get_model('bike'),
          m.Model.get_model('bike_bus_zoned'),
          m.Model.get_model('bike_bus_line'),
          m.Model.get_model('bike_bus_hub'),
          m.Model.get_model('bike_bus_zoned_line')]

df = pd.DataFrame(m.Model.models_metrics_df(models))
df.set_index('metrics_name', inplace=True)

st.table(df)
