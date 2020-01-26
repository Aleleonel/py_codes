import csv
from datetime import date
hj = (date.today())
#print(hj.toordinal()) #descobrir qual é a data atual em numeros ordinais
futuro = date.fromordinal(737399+13)

voluntarios = ['Alexandre', 'Leonardo', 'Eduardo', 'João', 'Natanael', 'Renato', 'Ronaldo', 'Ferreira', 'Claudio']
som = ['Natanael', 'Eduardo', 'Leonardo', 'Alexandre']

a = indicadores = []
b = volantes = []
c = opsom = ['Leonardo']

indicadores2 = []
volantes2 = []
opsom2 = ['Natanael']
d = leitor1 = ['Eduardo']

indicadores3 = []
volantes3 = []
opsom3 = ['Alexandre']

indicadores4 = []
volantes4 = []
opsom4 = ['Eduardo']
leitor2 = ['Alexandre']

indicadores5 = []
volantes5 = []
opsom5 = ['Leonardo']
leitor3 = ['Ronaldo']

indicadores6 = []
volantes6 = []
opsom6 = ['Natanael']

indicadores7 = []
volantes7 = []
opsom7 = ['Alexandre']
leitor4 = ['Renato']

indicadores8 = []
volantes8 = []
opsom8 = ['Eduardo']

indicadores9 = []
volantes9 = []
opsom9 = ['Leonardo']
leitor6 = ['Nelson']

indicadores10 = []
volantes10 = []
opsom10 = ['Natanael']
leitor7 = []
leitor8 = ['Alexandre']

#
# def arquivos(a, b, c, d):
#     try:
#
#         arquivo = open('../arquivo/new_arquivo.txt', 'w')
#         arquivo.writelines(str('- Indicadores'))
#
#         for i in a:
#             arquivo.writelines(str(' - '))
#             arquivo.writelines(str(i))
#
#         arquivo.writelines(str(' - Volantes'))
#         for ii in b:
#             arquivo.writelines(str(' - '))
#             arquivo.writelines(str(ii))
#         for ii in b:
#             arquivo.writelines(str(' - '))
#             arquivo.writelines(str(ii))
#         return a, b, c, d
#
#     except Exception as Error:
#         print()
#         print('não deu certo', Error)


def priv():

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
        if ind2 not in opsom2 and ind2 not in leitor1 and ind2 not in indicadores2 and ind2 not in volantes and cont <= 1:
            volantes2.append(ind2)
            cont += 1

    print()
    futuro = date.fromordinal(737399+13)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores} Volantes: {volantes} Som: {opsom}')
    futuro = date.fromordinal(hj.toordinal()+16)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores2} Volantes: {volantes2} Som: {opsom2} Leitor: {leitor1}')


    cont = 0
    for ind3 in voluntarios:
        if ind3 not in opsom3 and ind3 not in indicadores2 and ind3 and ind3 not in volantes3 and cont <= 1:
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
        if ind4 not in opsom4 and ind4 not in leitor2 and ind4 not in indicadores4 and ind4 not in volantes3 and cont <= 1:
            volantes4.append(ind4)
            cont += 1

    print()
    futuro = date.fromordinal(737399+20)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores3} Volantes: {volantes3} Som: {opsom3}')
    futuro = date.fromordinal(737399+23)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores4} Volantes: {volantes4} Som: {opsom4} Leitor: {leitor2}')

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
        if ind6 not in opsom6 and ind6 not in indicadores5 and ind6 not in leitor3 and cont <= 1:
            indicadores6.append(ind6)
            cont += 1

    cont = 0
    for ind6 in voluntarios:
        if ind6 not in opsom6 and ind6 not in leitor3 and ind6 not in indicadores6 and ind6 not in indicadores5 and cont <= 1:
            volantes6.append(ind6)
            cont += 1

    print()
    futuro = date.fromordinal(737399+27)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores5} Volantes: {volantes5} Som: {opsom5}')
    futuro = date.fromordinal(737399+30)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores6} Volantes: {volantes6} Som: {opsom6} Leitor: {leitor3}')

    cont = 0
    for ind7 in voluntarios:
        if ind7 not in opsom7 and ind7 not in indicadores6 and ind7 not in indicadores5 and cont <= 1:
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
    futuro = date.fromordinal(737399+34)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores7} Volantes: {volantes7} Som: {opsom7}')
    futuro = date.fromordinal(737399+37)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores8} Volantes: {volantes8} Som: {opsom8} Leitor: {leitor4}')

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
    futuro = date.fromordinal(737399+41)
    print(f'{futuro} - Reunião Quinta -- Indicadores: {indicadores9} Volantes: {volantes9} Som: {opsom9}')

    futuro = date.fromordinal(737399+44)
    print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores10} Volantes: {volantes10} Som: {opsom10} leitor: {leitor6}')

    from openpyxl import Workbook

    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = str(futuro)
    sheet["B1"] = "Reunião Domingo - Indicadores:" + str(indicadores10)

    workbook.save(filename="pkla.xlsx")

# arquivos(a, b, c, d)





cont = 0
while cont < 2:
    priv()
    cont += 1
