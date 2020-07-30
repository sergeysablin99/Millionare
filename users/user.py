import json

'''
default cross state
{
    'name': ..
    'state' ..
    achievement: True/False
}
'''

achievements = ["road_to_million", "easy_start", "steady_rise", "thorny_road", "warm_up_is_over",
                "increased_rates", "millionaire", "cleverest", "too_easy", "scoop", "decent_game",
                "reliable_victory", "champion", "serious_sam", "beginner", "druz", "professor",
                "like_a_boss", "so_easy", "lovely_user", "fan"]
# Достижения находятся в content/achievements.json
# Чтобы достать ачивку
'''
from config import achievements, getfile
achievement = getfile(achievements, 'ключ ачивки, например "first"')
'''


class User:

    def __init__(self, cross_state):
        if cross_state:
            cross_state = json.loads(cross_state)
            if 'state' not in cross_state:
                self.state = 'menu'
            else:
                self.state = cross_state['state']
            if 'name' not in cross_state:
                self.name = ''
                self.state = 'auth_begin'
            else:
                self.name = cross_state['name']
            for achievement in achievements:
                if achievement not in cross_state:
                    self.__dict__[achievement] = False
                else:
                    self.__setattr__(achievement, cross_state[achievement])
        else:
            self.name = ''
            self.state = 'auth_begin'

    def build(self):
        res = json.dumps(self.__dict__, ensure_ascii=False)
        return res
