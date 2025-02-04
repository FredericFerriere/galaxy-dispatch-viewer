import pandas as pd

import client as c

class Clients:
    client_dict = {}

    @classmethod
    def load_data(cls, file_path):
        df = pd.read_csv(file_path, sep=';')
        for _, row in df.iterrows():
            Clients.client_dict[row['client_id']] = c.Client(row['client_id'], row['client_name'],
                                                             row['latitude'], row['longitude'])