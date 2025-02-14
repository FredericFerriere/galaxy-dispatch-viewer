import os
from enum import Enum

import pandas as pd
import streamlit as st

import constants as co
import data.rounds as r
import data.model_stats as ms

#class ModelType(Enum):
#    VAN = 0
#    BIKE = 1
#    BIKE_BUS_ZONED = 2
#    BIKE_BUS_LINE = 3

class Model:

    def __init__(self, model_name, folder_name, display_name):
#        self.model_type = model_type
        self.rounds = r.Rounds()
        self.model_name = model_name
        self.model_stats = ms.ModelStats()
        self.folder_name = folder_name
        self.display_name = display_name

    def load_data(self, root_path):
        model_path = os.path.join(root_path, self.folder_name)
        self.rounds.load_data(model_path)
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

    @staticmethod
    def models_metrics_df(model_list):
        data_dict = {'metrics_name': ['Work Time (seconds)', 'Tasks Duration (seconds)', 'Distance (km)']}
        data_dict.update({
            el.display_name: [int(el.model_stats.total_work_time), int(el.model_stats.total_duration),
                              int(el.model_stats.total_distance)] for el in model_list
        })
        return pd.DataFrame(data_dict)