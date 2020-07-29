import json

default_answers = 'content/answers.json'
menus = 'content/menus.json'
basic = 'content/basics.json'
go_on = ['далее', 'дальше', 'продолжим', "продолжить", "продолжай", "продолжи", "хочу", "хотим", "хотелось", "давай",
         "следующщий", "следом", "след"]
history = 'content/history.json'
facts = 'content/facts.json'
quest = 'content/quest.json'


def get_file(path, key=None):
    with open(path, 'r', encoding='utf-8') as file:
        res = json.loads(file.read())
    return res if not key else res[key]


def give_buttons(*args, **kwargs):
    return [{"title": word, "hide": 'true'} for word in args]


# JSON array schema for menu:
'''
    {
        "header": ...,
        "description": ....
        "input": ...
    }
'''


def make_menu(header, args):
    return {
        "type": "ItemsList",
        "header": {"text": header},
        "items": [{
            "title": item['header'],
            "description": item['description'],
            "button": {
                "text": item['input']
            }
        } for item in args]
    }


def make_image(image_id, description):
    return {
        "type": "BigImage",
        "image_id": image_id,
        "description": description
    }


def matches(tokens, *args):
    if not isinstance(tokens, set):
        tokens = set(tokens)
    args = set(args)
    return len(list(tokens & args)) > 0
