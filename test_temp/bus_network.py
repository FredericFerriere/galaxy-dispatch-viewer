import os

import pandas as pd
import numpy as np

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
        #BusNetwork.load_bus_stops(network_path)
        #BusNetwork.load_trips(network_path)
        return

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
    def reachable_stops_old(cls, latitude, longitude, radius):
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

    @staticmethod
    def distance_vec(latitude_A, longitude_A, latitude_B, longitude_B):
        return distance.distance((latitude_A, longitude_A), (latitude_B, longitude_B)).meters

    def reachable_stops(cls, latitude, longitude, radius):
        bn_path = r'C:\Users\frede\Galaxy_dev\Lyon_bus'
        df_stops = pd.read_csv(os.path.join(bn_path, 'stops.txt'),sep=',',
                               usecols=['stop_id', 'stop_name', 'stop_lat', 'stop_lon'],
                               dtype={'stop_id': str,
                                      'stop_name':str,
                                      'stop_lat': np.float64,
                                      'stop_lon': np.float64})
        df_stop_times = pd.read_csv(os.path.join(bn_path, 'stop_times.txt'),sep=',',
                                    usecols=['trip_id', 'stop_id'],
                                    dtype={'trip_id': str,
                                           'stop_id': str})
        df_trips = pd.read_csv(os.path.join(bn_path, 'trips.txt'), sep=',')
        df_routes = pd.read_csv(os.path.join(bn_path, 'routes.txt'),sep=',')

#        df_routes = df_routes[df_routes['route_short_name']=='C25']

        df_stops['distance'] = np.vectorize(BusNetwork.distance_vec)(latitude, longitude,
                                                                     df_stops['stop_lat'], df_stops['stop_lon'])
        df_close_stops = df_stops[df_stops['distance']<=radius]
        df_eligible_trips = pd.merge(df_close_stops, df_stop_times)
        eligible_trips_id = df_eligible_trips['trip_id'].unique()

        eligible_stops = df_stop_times[df_stop_times['trip_id'].isin(eligible_trips_id)]['stop_id'].unique()
        eligible_routes = df_trips[df_trips['trip_id'].isin(eligible_trips_id)]['route_id'].unique()
        routes_data = df_routes[df_routes['route_id'].isin(eligible_routes)][['route_id', 'route_short_name', 'route_long_name']]

        return df_stops[df_stops['stop_id'].isin(eligible_stops)], routes_data

