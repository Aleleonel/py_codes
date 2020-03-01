voluntarios = ['José Ferreira', 'Leonardo Verzi', 'Eduardo Ferraz', 'João Melo', 'Natanael Silva', 'Leonardo Santos',
               'Renato Verzi', 'Ronaldo Flores', 'Alexandre Monticelli', 'Claudio Goveia', 'Alexandre Leonel',
               'Nelson Custódio']

leitores = ['Alexandre Leonel', 'Leonardo Verzi', 'Renato Verzi', 'Ronaldo Flores', 'Eduardo Ferraz', 'Nelson Custódio']
som = ['Natanael Silva', 'Eduardo Ferraz', 'Leonardo Verzi']


# cont = 0
# for counter, value in enumerate(voluntarios):
#     print(counter, value)

cont = 0

voluntarios_Domingo = []
voluntarios_Quinta = []
indicadores_quinta = []
indicadores_domingo = []
volantes_quinta = []
volantes_domingo = []
som_quinta = []
som_domingo = []
leitor = []


def checa_Quinta():
    """
    checa quem ja participou como voluntária na reunião de Quinta
    :return:
    voluntarios_Domingo - lista dos voluntarios que participarão da Reunião de Domingo
    :return:
    """
    # checa quem ja participou como voluntária na reunião de quinta
    for v in range(len(voluntarios)):
        if voluntarios[v] not in indicadores_quinta and voluntarios[v] not in volantes_quinta \
                and voluntarios[v] not in som_quinta and voluntarios[v] not in leitores:
            voluntarios_Domingo.append(voluntarios[v])

    for l in range(len(leitores)):
        if leitores[l] not in indicadores_quinta and leitores[l] not in volantes_quinta \
                and leitores[l] not in som_quinta and leitores[l] not in leitor:
            voluntarios_Domingo.append(leitores[l])

    for s in range(len(som)):
        if som[s] not in indicadores_quinta and som[s] not in volantes_quinta \
                and som[s] not in som_quinta and som[s] not in leitor:
            voluntarios_Domingo.append(som[s])
    # print()
    # print(voluntarios_Domingo)

    return voluntarios_Domingo


def checa_domingo():
    """
    checa quem ja participou como voluntária na reunião de Domingo
    :return:
    voluntarios_Quinta - lista dos voluntarios que participarão da Reunião de  Quinta
    """
    #
    for v in range(len(voluntarios)):
        if voluntarios[v] not in indicadores_domingo and voluntarios[v] not in volantes_domingo \
                and voluntarios[v] not in som_domingo and voluntarios[v] not in leitor and voluntarios[v] \
                not in voluntarios_Quinta:
            voluntarios_Quinta.append(voluntarios[v])

    for l in range(len(leitores)):
        if leitores[l] not in indicadores_domingo and leitores[l] not in volantes_domingo \
                and leitores[l] not in som_domingo and leitores[l] not in leitor and voluntarios[v] \
                not in voluntarios_Quinta:
            voluntarios_Quinta.append(leitores[l])

    for s in range(len(som)):
        if som[s] not in indicadores_domingo and som[s] not in volantes_domingo \
                and som[s] not in som_domingo and som[s] not in leitor and voluntarios[v] not in voluntarios_Quinta:
            voluntarios_Quinta.append(som[s])
    # print()
    # print(voluntarios_Quinta)

    return voluntarios_Quinta


def volun_quinta():

    cont = 0
    for v in range(len(voluntarios)):
        # indicadores de Quinta-Feira
        if voluntarios[v] not in indicadores_quinta and voluntarios[v] not in volantes_quinta and voluntarios[v] \
                not in som_quinta and cont <= 1:
            indicadores_quinta.append(voluntarios[v])
            cont += 1

    cont = 0
    for v in range(len(voluntarios)):
        # volantes de  Quinta-Feira
        if voluntarios[v] not in indicadores_quinta and voluntarios[v] not in volantes_quinta and voluntarios[v] \
                not in som_quinta and cont <= 1:
            volantes_quinta.append(voluntarios[v])
            cont += 1

    cont = 0
    for s in range(len(som)):
        # Operadores do Som - Quinta-Feira
        if som[s] not in indicadores_quinta and som[s] not in volantes_quinta and som[s] not in som_quinta and cont < 1:
            som_quinta.append(som[s])
            cont += 1

    # imprime todos os voluntários da reunião de quinta primeira semana
    print()
    print(f'Indicadores Quinta- feira: {indicadores_quinta}')
    print(f'Volantes Quinta- feira: {volantes_quinta}')
    print(f'Operadores de som Quinta- feira: {som_quinta}')


def volun_domingo():
    cont = 0
    for v in range(len(voluntarios_Domingo)):
        # indicadores de Domingo
        if voluntarios_Domingo[v] not in indicadores_domingo and voluntarios_Domingo[v] not in volantes_domingo \
                and voluntarios_Domingo[v] not in som_domingo and voluntarios_Domingo[v] not in leitor and cont <= 1:
            indicadores_domingo.append(voluntarios_Domingo[v])
            cont += 1

    cont = 0
    for v in range(len(voluntarios_Domingo)):
        # volantes de  Domingo
        if voluntarios_Domingo[v] not in indicadores_domingo and voluntarios_Domingo[v] not in volantes_domingo \
                and voluntarios_Domingo[v] not in som_domingo and voluntarios_Domingo[v] not in leitor and cont <= 1:
            volantes_domingo.append(voluntarios_Domingo[v])
            cont += 1

    # verifica se tem apenas um volante e acrescenta + 1
    for v in range(len(voluntarios_Domingo)):
        if len(volantes_domingo) < 2:
            cont = 0
            for ind in range(len(indicadores_quinta)):
                if indicadores_quinta[ind] not in volantes_domingo:
                    volantes_domingo.append(indicadores_quinta)
            cont += 1

    cont = 0
    for s in range(len(som)):
        # Operadores do Som - Domingo
        if som[s] not in indicadores_domingo and som[s] not in volantes_domingo and som[s] not in som_domingo \
                and som[s] not in som_quinta and cont < 1:
            som_domingo.append(som[s])
            cont += 1

    cont = 0
    for l in range(len(leitores)):
        # Leitor - Domingo
        if leitores[l] not in indicadores_domingo and leitores[l] not in volantes_domingo and leitores[l] \
                not in som_domingo and cont < 1:
            leitor.append(leitores[l])
            cont += 1

    # imprime todos os voluntários da reunião de Domingo Primeira semana
    print()
    print(f'Indicadores Domingo: {indicadores_domingo}')
    print(f'Volantes Domingo: {volantes_domingo}')
    print(f'Operadores de som Domingo: {som_domingo}')
    print(f'Leitor de A Sentinela: {leitor}')


volun_quinta()
checa_Quinta()

volun_domingo()
checa_domingo()

volun_quinta()
checa_domingo()

volun_domingo()
checa_Quinta()



