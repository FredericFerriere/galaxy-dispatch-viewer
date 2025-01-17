import os
import pandas as pd
import round as r

class Rounds():

    round_dict = {}

    @classmethod
    def load_data(cls, file_path):
        df_r = pd.read_csv(os.path.join(file_path, 'rounds.csv'), sep=';')
        for _, row in df_r.iterrows():
            Rounds.round_dict[row['round_id']] = r.Round(row['round_id'], row['start_location_latitude'],
                                                         row['start_location_longitude'])

        df_rs = pd.read_csv(os.path.join(file_path, 'round_sequences.csv'), sep=';')
        df_rs.sort_values(['round_id', 'sequence_number'], inplace=True)
        for _, row in df_rs.iterrows():
            Rounds.round_dict[row['round_id']].add_parcel(row['parcel_id'])
