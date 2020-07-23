from users.user import User
from dialogues.dialogue_factory import Creator


def handler(event, context):
    cross_state = event['state']['user'].get('value')
    user = User(cross_state)
    if event['session']['new'] and 'auth' not in user.state:
        user.state = 'greet'
    dialogue = Creator.create(user)
    result = dialogue(event['request'], user)
    return form_response(event['version'], event['session'], result, user)


def form_response(version, session, dialogue, user):
    if dialogue.tts == 'Default':
        dialogue.tts = dialogue.text
    res = {
        'version': version,
        'session': session,
        'response': {
            'text': dialogue.text,
            'end_session': 'false'
        },
        "user_state_update": {"value": user.build()}
    }
    return res
