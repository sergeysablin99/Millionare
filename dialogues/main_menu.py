from dialogues.base_dialogue import Dialogue
from config import give_buttons, make_menu, get_file, menus


class MainMenu(Dialogue):

    def __init__(self, request, user):
        self.text = 'Вы в главном меню. Желаете сыграть, посмотреть достижения или ознакомиться с рейтингом игроков?'
        self.tts = self.text
        self.card = get_file(menus, 'main_menu')
        self.card = make_menu(self.card['title'], self.card['content'])
        self.buttons = give_buttons("Надпись на кнопке", "Надпись 2")
