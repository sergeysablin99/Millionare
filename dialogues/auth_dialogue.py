from dialogues.base_dialogue import Dialogue


class AuthDialogue(Dialogue):

    def __init__(self, request, user):
        if user.state == 'auth_begin':
            self.text = 'Приветствую. Для начала давайте познакомимся. Как вас зовут?'
            self.tts = self.text
            user.state = 'auth_wait'
        elif user.state == 'auth_wait':
            entities = request['nlu']['entities']
            name = []
            for item in entities:
                if item['type'] == 'YANDEX.FIO':
                    for val in ("last_name", "first_name", "patronymic_name"):
                        if item['value'].get(val):
                            name.append(item['value'].get(val).capitalize())
            if name:
                name = ' '.join(name)
                user.name = name
                user.state = 'auth_check'
                self.text = f'Я правильно поняла, вас зовут: {name}?'
            else:
                self.text = 'Назовите пожалуйста настоящее имя.'
        else:
            intents = request['nlu']['intents']
            if intents.get('YANDEX.CONFIRM'):
                self.text = f'Приятно познакомиться, {user.name}'
                user.state = 'menu'
            elif intents.get('YANDEX.REJECT'):
                self.text = 'Хорошо, давайте попробуем еще раз. Как вас зовут?'
            else:
                self.text = f'Это не похоже ни на согласие, ни на несогласие. Вас зовут {user.name}?'
