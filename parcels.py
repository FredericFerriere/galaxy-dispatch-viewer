import pandas as pd

import parcel as p

class Parcels:
    parcel_dict = {}

    @classmethod
    def load_data(cls, file_path):
        df = pd.read_csv(file_path, sep=';')
        for _, row in df.iterrows():
            Parcels.parcel_dict[row['parcel_id']] = p.Parcel(row['parcel_id'], row['delivery_latitude'],
                                                             row['delivery_longitude'], row['client_id'])
