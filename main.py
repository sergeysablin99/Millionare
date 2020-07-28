from users.user import User
from dialogues.dialogue_factory import Creator


def handler(event, context):
    if event['state'].get('user'):
        cross_state = event['state']['user'].get('value')
        state_key = 'user_state_update'
    else:
        cross_state = event['state']['session'].get('value')
        state_key = 'session_state'
    user = User(cross_state)
    if event['session']['new'] and 'auth' not in user.state:
        user.state = 'greet'
    dialogue = Creator.create(user)
    result = dialogue(event['request'], user)
    return form_response(event['version'], event['session'], result, user, state_key)


def form_response(version, session, dialogue, user, state_key):
    if dialogue.tts == 'Default':
        dialogue.tts = dialogue.text
    res = {
        'version': version,
        'session': session,
        'end_session': 'false',
        "response": {
            "text": dialogue.text,
            "tts": dialogue.text,
            "card": {
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
                        "title": "Техника соблазнения",
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
            },
            "buttons": [
                {
                    "title": "Надпись на кнопке",
                    "payload": {},
                    "url": "https://google.com/",
                    "hide": 'true'
                }
            ],
            "end_session": 'false'
        },
        state_key: {"value": user.build()}
    }
    return res


