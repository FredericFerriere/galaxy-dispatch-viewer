

class Parcel():

    def __init__(self, parcel_id, delivery_latitude, delivery_longitude, client_id):
        self.id = parcel_id
        self.delivery_latitude = delivery_latitude
        self.delivery_longitude = delivery_longitude
        self.client_id = client_id