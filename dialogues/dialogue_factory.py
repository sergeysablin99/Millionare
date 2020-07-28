from dialogues.auth_dialogue import AuthDialogue
from dialogues.main_menu import MainMenu


class Creator:

    @staticmethod
    def create(user):
        if 'auth' in user.state:
            return AuthDialogue
        else:
            return MainMenu
