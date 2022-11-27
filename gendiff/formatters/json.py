import json


def format_json(dictionary):
    return json.dumps(dictionary, indent=4) + '\n'
