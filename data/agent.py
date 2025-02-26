import data.schedule as sch


class Agent:
    def __init__(self, agent_id, agent_type, move_mode, ref_location):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.move_mode = move_mode
        self.schedule = sch.Schedule()
        self.ref_location = ref_location

    def get_schedule(self):
        return self.schedule

    def add_schedule_item(self, new_it):
        self.schedule.add_item(new_it)

    def sort_schedule(self):
        self.schedule.sort()


