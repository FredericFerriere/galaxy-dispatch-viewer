import data.schedule_item as si

class Schedule:
    def __init__(self):
        self.items = []

    def add_item(self, schedule_item):
        self.items.append(schedule_item)

    def sort(self):
        self.items.sort(key=lambda el:el.start_time)
