from datetime import date

v = voluntarios = ['Alexandre', 'Leonardo', 'Eduardo', 'Natanael', 'Renato', 'Ronaldo', 'Ferreira', 'Claudio', 'João','Nelson']
s = som = ['Natanael', 'Eduardo', 'Leonardo', 'Alexandre']
l = leitores = ['Alexandre', 'Leonardo', 'Renato', 'Eduardo', 'Ronaldo']

indicadores = []
volantes = []
opsom = []
leitor = []


try:

    indicadoresaux = []
    cont = 0
    for ind in range(len(v)):
        if ind not in indicadores and cont <= 1:
            indicadores.append(v[ind])
            cont += 1
    futuro = date.fromordinal(737399 + 44)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores} ')

    cont = 0
    for ind2 in v:
        for ind3 in indicadores:
            if v != indicadores and cont <= 1:
                indicadoresaux.append(v)
                cont += 1

    print()
    futuro = date.fromordinal(737399 + 41)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadoresaux}')


except Exception as erro:
    print()
    print('não deu certo', erro)


