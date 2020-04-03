import json


def format_json(content):
    return json.dumps(content, sort_keys=True, indent=4, separators=(', ', ': '))