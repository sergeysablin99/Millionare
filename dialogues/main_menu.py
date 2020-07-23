from dialogues.base_dialogue import Dialogue


class MainMenu(Dialogue):

    def __init__(self, *args, **kwargs):
        self.text = 'Привет. Ты в меню. Больше я ничего не умею'
        self.tts = self.text
