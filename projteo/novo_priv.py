voluntarios = ['José Ferreira', 'Leonardo Verzi', 'Eduardo Ferraz', 'João Melo', 'Natanael Silva', 'Leonardo Santos',
               'Renato Verzi', 'Ronaldo Flores', 'Alexandre Monticelli', 'Claudio Goveia', 'Alexandre Leonel',
               'Nelson Custódio']

leitores = ['Alexandre Leonel', 'Leonardo Verzi', 'Renato Verzi', 'Ronaldo Flores', 'Eduardo Ferraz', 'Nelson Custódio']
som = ['Natanael Silva', 'Eduardo Ferraz', 'Leonardo Verzi', 'Alexandre Leonel']


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

voluntarios_Domingo2 = []
voluntarios_Quinta2 = []
indicadores_quinta2 = []
indicadores_domingo2 = []
volantes_quinta2 = []
volantes_domingo2 = []
som_quinta2 = []
som_domingo2 = []
leitor2 = []

voluntarios_Domingo3 = []
voluntarios_Quinta3 = []
indicadores_quinta3 = []
indicadores_domingo3 = []
volantes_quinta3 = []
volantes_domingo3 = []
som_quinta3 = []
som_domingo3 = []
leitor3 = []

voluntarios_Domingo4 = []
voluntarios_Quinta4 = []
indicadores_quinta4 = []
indicadores_domingo4 = []
volantes_quinta4 = []
volantes_domingo4 = []
som_quinta4 = []
som_domingo4 = []
leitor4 = []

voluntarios_Domingo5 = []
voluntarios_Quinta5 = []
indicadores_quinta5 = []
indicadores_domingo5 = []
volantes_quinta5 = []
volantes_domingo5 = []
som_quinta5 = []
som_domingo5 = []
leitor5 = []


voluntarios_Quinta_segunda_semana = []


# voluntarios da quinta
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
print()
print(voluntarios_Domingo)


# voluntarios do domingo
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
for l in range(len(leitores)):
    # Leitor - Domingo
    if leitores[l] not in indicadores_domingo and leitores[l] not in volantes_domingo and leitores[l] \
            not in som_domingo and cont < 1:
        leitor.append(leitores[l])
        cont += 1

print()
print(f'Indicadores Domingo: {indicadores_domingo}')
print(f'Volantes Domingo: {volantes_domingo}')
print(f'Operadores de som Domingo: {som_domingo}')
print(f'Leitor de A Sentinela: {leitor}')

# checa quem ja participou como voluntária na reunião de Domingo
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
print()
print(voluntarios_Quinta)

# voluntarios da quinta segunda semana
cont = 0
for v in range(len(voluntarios_Quinta)):
    # indicadores de Quinta-Feira segunda semana
    if voluntarios_Quinta[v] not in indicadores_quinta and voluntarios_Quinta[v] not in volantes_quinta \
            and voluntarios_Quinta[v] not in som_quinta and cont <= 1:
        indicadores_quinta2.append(voluntarios_Quinta[v])
        cont += 1

cont = 0
for v in range(len(voluntarios_Quinta)):
    # volantes de  Quinta-Feira segunda semana
    if voluntarios_Quinta[v] not in indicadores_quinta2 and voluntarios_Quinta[v] not in volantes_quinta2 \
            and voluntarios_Quinta[v] not in som_quinta2 and cont <= 1:
        volantes_quinta2.append(voluntarios_Quinta[v])
        cont += 1

cont = 0
for s in range(len(som)):
    # Operadores do Som - Quinta-Feira segunda semana
    if som[s] not in indicadores_quinta2 and som[s] not in volantes_quinta2 and som[s] not in som_quinta2 \
            and som[s] not in som_quinta and som[s] not in som_domingo and cont < 1:
        som_quinta2.append(som[s])
        cont += 1

# imprime todos os voluntários da reunião de quinta segunda semana
print()
print(f'Indicadores Quinta- feira: {indicadores_quinta2}')
print(f'Volantes Quinta- feira: {volantes_quinta2}')
print(f'Operadores de som Quinta- feira: {som_quinta2}')


###
# checa quem ja participou como voluntária na reunião de quinta segunda semana
for v in range(len(voluntarios)):
    if voluntarios[v] not in indicadores_quinta2 and voluntarios[v] not in volantes_quinta2 \
            and voluntarios[v] not in som_quinta2 and voluntarios[v] not in leitores:
        voluntarios_Domingo2.append(voluntarios[v])

for l in range(len(leitores)):
    if leitores[l] not in indicadores_quinta2 and leitores[l] not in volantes_quinta2 \
            and leitores[l] not in som_quinta2 and leitores[l] not in leitor:
        voluntarios_Domingo2.append(leitores[l])

for s in range(len(som)):
    if som[s] not in indicadores_quinta2 and som[s] not in volantes_quinta2 \
            and som[s] not in som_quinta2 and som[s] not in leitor:
        voluntarios_Domingo2.append(som[s])
print()
print(voluntarios_Domingo2)

# voluntarios do domingo segunda semana
cont = 0
for v in range(len(voluntarios_Domingo2)):
    # indicadores de Domingo
    if voluntarios_Domingo2[v] not in indicadores_domingo2 and voluntarios_Domingo2[v] not in volantes_domingo2 \
            and voluntarios_Domingo2[v] not in som_domingo2 and voluntarios_Domingo2[v] not in leitor and cont <= 1:
        indicadores_domingo2.append(voluntarios_Domingo2[v])
        cont += 1

cont = 0
for v in range(len(voluntarios_Domingo2)):
    # volantes de  Domingo
    if voluntarios_Domingo2[v] not in indicadores_domingo2 and voluntarios_Domingo2[v] not in volantes_domingo2 \
            and voluntarios_Domingo2[v] not in som_domingo2 and voluntarios_Domingo2[v] not in leitor and cont <= 1:
        volantes_domingo2.append(voluntarios_Domingo2[v])
        cont += 1

# verifica se tem apenas um volante e acrescenta + 1
for v in range(len(voluntarios_Domingo2)):

    if len(volantes_domingo2) < 2:
        cont = 0
        for ind in range(len(indicadores_quinta2)):
            if indicadores_quinta2[ind] not in volantes_domingo2:
                volantes_domingo2.append(indicadores_quinta)
        cont += 1

cont = 0
for s in range(len(som)):
    # Operadores do Som - Domingo
    if som[s] not in indicadores_domingo2 and som[s] not in volantes_domingo2 and som[s] not in som_domingo2 \
            and som[s] not in som_quinta and cont < 1:
        som_domingo2.append(som[s])
        cont += 1

cont = 0
for l in range(len(leitores)):
    # Leitor - Domingo
    if leitores[l] not in indicadores_domingo2 and leitores[l] not in volantes_domingo2 and leitores[l] \
            not in som_domingo2 and cont < 1:
        leitor2.append(leitores[l])
        cont += 1

print()
print(f'Indicadores Domingo: {indicadores_domingo2}')
print(f'Volantes Domingo: {volantes_domingo2}')
print(f'Operadores de som Domingo: {som_domingo2}')
print(f'Leitor de A Sentinela: {leitor2}')


# checa quem ja participou como voluntária na reunião de Domingo terceira semana
for v in range(len(voluntarios)):
    if voluntarios[v] not in indicadores_domingo2 and voluntarios[v] not in volantes_domingo2 \
            and voluntarios[v] not in som_domingo2 and voluntarios[v] not in leitor2 and voluntarios[v] \
            not in voluntarios_Quinta2:
        voluntarios_Quinta3.append(voluntarios[v])

for l in range(len(leitores)):
    if leitores[l] not in indicadores_domingo2 and leitores[l] not in volantes_domingo2 \
            and leitores[l] not in som_domingo2 and leitores[l] not in leitor2 and voluntarios[v] \
            not in voluntarios_Quinta2:
        voluntarios_Quinta3.append(leitores[l])

for s in range(len(som)):
    if som[s] not in indicadores_domingo2 and som[s] not in volantes_domingo2 \
            and som[s] not in som_domingo2 and som[s] not in leitor2 and voluntarios[v] not in voluntarios_Quinta2:
        voluntarios_Quinta3.append(som[s])
print()
print(voluntarios_Quinta3)

# voluntarios da quinta segunda semana
cont = 0
for v in range(len(voluntarios_Quinta3)):
    # indicadores de Quinta-Feira segunda semana
    if voluntarios_Quinta3[v] not in indicadores_quinta and voluntarios_Quinta3[v] not in indicadores_quinta2 \
            and voluntarios_Quinta3[v] not in indicadores_quinta3 \
            and voluntarios_Quinta3[v] not in volantes_quinta3 and voluntarios_Quinta3[v] not in som_quinta3 \
            and cont <= 1:
        indicadores_quinta3.append(voluntarios_Quinta3[v])
        cont += 1

cont = 0
for v in range(len(voluntarios_Quinta3)):
    # volantes de  Quinta-Feira segunda semana
    if voluntarios_Quinta3[v] not in indicadores_quinta3 and voluntarios_Quinta3[v] not in volantes_quinta3 \
            and voluntarios_Quinta3[v] not in som_quinta3 and cont <= 1:
        volantes_quinta3.append(voluntarios_Quinta3[v])
        cont += 1

cont = 0
for s in range(len(som)):
    # Operadores do Som - Quinta-Feira terceira semana
    if som[s] not in indicadores_quinta3 \
            and som[s] not in volantes_quinta3 \
            and som[s] not in som_quinta \
            and som[s] not in som_domingo \
            and som[s] not in som_quinta2 \
            and som[s] not in som_domingo2 \
            and som[s] not in som_quinta3 \
            and cont < 1:
        som_quinta3.append(som[s])
        cont += 1

# imprime todos os voluntários da reunião de quinta terceira semana
print()
print(f'Indicadores Quinta- feira: {indicadores_quinta3}')
print(f'Volantes Quinta- feira: {volantes_quinta3}')
print(f'Operadores de som Quinta- feira: {som_quinta3}')


###
# checa quem ja participou como voluntária na reunião de quinta terceira semana
for v in range(len(voluntarios)):
    if voluntarios[v] not in indicadores_quinta3 and voluntarios[v] not in volantes_quinta3 \
            and voluntarios[v] not in som_quinta3 and voluntarios[v] not in leitores:
        voluntarios_Domingo3.append(voluntarios[v])

for l in range(len(leitores)):
    if leitores[l] not in indicadores_quinta3 and leitores[l] not in volantes_quinta3 \
            and leitores[l] not in som_quinta3 and leitores[l] not in leitor:
        voluntarios_Domingo3.append(leitores[l])

for s in range(len(som)):
    if som[s] not in indicadores_quinta3 and som[s] not in volantes_quinta3 \
            and som[s] not in som_quinta3 and som[s] not in leitor:
        voluntarios_Domingo3.append(som[s])
print()
print(voluntarios_Domingo3)

# voluntarios do domingo terceira semana
cont = 0
for v in range(len(voluntarios_Domingo3)):
    # indicadores de Domingo
    if voluntarios_Domingo3[v] not in indicadores_domingo3 and voluntarios_Domingo3[v] not in volantes_domingo3 \
            and voluntarios_Domingo3[v] not in som_domingo3 and voluntarios_Domingo3[v] not in leitor and cont <= 1:
        indicadores_domingo3.append(voluntarios_Domingo3[v])
        cont += 1

cont = 0
for v in range(len(voluntarios_Domingo3)):
    # volantes de  Domingo
    if voluntarios_Domingo3[v] not in indicadores_domingo3 and voluntarios_Domingo3[v] not in volantes_domingo3 \
            and voluntarios_Domingo3[v] not in som_domingo3 and voluntarios_Domingo3[v] not in leitor and cont <= 1:
        volantes_domingo3.append(voluntarios_Domingo3[v])
        cont += 1

# verifica se tem apenas um volante e acrescenta + 1
for v in range(len(voluntarios_Domingo3)):

    if len(volantes_domingo3) < 2:
        cont = 0
        for ind in range(len(indicadores_quinta3)):
            if indicadores_quinta3[ind] not in volantes_domingo3:
                volantes_domingo3.append(indicadores_quinta)
        cont += 1

cont = 0
for s in range(len(som)):
    # Operadores do Som - Domingo
    if som[s] not in indicadores_domingo3 and som[s] not in volantes_domingo3 and som[s] not in som_domingo2 \
            and som[s] not in som_domingo3 \
            and som[s] not in som_quinta and cont < 1:
        som_domingo3.append(som[s])
        cont += 1

cont = 0
for l in range(len(leitores)):
    # Leitor - Domingo
    if leitores[l] not in indicadores_domingo3 and leitores[l] not in volantes_domingo3 \
            and leitores[l] not in leitor2 \
            and leitores[l] not in som_domingo3 and cont < 1:
        leitor3.append(leitores[l])
        cont += 1

print()
print(f'Indicadores Domingo: {indicadores_domingo3}')
print(f'Volantes Domingo: {volantes_domingo3}')
print(f'Operadores de som Domingo: {som_domingo3}')
print(f'Leitor de A Sentinela: {leitor3}')


# checa quem ja participou como voluntária na reunião de Domingo terceira semana
for v in range(len(voluntarios)):
    if voluntarios[v] and voluntarios[v] not in indicadores_domingo3 \
            and voluntarios[v] not in volantes_domingo3 \
            and voluntarios[v] not in som_domingo3 \
            and voluntarios[v] not in leitor3 and voluntarios[v] \
            not in voluntarios_Quinta4:
        voluntarios_Quinta4.append(voluntarios[v])

for l in range(len(leitores)):
    if leitores[l] and leitores[l] not in indicadores_domingo3\
            and leitores[l] not in volantes_domingo3 \
            and leitores[l] not in som_domingo3 \
            and leitores[l] not in leitor3 and voluntarios[v] \
            not in voluntarios_Quinta3:
        voluntarios_Quinta4.append(leitores[l])

for s in range(len(som)):
    if som[s] not in indicadores_domingo3 and som[s] not in volantes_domingo3 \
            and som[s] not in som_domingo3 and som[s] not in leitor3 and voluntarios[v] not in voluntarios_Quinta3:
        voluntarios_Quinta4.append(som[s])
print()
print(voluntarios_Quinta4)

# voluntarios da quinta segunda semana
cont = 0
for v in range(len(voluntarios_Quinta4)):
    # indicadores de Quinta-Feira segunda semana
    if voluntarios_Quinta4[v] not in indicadores_quinta2 \
            and voluntarios_Quinta4[v] not in indicadores_quinta3 \
            and voluntarios_Quinta4[v] not in indicadores_quinta4 \
            and voluntarios_Quinta4[v] not in volantes_quinta4 \
            and voluntarios_Quinta3[v] not in som_quinta4 \
            and cont <= 1:
        indicadores_quinta4.append(voluntarios_Quinta4[v])
        cont += 1

cont = 0
for v in range(len(voluntarios_Quinta4)):
    # volantes de  Quinta-Feira segunda semana
    if voluntarios_Quinta4[v] not in indicadores_quinta4 \
            and voluntarios_Quinta4[v] not in volantes_quinta4 \
            and voluntarios_Quinta4[v] not in som_quinta4 and cont <= 1:
        volantes_quinta4.append(voluntarios_Quinta4[v])
        cont += 1

cont = 0
for s in range(len(som)):
    # Operadores do Som - Quinta-Feira terceira semana
    if som[s] not in indicadores_quinta4 \
            and som[s] not in volantes_quinta4 \
            and som[s] not in som_quinta2 \
            and som[s] not in som_domingo2 \
            and som[s] not in som_quinta3 \
            and som[s] not in som_domingo3 \
            and som[s] not in som_quinta4 \
            and cont < 1:
        som_quinta4.append(som[s])
        cont += 1

# imprime todos os voluntários da reunião de quinta quarta semana
print()
print(f'Indicadores Quinta- feira: {indicadores_quinta4}')
print(f'Volantes Quinta- feira: {volantes_quinta4}')
print(f'Operadores de som Quinta- feira: {som_quinta4}')


###
# checa quem ja participou como voluntária na reunião de quinta terceira semana
for v in range(len(voluntarios)):
    if voluntarios[v] not in indicadores_quinta4 and voluntarios[v] not in volantes_quinta4 \
            and voluntarios[v] not in som_quinta4 and voluntarios[v] not in leitores:
        voluntarios_Domingo4.append(voluntarios[v])

for l in range(len(leitores)):
    if leitores[l] not in indicadores_quinta4 and leitores[l] not in volantes_quinta4 \
            and leitores[l] not in som_quinta4 and leitores[l] not in leitor3:
        voluntarios_Domingo4.append(leitores[l])

for s in range(len(som)):
    if som[s] not in indicadores_quinta4 and som[s] not in volantes_quinta4 \
            and som[s] not in som_quinta4 and som[s] not in leitor3:
        voluntarios_Domingo4.append(som[s])
print()
print(voluntarios_Domingo5)