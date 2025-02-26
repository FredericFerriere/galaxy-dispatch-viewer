import os

import pandas as pd

import data.agent as agent
import data.location as loc
import data.schedule_item as si

class AgentHolder:

    def __init__(self):
        self.agent_dict = {}

    def load_data(self, model_path):
        self.load_agents(model_path)
        self.load_schedules(model_path)

    def load_agents(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'agents.csv'), sep=';')
        for _, r in df.iterrows():
            ref_loc = loc.Location(r['latitude_start'], r['longitude_start'])
            self.agent_dict[r['agent_id']] = agent.Agent(r['agent_id'], r['agent_type'], r['move_mode'], ref_loc)

    def load_schedules(self, model_path):
        df = pd.read_csv(os.path.join(model_path, 'schedules.csv'), sep=';')
        for _, r in df.iterrows():
            new_it = si.ScheduleItem(r['task_id'], r['start_time'])
            self.agent_dict[r['agent_id']].add_schedule_item(new_it)
        for v in self.agent_dict.values():
            v.sort_schedule()

    def get_agent(self, agent_id):
        return self.agent_dict[agent_id]

