from dialogues.base_dialogue import Dialogue


class MainMenu(Dialogue):

    def __init__(self, request, user):
        self.text = 'Текст главного меню'
        self.tts = self.text
        self.card = {
            "type": "ItemsList",
            "header": {
                "text": "Моя прекрасная галерея",
            },
            "items": [
                {
                    "image_id": "1030494/48a8d971e1001286fdcc",
                    "title": "Ты не пройдешь!",
                    "description": "Точно не пройдешь",
                    "button": {
                        "text": "Попробовать пройти",
                        "url": "http://google.com",
                        "payload": {}
                    }
                },
                {
                    "image_id": "1030494/274ba5413144f7607711",
                    "title": "Таехник соблазнения",
                    "description": "Научись соблазну вместе с Хатаке Какаши!",
                    "button": {
                        "text": "Попробовать бесплатно",
                        "url": "http://google.com",
                        "payload": {}
                    }
                }
            ],
            "footer": {
                "text": "Текст блока под изображением.",
                "button": {
                    "text": "Надпись на кнопке",
                    "url": "https://example.com/",
                    "payload": {}
                }
            }
        }
        self.buttons = [
            {
                "title": "Надпись на кнопке",
                "payload": {},
                "url": "https://google.com/",
                "hide": 'true'
            }
        ]
        self.answer = {
            'text': self.text,
            'tts': self.tts,
            'card': self.card,
            'buttons': self.buttons,
            }
