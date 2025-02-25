import os
from enum import Enum

import pandas as pd
import streamlit as st

import constants as co
import data.round_holder as rh
import data.model_stats as ms
import data.parcels as ps
import data.task_holder as th


#class ModelType(Enum):
#    VAN = 0
#    BIKE = 1
#    BIKE_BUS_ZONED = 2
#    BIKE_BUS_LINE = 3

class Model:

    def __init__(self, model_name, folder_name, display_name):
        self.model_name = model_name
        self.model_stats = ms.ModelStats()
        self.folder_name = folder_name
        self.display_name = display_name
        self.round_holder = rh.RoundHolder()
        self.task_holder = th.TaskHolder()

    def load_data(self, root_path):
        model_path = os.path.join(root_path, self.folder_name)
        self.round_holder.load_data(model_path)
        self.task_holder.load_data(model_path)
        self.model_stats.load_data(model_path)

    @staticmethod
    def get_model(model_name):
        if 'models' not in st.session_state:
            st.session_state.models = dict()
        if model_name not in st.session_state.models.keys():
            cur_model = Model(model_name, co.MODEL_MAP[model_name][0], co.MODEL_MAP[model_name][1])
            cur_model.load_data(co.ROOT_PATH)
            st.session_state.models[model_name] = cur_model
        return st.session_state.models[model_name]

    def get_round(self, round_id):
        return self.round_holder.round_dict[round_id]

    def client_round_df(self):
        client_ids, round_ids = [], []
        for k, v in self.round_holder.round_dict.items():
            client_ids.append(ps.Parcels.get_parcel(v.parcel_ids[0]).client_id)
            round_ids.append(k)
        return pd.DataFrame({'client_id':client_ids, 'round_id':round_ids})


    @staticmethod
    def models_metrics_df(model_list):
        data_dict = {'metrics_name': ['Work Time (seconds)', 'Tasks Duration (seconds)', 'Distance (km)']}
        data_dict.update({
            el.display_name: [int(el.model_stats.total_work_time), int(el.model_stats.total_duration),
                              int(el.model_stats.total_distance)] for el in model_list
        })
        return pd.DataFrame(data_dict)