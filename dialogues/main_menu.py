from dialogues.base_dialogue import Dialogue


class MainMenu(Dialogue):

    def __init__(self, request, user):
        self.text = f'Приветствую вас, {user.name}. Вы в меню. Больше я ничего не умею'
        self.tts = self.text
