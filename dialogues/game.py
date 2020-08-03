from config import questions_path, get_file, make_menu, game_path
from dialogues.base_dialogue import Dialogue


class Game(Dialogue):

    def check_answer(self, tokens, num):
        return len(set(get_file(questions_path[self.define_level(num)])[num]) & tokens) > 0

    def __init__(self, request, user):
        tokens = set(request['nlu']['tokens'])
        if user.__dict__.get('game', {}):
            user.game = {
                'question': 1,
                'past_question': 0,
                "past_questions": {}
            }
        else:
            num = user.game['question']
            if self.check_answer(tokens, num):
                user.game['question'] += 1
                user['past_questions'].add(num)
            else:
                self.text = 'К сожалению, ваш ответ оказался неверным'
                user.state = 'menu'
                user.game = {}
        question = self.give_question(user.game)
        self.text = question['text']
        self.tts = question['tts']

    @staticmethod
    def define_level(num):
        if 1 <= num <= 5:
            return 'easy'
        if 6 <= num <= 10:
            return 'medium'
        return 'hard'

    def give_question(self, game_stat):
        num, past_questions = game_stat['question'], game_stat['past_questions']
        from random import randint
        questions = get_file(questions_path[self.define_level(num)], 'questions')
        question = randint(0, len(questions))
        while question in past_questions:
            question = randint(0, len(questions))
        game_stat['past_question'] = question
        return questions[question]
