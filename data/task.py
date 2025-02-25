from enum import Enum

import data.location as l


class TaskType(Enum):
    GENERIC = 0
    COLLECTION = 1
    LOCAL_ROUND = 2
    IMPORTED_ROUND = 3
    RETURN_TRAILER = 4
    RECEIVE_TRAILER = 5
    SEND_TRAILER = 6
    STORE_TRAILER = 7
    ROUTE_TRAILER = 8
    TRANSITION_RIDE = 9
    RETURN_STORE_TRAILER = 10

class Task:

    def __init__(self, task_id, start_location: l.Location, end_location: l.Location, agent_id):
        self.id = task_id
        self.start_location = start_location
        self.end_location = end_location
        self.agent_id = agent_id
        self.duration = 0
        self.distance = 0



class Collection(Task):
    """
    Description:
    Who: zone A delivery man
    Warehouse location: zone A
    Target delivery: zone B
    A task the delivery person in zone A has to perform so that the delivery person in zone B can deliver
    to zone B clients goods located in a zone A warehouse
    The delivery person starts at client warehouse location (zone A) with an empty trailer
    he loads merchandise into the trailer, then rides to the nearest bus stop and loads bike trailer into bus trailer
    """

    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.distance = 0
        self.parcel_loading_duration = 0
        self.riding_duration = 0
        self.bus_loading_duration = 0
        self.duration = self.parcel_loading_duration + self.riding_duration + self.bus_loading_duration


class LocalRound(Task):

    def __init__(self, task_id, start_location, end_location, delivery_round_id, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.delivery_round_id = delivery_round_id
        self.distance = 0
        self.parcel_loading_duration = 0
        self.round_duration = 0
        self.duration = self.parcel_loading_duration + self.round_duration


class ImportedRound(Task):

    def __init__(self, task_id, start_location, end_location, delivery_round_id, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)

        self.delivery_round_id = delivery_round_id
        self.distance = 0
        self.bus_unloading_duration = 0
        self.round_duration = 0
        self.duration = self.bus_unloading_duration + self.round_duration


class ReturnTrailer(Task):

    def __init__(self, task_id, start_location, agent_id):
        super().__init__(task_id, start_location, start_location, agent_id)
        self.distance = 0
        self.duration = 0


class ReceiveTrailer(Task):

    def __init__(self, task_id, start_location, agent_id):
        super().__init__(task_id, start_location, start_location, agent_id)
        self.distance = 0
        self.duration = 0


class SendTrailer(Task):

    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.distance = 0
        self.riding_duration = 0
        self.bus_loading_duration = 0
        self.duration = self.riding_duration + self.bus_loading_duration


class StoreTrailer(Task):
    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.distance = 0
        self.bus_unloading_duration = 0
        self.riding_duration = 0
        self.duration = self.bus_unloading_duration + self.riding_duration


class RouteTrailer(Task):

    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)

        self.distance = 0
        self.bus_unloading_duration = 0
        self.riding_duration = 0
        self.wait_duration = 0
        self.bus_loading_duration = 0
        self.duration = 0


class ReturnStoreTrailer(Task):

    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.distance = 0
        self.duration = 0


class TransitionRide(Task):
    def __init__(self, task_id, start_location, end_location, agent_id):
        super().__init__(task_id, start_location, end_location, agent_id)
        self.distance = 0
        self.duration = 0

