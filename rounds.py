import os
import pandas as pd
import round as r

class Rounds:

    def __init__(self):
        self.round_dict = {}

    def load_data(self, model_path):
        df_r = pd.read_csv(os.path.join(model_path, 'rounds.csv'), sep=';')
        for _, row in df_r.iterrows():
            self.round_dict[row['round_id']] = r.Round(row['round_id'], row['start_location_latitude'],
                    row['start_location_longitude'], row['end_location_latitude'], row['end_location_longitude'])

        df_rs = pd.read_csv(os.path.join(model_path, 'round_sequences.csv'), sep=';')
        df_rs.sort_values(['round_id', 'sequence_number'], inplace=True)
        for _, row in df_rs.iterrows():
            self.round_dict[row['round_id']].add_parcel(row['parcel_id'])
