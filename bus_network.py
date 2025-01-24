import os

import pandas as pd

from geopy import distance

class BusStop:
    def __init__(self, stop_id, name, latitude, longitude):
        self.id = stop_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.trip_ids = []

    def add_trip(self, trip_id):
        self.trip_ids.append(trip_id)

    def get_trip_ids(self):
        return self.trip_ids

class Trip:
    def __init__(self, trip_id, route_id):
        self.id = trip_id
        self.route_id = route_id
        self.stop_ids = []

    def add_stop(self, stop_id):
        self.stop_ids.append(stop_id)
        BusNetwork.bus_stops[stop_id].add_trip(self.id)

    def get_stop_ids(self):
        return self.stop_ids


class BusNetwork:

    bus_stops = dict()
    trips = dict()

    @classmethod
    def create_from_files(cls, network_path):
        BusNetwork.load_bus_stops(network_path)
        BusNetwork.load_trips(network_path)

    @classmethod
    def load_bus_stops(cls, network_path):
        df = pd.read_csv(os.path.join(network_path, 'stops.txt'), sep=',')
        for _, row in df.iterrows():
            BusNetwork.bus_stops[str(row['stop_id'])] = BusStop(str(row['stop_id']), row['stop_name'], float(row['stop_lat']), float(row['stop_lon']))
        print('stops loaded')

    @classmethod
    def load_trips(cls, network_path):
        df_trips = pd.read_csv(os.path.join(network_path, 'trips.txt'), sep=',')
        for _, row in df_trips.iterrows():
            BusNetwork.trips[str(row['trip_id'])] = Trip(str(row['trip_id']), str(row['route_id']))
        print('trips loaded')

        df_stop_times = pd.read_csv(os.path.join(network_path, 'stop_times.txt'), sep=',')
        for _, row in df_stop_times.iterrows():
            BusNetwork.trips[str(row['trip_id'])].add_stop(str(row['stop_id']))
        print('trip/stop mapping loaded')



    @classmethod
    def reachable_stops(cls, latitude, longitude, radius):
        start_stop_ids = []
        for k, v in BusNetwork.bus_stops.items():
            #calculate distance
            cur_distance = distance.distance((latitude, longitude), (v.latitude, v.longitude)).meters
            if cur_distance<=radius:
                start_stop_ids.append(v.id)

        reachable_stops = []
        for stop_id in start_stop_ids:
            trip_ids = BusNetwork.bus_stops[stop_id].get_trip_ids()
            for trip_id in trip_ids:
                reachable_stops+=BusNetwork.trips[trip_id].get_stop_ids()

        return set(reachable_stops)
