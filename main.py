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
        'response': {
            'text': dialogue.text,
            'end_session': 'false'
        },
        state_key: {"value": user.build()}
    }
    return res
