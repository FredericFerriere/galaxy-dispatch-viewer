

class Client:
    def __init__(self, client_id, client_name, latitude, longitude):
        self.id = client_id
        self.name = client_name
        self.latitude = latitude
        self.longitude = longitude
        self.parcel_ids = []

    def add_parcel(self, parcel_id):
        self.parcel_ids.append(parcel_id)
