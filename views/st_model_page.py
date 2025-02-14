import streamlit as st

import views.st_model_stats_viewer as msv
import views.st_round_viewer as rv

def view_model(cur_model):
    st.title(cur_model.display_name)
    mod_summary, mod_anim = st.tabs(['Summary', 'Animation'])
    with mod_summary:
        col_stats, col_rounds = st.columns([1,3])
        with col_stats:
            msv.view_model_stats(cur_model)
        with col_rounds:
            rv.view_rounds(cur_model)

    with mod_anim:
        st.text("animation")

