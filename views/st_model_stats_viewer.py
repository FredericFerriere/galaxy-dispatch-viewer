
import pandas as pd
import streamlit as st

import data.model as m

def view_model_stats(cur_model):
    df = pd.DataFrame(m.Model.models_metrics_df([cur_model]))
    df.set_index('metrics_name', inplace=True)

    st.table(df)
