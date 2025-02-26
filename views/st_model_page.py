import streamlit as st

import data.clients as cs
import data.model as model
import views.st_model_stats_viewer as msv
import views.st_round_viewer as rv

def view_model(cur_model:model):
    st.title(cur_model.display_name)
    mod_summary, mod_anim = st.tabs(['Summary', 'Animation'])
    with mod_summary:
        col_data, col_map = st.columns([1,2])
        with col_data:
            msv.view_model_stats(cur_model)
            df_client_task = st.dataframe(cur_model.client_round_task_df(), hide_index=True,
                                            selection_mode="multi-row", on_select="rerun")
        with col_map:
            sel_tasks = [cur_model.client_round_task_df().iloc[sel]['task_id'] for sel in df_client_task.selection['rows']]
            rv.view_rounds(cur_model, sel_tasks)

    with mod_anim:
        st.text("animation")

