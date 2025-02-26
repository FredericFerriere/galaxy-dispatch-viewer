import os

import pandas as pd

import data.route_segment as rs

class RouteHolder:

    def __init__(self):
        self.route_dict = dict()

    def load_data(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'routes.csv'), sep=';')
        for _, row in df.iterrows():
            start_lat = row['from_lat']
            start_lon = row['from_lon']
            end_lat = row['to_lat']
            end_lon = row['to_lon']
            mode = row['move_mode']
            if (start_lat, start_lon, end_lat, end_lon, mode) not in self.route_dict:
                self.route_dict[(start_lat, start_lon, end_lat, end_lon, mode)] = []
            cur_route = self.route_dict[(start_lat, start_lon, end_lat, end_lon, mode)]
            cur_route.append(rs.RouteSegment(row['step_sequence'], row['step_start_lat'], row['step_start_lon'],
                                             row['distance_meters'], row['duration_seconds']))
        for v in self.route_dict.values():
            v.sort(key=lambda x:x.sequence)

    def get_route(self, start_lat, start_lon, end_lat, end_lon, move_mode):
        if (start_lat, start_lon, end_lat, end_lon, move_mode) not in self.route_dict:
            return []
        return self.route_dict[(start_lat, start_lon, end_lat, end_lon, move_mode)]

    def get_path(self, start_lat, start_lon, end_lat, end_lon, move_mode):
        cur_route = self.get_route(start_lat, start_lon, end_lat, end_lon, move_mode)
        path = [{'start_lat': el.start_lat, 'start_lon': el.start_lon} for el in cur_route]
        return path
