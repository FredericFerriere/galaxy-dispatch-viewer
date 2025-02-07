

class Round():

    def __init__(self, round_id, start_latitude, start_longitude, end_latitude, end_longitude):
        self.id = round_id
        self.start_latitude = start_latitude
        self.start_longitude = start_longitude
        self.end_latitude = end_latitude
        self.end_longitude = end_longitude
        self.parcel_ids = []

    def add_parcel(self, parcel_id):
        self.parcel_ids.append(parcel_id)