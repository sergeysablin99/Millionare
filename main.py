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
    if event['request']['nlu']['intents'].get('GAME'):
        user.state = 'game'
    dialogue = Creator.create(user)
    result = dialogue(event['request'], user)
    return form_response(event['version'], event['session'], result, user, state_key)


def form_response(version, session, dialogue, user, state_key):
    if dialogue.tts == 'Default':
        dialogue.tts = dialogue.text
    response = {
        'text': dialogue.text,
        "tts": dialogue.tts
    }
    if dialogue.card:
        response['card'] = dialogue.card
    if dialogue.buttons:
        response['buttons'] = dialogue.buttons
    res = {
        'version': version,
        'session': session,
        'response': response,
        state_key: {"value": user.build()}
    }
    return res
