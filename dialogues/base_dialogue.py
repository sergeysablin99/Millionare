from abc import ABC


class Dialogue(ABC):
    text = 'Default'
    tts = 'Default'
    buttons = None
    card = None
    state = 'menu'
    show_menu = False
    ended = False
