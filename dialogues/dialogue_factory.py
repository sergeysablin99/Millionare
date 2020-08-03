from dialogues.auth_dialogue import AuthDialogue
from dialogues.main_menu import MainMenu
from dialogues.game import Game


class Creator:

    @staticmethod
    def create(user):
        if 'auth' in user.state:
            return AuthDialogue
        if 'game' in user.state:
            return Game
        else:
            return MainMenu
