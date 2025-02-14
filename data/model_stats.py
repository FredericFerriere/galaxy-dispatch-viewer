import os
import pandas as pd

class ModelStats:
    def __init__(self):
        self.num_deliverers = 0
        self.num_robots = 0
        self.total_duration = 0
        self.total_work_time = 0
        self.total_distance = 0

    def load_data(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'model_stats.csv'), sep=';')
        self.num_deliverers = df.iloc[0]['num_deliverers']
        self.num_robots = df.iloc[0]['num_robots']
        self.total_work_time = df.iloc[0]['total_work_time']
        self.total_duration = df.iloc[0]['total_duration']
        self.total_distance = df.iloc[0]['total_distance']

    def get_display_df(self):
        df = pd.DataFrame(
            {
                'Metric': ['Work Time', 'Tasks Duration', 'Distance', 'Deliverers', 'Robots'],
                'Value': [int(self.total_work_time), int(self.total_duration), int(self.total_distance), self.num_deliverers, self.num_robots]
            }
        )
        return df