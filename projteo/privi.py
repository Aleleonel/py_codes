from datetime import date, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment


workbook = Workbook()
sheet = workbook.active

hj = (date.today())
# date_now = datetime.now()
# if hj == date_now:
#     hj = date_now - datetime.timedelta(days=1)
futuro = date.fromordinal(737399+13)
print(hj)

# listas contendo os nomes e dos voluntarios
voluntarios = ['José Ferreira', 'Leonardo Verzi', 'Eduardo Ferraz', 'João Melo', 'Natanael Silva', 'Leonardo Santos',
               'Renato Verzi', 'Ronaldo Flores', 'Alexandre Monticelli', 'Claudio Goveia', 'Alexandre Leonel']

# apenas alguns irmão podem participar dos dois privilégios
som = ['Natanael Silva', 'Eduardo Ferraz', 'Leonardo Verzi', 'Alexandre Leonel']

# listas vazias para guardar os voluntarios de cada função
# Alguns serviços estão fixos para eu poder garantir que não se repitam a cada interação
indicadores = []
volantes = []
opsom = ['Leonardo Verzi']

indicadores2 = []
volantes2 = []
opsom2 = ['Natanael Silva']
leitor1 = ['Eduardo Ferraz']

indicadores3 = []
volantes3 = []
opsom3 = ['Alexandre Leonel']

indicadores4 = []
volantes4 = []
opsom4 = ['Eduardo Ferraz']
leitor2 = ['Alexandre Monticelli']

indicadores5 = []
volantes5 = []
opsom5 = ['Leonardo Verzi']
leitor3 = ['Ronaldo Flores']

indicadores6 = []
volantes6 = []
opsom6 = ['Natanael Silva']

indicadores7 = []
volantes7 = []
opsom7 = ['Alexandre Leonel']
leitor4 = ['Renato Verzi']

indicadores8 = []
volantes8 = []
opsom8 = ['Eduardo Ferraz']

indicadores9 = []
volantes9 = []
opsom9 = ['Leonardo Verzi']
leitor6 = ['Nelson Custódio']

indicadores10 = []
volantes10 = []
opsom10 = ['Natanael Silva']
leitor8 = ['Alexandre Leonel']

indicadores11 = []
volantes11 = []
opsom11 = ['Alexandre Leonel']
leitor9 = ['Leonardo Verzi']

indicadores12 = []
volantes12 = []
opsom12 = ['Eduardo Ferraz']
leitor10 = ['Ronaldo ']

indicadores13 = []
volantes13 = []
opsom13 = ['Leonardo Verzi']
leitor11 = ['Nelson Custódio']

indicadores14 = []
volantes14 = []
opsom14 = ['Natanael Silva']
leitor12 = ['Renato Verzi']


# criei uma função que verifica do dia da semana e calcula o numero para poder gerar cada dia refernte ao dia da semna
def priv():
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

    if hj.weekday() == 0: # segunda-feira #
        quinta1 = date.fromordinal(hj.toordinal() + 3)
        ordinario_number = quinta1.toordinal()
        domingo1 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo1.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

    elif hj.weekday() == 1: # terça-feira #
        quinta1 = date.fromordinal(hj.toordinal() + 2)
        ordinario_number = quinta1.toordinal()
        domingo1 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo1.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

    elif hj.weekday() == 2: # quarta-feira #
        quinta1 = date.fromordinal(hj.toordinal() + 1)
        ordinario_number = quinta1.toordinal()
        domingo1 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo1.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta7.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

    elif hj.weekday() == 3: # quinta-feira #

        quinta1 = date.fromordinal(hj.toordinal())
        ordinario_number = quinta1.toordinal()

        domingo1 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo1.toordinal()

        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()

        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para o próximo Domingo dia: {domingo1}')

    elif hj.weekday() == 4: # sexta-feita #
        domingo1 = date.fromordinal(hj.toordinal() + 2)
        ordinario_number = domingo1.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para o próximo Domingo dia: {domingo1}')

    elif hj.weekday() == 5: # sábado #
        domingo1 = date.fromordinal(hj.toordinal() + 1)
        ordinario_number = domingo1.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo2 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo2.toordinal()
        quinta3 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta3.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'A data será gerada para o próximo Domingo dia: {domingo1}')

    elif hj.weekday() == 6:  # domingo #
        quinta1 = date.fromordinal(hj.toordinal() + 4)
        ordinario_number = quinta1.toordinal()
        domingo2 = date.fromordinal(hj.toordinal())
        ordinario_number = domingo2.toordinal()
        quinta2 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta2.toordinal()
        domingo3 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo3.toordinal()
        quinta4 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta4.toordinal()
        domingo4 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo4.toordinal()
        quinta5 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta5.toordinal()
        domingo5 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo5.toordinal()
        quinta6 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta6.toordinal()
        domingo6 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo6.toordinal()
        quinta7 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta7.toordinal()
        domingo7 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo7.toordinal()
        quinta8 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta8.toordinal()
        domingo8 = date.fromordinal(ordinario_number + 3)

        ordinario_number = domingo8.toordinal()
        quinta9 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta9.toordinal()
        domingo9 = date.fromordinal(ordinario_number + 3)
        ordinario_number = domingo9.toordinal()
        quinta10 = date.fromordinal(ordinario_number + 4)
        ordinario_number = quinta10.toordinal()
        domingo10 = date.fromordinal(ordinario_number + 3)

        print("Hoje é", dias[hj.weekday()])
        print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta2}')

    # verifico a lista de voluntarios e adiciono na lista vazia aquele que ainda não trabalhou na reunião anterior
    cont = 0
    for ind1 in voluntarios:
        if ind1 not in opsom and ind1 not in indicadores and cont <= 1:
            indicadores.append(ind1)
            cont += 1

    cont = 0
    for ind1 in voluntarios:
        if ind1 not in som and ind1 not in indicadores and cont <= 1:
            volantes.append(ind1)
            cont += 1

    cont = 0
    for ind2 in voluntarios:
        if ind2 not in opsom2 and ind2 not in indicadores and ind2 not in volantes and ind2 not in leitor2 and cont <= 1:
            indicadores2.append(ind2)
            cont += 1

    cont = 0
    for ind2 in voluntarios:
        if ind2 not in opsom2 and ind2 not in leitor1 and ind2 not in indicadores2 and ind2 not in indicadores and ind2 not in volantes and cont <= 1:
            volantes2.append(ind2)
            cont += 1

    # imprimo na tela
    print()
    futuro = quinta1
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores} Volantes: {volantes} Som: {opsom}')
    futuro = domingo1
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores2} Volantes: {volantes2} Som: {opsom2} Leitor: {leitor1}')


    # configuro as celulas do excel e insiro os dados em da sheet
    center_aligned_text = Alignment(horizontal="center")
    bold_font = Font(bold=True)
    sheet["A1"] = str(quinta2)
    sheet["A1"].alignment = center_aligned_text
    sheet["A1"].font = bold_font
    sheet["A2"] = str(quinta2)

    sheet["B1"] = "Indicadores:"
    sheet["B1"].alignment = center_aligned_text
    sheet["B1"].font = bold_font
    sheet["B2"] = str(indicadores)

    sheet["C1"] = "Volantes:"
    sheet["C1"].alignment = center_aligned_text
    sheet["C1"].font = bold_font
    sheet["C2"] = str(volantes)

    sheet["D1"] = "Som:"
    sheet["D1"].alignment = center_aligned_text
    sheet["D1"].font = bold_font
    sheet["D2"] = str(opsom)

    # sheet["A3"] = str(domingo1)
    sheet["B3"] = str(indicadores2)
    sheet["C3"] = str(volantes2)
    sheet["D3"] = str(opsom2)
    sheet["E1"] = "Leitor:"
    sheet["E1"].alignment = center_aligned_text
    sheet["E1"].font = bold_font
    sheet["E3"] = str(leitor1)

    cont = 0
    for ind3 in voluntarios:
        if ind3 not in opsom3 and ind3 not in indicadores2 and ind3 not in indicadores and ind3 and ind3 not in volantes3 and cont <= 1:
            indicadores3.append(ind3)
            cont += 1

    cont = 0
    for ind3 in voluntarios:
        if ind3 not in opsom3 and ind3 not in indicadores3 and ind3 not in volantes2 and cont <= 1:
            volantes3.append(ind3)
            cont += 1

    cont = 0
    for ind4 in voluntarios:
        if ind4 not in leitor2 and ind4 not in opsom4 and ind4 not in indicadores3 and cont <= 1:
            indicadores4.append(ind4)
            cont += 1

    cont = 0
    for ind4 in voluntarios:
        if ind4 not in opsom4 and ind4 not in leitor2 and ind4 not in indicadores4 and ind4 not in \
                volantes3 and cont <= 1:
            volantes4.append(ind4)
            cont += 1

    print()
    futuro = quinta2
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores3} Volantes: {volantes3} Som: {opsom3}')
    futuro = domingo2
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores4} Volantes: {volantes4} Som: {opsom4} Leitor: {leitor2}')

    sheet["A4"] = str(quinta2)
    sheet["B4"] = str(indicadores3)
    sheet["C4"] = str(volantes3)
    sheet["D4"] = str(opsom3)

    sheet["A5"] = str(domingo2)
    sheet["B5"] = str(indicadores4)
    sheet["C5"] = str(volantes4)
    sheet["D5"] = str(opsom4)
    sheet["E5"] = str(leitor2)

    cont = 0
    for ind5 in voluntarios:
        if ind5 not in opsom5 and ind5 not in indicadores4 and cont <= 1:
            indicadores5.append(ind5)
            cont += 1

    cont = 0
    for ind5 in voluntarios:
        if ind5 not in opsom5 and ind5 not in indicadores5 and ind5 not in volantes4 and cont <= 1:
            volantes5.append(ind5)
            cont += 1

    cont = 0
    for ind6 in voluntarios:
        if ind6 not in opsom6 and ind6 not in indicadores5 and ind6 not in indicadores4 and ind6 not in leitor3 and cont <= 1:
            indicadores6.append(ind6)
            cont += 1

    cont = 0
    for ind6 in voluntarios:
        if ind6 not in opsom6 and ind6 not in leitor3 and ind6 not in indicadores6 and ind6 not in indicadores5 and cont <= 1:
            volantes6.append(ind6)
            cont += 1

    print()
    futuro = quinta3
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores5} Volantes: {volantes5} Som: {opsom5}')
    futuro = domingo3
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores6} Volantes: {volantes6} Som: {opsom6} Leitor: {leitor3}')

    # sheet["A6"] = str(quinta3)
    sheet["B6"] = str(indicadores5)
    sheet["C6"] = str(volantes5)
    sheet["D6"] = str(opsom5)

    sheet["A7"] = str(domingo3)
    sheet["B7"] = str(indicadores6)
    sheet["C7"] = str(volantes6)
    sheet["D7"] = str(opsom6)
    sheet["E7"] = str(leitor3)

    cont = 0
    for ind7 in voluntarios:
        if ind7 not in opsom7 and ind7 not in indicadores6 and ind7 not in indicadores5 and ind7 not in indicadores4 and cont <= 1:
            indicadores7.append(ind7)
            cont += 1
    cont = 0
    for ind7 in voluntarios:
        if ind7 not in opsom7 and ind7 not in indicadores7 and cont <= 1:
            volantes7.append(ind7)
            cont += 1

    cont = 0
    for ind8 in voluntarios:
        if ind8 not in opsom8 and ind8 not in leitor4 and cont <= 1:
            indicadores8.append(ind8)
            cont += 1

    cont = 0
    for ind8 in voluntarios:
        if ind8 not in opsom8 and ind8 not in leitor4 and ind8 not in indicadores8 and ind8 not in indicadores7 and cont <= 1:
            volantes8.append(ind8)
            cont += 1

    print()
    futuro = quinta4
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores7} Volantes: {volantes7} Som: {opsom7}')
    futuro = domingo4
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores8} Volantes: {volantes8} Som: {opsom8} Leitor: {leitor4}')

    sheet["A8"] = str(quinta4)
    sheet["B8"] = str(indicadores7)
    sheet["C8"] = str(volantes7)
    sheet["D8"] = str(opsom7)

    sheet["A9"] = str(domingo4)
    sheet["B9"] = str(indicadores8)
    sheet["C9"] = str(volantes8)
    sheet["D9"] = str(opsom8)
    sheet["E9"] = str(leitor4)

    cont = 0
    for ind9 in voluntarios:
        if ind9 not in opsom9 and ind9 not in indicadores8 and cont <= 1:
            indicadores9.append(ind9)
            cont += 1

    cont = 0
    for ind9 in voluntarios:
        if ind9 not in opsom9 and ind9 not in indicadores9 and ind9 not in indicadores8 and cont <= 1:
            volantes9.append(ind9)
            cont += 1

    cont = 0
    for ind10 in voluntarios:
        if ind10 not in opsom10 and ind10 not in indicadores9 and ind10 not in indicadores8 and ind10 not in volantes9 and cont <= 1:
            indicadores10.append(ind10)
            cont += 1

    cont = 0
    for ind10 in voluntarios:
        if ind10 not in opsom10 and ind10 not in indicadores9 and ind10 not in indicadores10 and ind10 not in volantes9 and cont <= 1:
            volantes10.append(ind10)
            cont += 1

    print()
    futuro = quinta5
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores9} Volantes: {volantes9} Som: {opsom9}')
    futuro = domingo5
    print(
        f'{futuro} - Reunião Domingo - Indicadores: {indicadores10} Volantes: {volantes10} '
        f'Som: {opsom10} Leitor: {leitor6}'
    )

    sheet["A10"] = str(quinta5)
    sheet["B10"] = str(indicadores9)
    sheet["C10"] = str(volantes9)
    sheet["D10"] = str(opsom9)

    sheet["A11"] = str(domingo5)
    sheet["B11"] = str(indicadores10)
    sheet["C11"] = str(volantes10)
    sheet["D11"] = str(opsom10)
    sheet["E11"] = str(leitor6)

    cont = 0
    for ind11 in voluntarios:
        if ind11 not in opsom10 and ind11 not in indicadores10 and cont <= 1:
            indicadores11.append(ind11)
            cont += 1

    cont = 0
    for ind11 in voluntarios:
        if ind11 not in opsom11 and ind11 not in indicadores10 and ind11 not in indicadores11 and cont <= 1:
            volantes11.append(ind11)
            cont += 1

    cont = 0
    for ind11 in voluntarios:
        if ind11 not in opsom11 and ind11 not in indicadores10 and ind11 not in indicadores11 \
                and ind11 not in volantes11 and cont <= 1:
            indicadores12.append(ind11)
            cont += 1

    cont = 0
    for ind11 in voluntarios:
        if ind11 not in opsom11 and ind11 not in indicadores11 and ind11 not in indicadores12 \
                and ind11 not in volantes11 and cont <= 1:
            volantes12.append(ind11)
            cont += 1

    print()
    print()
    futuro = quinta6
    print(
        f'{futuro} - Reunião Quinta -- Indicadores: {indicadores11} '
        f'Volantes: {volantes11} Som: {opsom11}'
    )
    futuro = domingo6
    print(
        f'{futuro} - Reunião Domingo - Indicadores: {indicadores12}'
        f' Volantes: {volantes12} Som: {opsom12} Leitor: {leitor9}'
    )

    sheet["A12"] = str(quinta6)
    sheet["B12"] = str(indicadores11)
    sheet["C12"] = str(volantes11)
    sheet["D12"] = str(opsom11)

    sheet["A13"] = str(domingo6)
    sheet["B13"] = str(indicadores12)
    sheet["C13"] = str(volantes12)
    sheet["D13"] = str(opsom12)
    sheet["E13"] = str(leitor9)

    cont = 0
    for ind12 in voluntarios:
        if ind12 not in opsom12 and ind12 not in indicadores11 and ind12 not in indicadores12 and ind12\
                not in indicadores13 and cont <= 1:
            indicadores13.append(ind12)
            cont += 1

    cont = 0
    for ind12 in voluntarios:
        if ind12 not in opsom12 and ind12 not in indicadores11 and ind12 not in indicadores12\
                and ind12 not in volantes13 and ind12 not in volantes14 and ind12 not in indicadores13 and cont <= 1:
            volantes13.append(ind12)
            cont += 1

    cont = 0
    for ind12 in voluntarios:
        if ind12 not in opsom12 and ind12 not in indicadores12 and ind12 not in indicadores11 \
                and ind12 not in volantes13 and ind12 not in indicadores13 and cont <= 1:
            indicadores14.append(ind12)
            cont += 1

    cont = 0
    for ind12 in voluntarios:
        if ind12 not in opsom12 and ind12 not in indicadores11 and ind12 not in indicadores12 \
                and ind12 not in volantes13 and ind12 not in volantes14 and ind12 not in indicadores13 and cont <= 1:
            volantes14.append(ind12)
            cont += 1

    print()
    print()

    futuro = quinta7
    print(
        f'{futuro} - Reunião Quinta -- Indicadores: {indicadores13} '
        f'Volantes: {volantes13} Som: {opsom13}'
    )
    futuro = domingo7
    print(
        f'{futuro} - Reunião Domingo - Indicadores: {indicadores14}'
        f' Volantes: {volantes14} Som: {opsom14} Leitor: {leitor10}'
    )

    sheet["A14"] = str(quinta7)
    sheet["B14"] = str(indicadores13)
    sheet["C14"] = str(volantes13)
    sheet["D14"] = str(opsom13)

    sheet["A15"] = str(domingo7)
    sheet["B15"] = str(indicadores14)
    sheet["C15"] = str(volantes14)
    sheet["D15"] = str(opsom14)
    sheet["E15"] = str(leitor10)

    workbook.save(filename="pkla.xlsx")

priv()
