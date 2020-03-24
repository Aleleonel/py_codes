import json

"""criei uma lista com nomes e um dicionario vazio, faço um for na minha lista e preencho meu dicionario
    depois eu crio um arquivo json para armazenar esses dados
"""

voluntarios = ['Alexandre', 'Flavio', 'Marcos', 'Leandro', 'Adalberto', 'Paulo Cesar']
quinta = {}

for vol in range(len(voluntarios)):
    quinta['indicador1'] = voluntarios[0]
    quinta['indicador2'] = voluntarios[1]
    quinta['volantes1'] = voluntarios[2]
    quinta['volantes2'] = voluntarios[3]
    quinta['som'] = voluntarios[4]

print(quinta)


def escrever_json(arq01):
    with open('aq01.json', 'w', encoding='utf8') as f:
        json.dump(arq01, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


escrever_json(quinta)