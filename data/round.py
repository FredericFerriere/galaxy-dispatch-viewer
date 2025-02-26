import data.parcels as ps

class Round:

    def __init__(self, round_id, start_latitude, start_longitude, end_latitude, end_longitude):
        self.id = round_id
        self.start_latitude = start_latitude
        self.start_longitude = start_longitude
        self.end_latitude = end_latitude
        self.end_longitude = end_longitude
        self.parcel_ids = []

    def add_parcel(self, parcel_id):
        self.parcel_ids.append(parcel_id)

    def get_path(self, cur_model, move_mode):
        prev_lat, prev_lon = self.start_latitude, self.start_longitude
        path = []

        for el in self.parcel_ids:
            cur_lat, cur_lon = ps.Parcels.get_parcel(el).delivery_latitude, ps.Parcels.get_parcel(el).delivery_longitude
            new_path = cur_model.get_path(prev_lat, prev_lon, cur_lat, cur_lon, move_mode)
            path = path + new_path
            prev_lat, prev_lon = cur_lat, cur_lon

        cur_lat, cur_lon = self.end_latitude, self.end_longitude
        new_path = cur_model.get_path(prev_lat, prev_lon, cur_lat, cur_lon, move_mode)
        path = path + new_path

#        path = ([[self.start_longitude, self.start_latitude]]
#                + [[ps.Parcels.get_parcel(el).delivery_longitude, ps.Parcels.get_parcel(el).delivery_latitude]
#                 for el in self.parcel_ids]
#                + [[self.end_longitude, self.end_latitude]])
        return path
