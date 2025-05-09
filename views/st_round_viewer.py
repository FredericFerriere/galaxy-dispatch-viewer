import streamlit as st

import constants as co
import data.parcels as ps
import pdk_layer_builder

def view_rounds(cur_model, selected_tasks):

    selected_rounds = [cur_model.get_task(t_id).delivery_round_id for t_id in selected_tasks]
    client_ids = set([ps.Parcels.get_parcel(cur_model.get_round(r_id).parcel_ids[0]).client_id
                        for r_id in selected_rounds])
    parcel_ids = [p_id for round_id in selected_rounds for p_id in cur_model.get_round(round_id).parcel_ids]

    cw_layer = pdk_layer_builder.get_warehouse_layer(client_ids)
    parcel_layer = pdk_layer_builder.get_parcel_layer(parcel_ids)
    round_layers = pdk_layer_builder.get_rounds_layer(cur_model, selected_tasks)
    all_layers = [cw_layer, parcel_layer] + round_layers

    pdk_layer_builder.draw_map(co.CENTER_LATITUDE, co.CENTER_LONGITUDE, all_layers)

