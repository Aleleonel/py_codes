import json


def ler_json():
    with open('aq01.json', 'r', encoding='utf8') as f:
        return json.load(f)


data = ler_json()

print(data)