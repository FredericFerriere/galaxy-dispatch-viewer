import os

import pandas as pd

import data.task as ta
import data.location as loc

class TaskHolder:

    def __init__(self):
        self.task_dict = {}

    def load_data(self, model_path):
        self.load_collection_tasks(model_path)
        self.load_imported_round_tasks(model_path)
        self.load_local_round_tasks(model_path)


    def load_collection_tasks(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'collection_tasks.csv'), sep=';')
        for _, row in df.iterrows():
            start_loc = loc.Location(row['start_location_latitude'], row['start_location_longitude'])
            end_loc = loc.Location(row['end_location_latitude'], row['end_location_longitude'])
            new_task = ta.Collection(row['task_id'], start_loc, end_loc, row['agent_id'])
            self.task_dict[new_task.id] = new_task

    def load_imported_round_tasks(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'imported_round_tasks.csv'), sep=';')
        for _, row in df.iterrows():
            start_loc = loc.Location(row['start_location_latitude'], row['start_location_longitude'])
            end_loc = loc.Location(row['end_location_latitude'], row['end_location_longitude'])
            new_task = ta.ImportedRound(row['task_id'], start_loc, end_loc, row['round_id'], row['agent_id'])
            self.task_dict[new_task.id] = new_task

    def load_local_round_tasks(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'local_round_tasks.csv'), sep=';')
        for _, row in df.iterrows():
            start_loc = loc.Location(row['start_location_latitude'], row['start_location_longitude'])
            end_loc = loc.Location(row['end_location_latitude'], row['end_location_longitude'])
            new_task = ta.LocalRound(row['task_id'], start_loc, end_loc, row['round_id'], row['agent_id'])
            self.task_dict[new_task.id] = new_task

    def get_task(self, task_id):
        return self.task_dict[task_id]


