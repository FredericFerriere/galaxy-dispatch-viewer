import os

from enum import Enum

import rounds

class ModelType(Enum):
    VAN = 0
    BIKE = 1
    BIKE_BUS = 2

class Model:
    def __init__(self, model_type:ModelType):
        self.model_type = model_type
        self.rounds = rounds.Rounds()

    def load_data(self, model_path):
        self.rounds.load_data(model_path)
