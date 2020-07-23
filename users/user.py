import json


class User:

    def __init__(self, cross_state):
        if cross_state:
            cross_state = json.loads(cross_state)
            self.name = cross_state['name']
            self.state = cross_state['state']
        else:
            self.name = ''
            self.state = 'auth_begin'

    def build(self):
        return json.dumps({
            "name": self.name,
            "state": self.state
        })
