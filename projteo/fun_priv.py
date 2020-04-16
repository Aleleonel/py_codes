from datetime import date
hj = (date.today())
# date_now = datetime.now()
# if hj == date_now:
#     hj = date_now - datetime.timedelta(days=1)

print(hj)

voluntarios = ['Ferreira',  'João', 'Nelson', 'Leonardo Santos', 'Claudio', 'Monticelli', 'Alexandre',
               'Leonardo', 'Eduardo', 'Natanael', 'Renato', 'Ronaldo', ]

som = ['Natanael', 'Eduardo', 'Leonardo', 'Alexandre']
somaux = []

leitores = ['Alexandre', 'Leonardo', 'Renato', 'Eduardo', 'Ronaldo', 'Nelson', 'Monticelli']
leitoresaux = []

indicadores = []
indicadores1 = []
indicadores2 = []
indicadores3 = []
indicadores4 = []
indicadores5 = []
indicadores6 = []
indicadores7 = []
indicadores8 = []
indicadores9 = []
indicadores10 = []
indicadores11 = []
indicadores12 = []
indicadores13 = []
indicadores14 = []

indicadoresaux = []

volantes = []
volantes1 = []
volantes2 = []
volantes3 = []
volantes4 = []
volantes5 = []
volantes6 = []
volantes7 = []
volantes8 = []
volantes9 = []
volantes10 = []
volantes11 = []
volantes12 = []
volantes13 = []
volantes14 = []
volantes15 = []

volantesaux = []

opsom = []
opsom1 = []
opsom2 = []
opsom3 = []
opsom4 = []
opsom5 = []
opsom6 = []
opsom7 = []
opsom8 = []
opsom9 = []
opsom10 = []
opsom11 = []
opsom12 = []
opsom13 = []
opsom14 = []
opsom15 = []

opsomaux = []

sentinela = []
sentinela1 = []
sentinela2 = []
sentinela3 = []
sentinela4 = []
sentinela5 = []
sentinela6 = []
sentinela7 = []
sentinela8 = []
sentinela9 = []
sentinela10 = []
sentinela11 = []
sentinela12 = []
sentinela13 = []
sentinela14 = []

sentinelaux = []


def gera_leitor():
    try:
        cont = 0
        for leitor in leitores:
            if leitor not in opsom2 and cont < 1:
                sentinela.append(leitor)
                cont += 1
        cont = 0

        for leitor in leitores:
            if leitor not in sentinela and leitor not in opsom4 and cont < 1:
                sentinela1.append(leitor)
                cont += 1

        cont = 0
        for leitor in leitores:
            if leitor not in sentinela and leitor not in sentinela1 and leitor not in opsom6 and cont < 1:
                sentinela2.append(leitor)
                cont += 1

        cont = 0
        for leitor in leitores:
            if leitor not in sentinela and leitor not in sentinela1 and leitor not in sentinela2\
                    and leitor not in opsom8 and cont < 1:
                sentinela3.append(leitor)
                cont += 1

        cont = 0
        for leitor in leitores:
            if leitor not in sentinela and leitor not in sentinela1 and leitor not in sentinela2\
                    and leitor not in sentinela3 and leitor not in opsom10 and cont < 1:
                sentinela4.append(leitor)
                cont += 1

        cont = 0
        for leitor in leitores:
            if leitor not in sentinela and leitor not in sentinela1 and leitor not in sentinela2\
                    and leitor not in sentinela3 and leitor not in sentinela4 and leitor not in opsom12 and cont < 1:
                sentinela5.append(leitor)
                cont += 1

        cont = 0
        for leitor in leitores:
            if leitor not in sentinela and leitor not in sentinela1 and leitor not in sentinela2\
                    and leitor not in sentinela3 and leitor not in sentinela4 and leitor not in sentinela5\
                    and leitor not in opsom14 and cont < 1:
                sentinela6.append(leitor)
                cont += 1

    except Exception as erro:
        print()
        print('não deu certo', erro)
        quit()

    return


def gera_opersom():
    try:
        cont = 0
        for operasom in som:
            if operasom not in sentinela and cont < 1:
                opsom2.append(operasom)
                cont += 1
        cont = 0
        for operasom in som:
            if operasom not in opsom2 and cont < 1:
                opsom1.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom2 and operasom not in opsom1 and operasom not in sentinela1 and cont < 1:
                opsom4.append(operasom)
                cont += 1
        cont = 0
        for operasom in som:
            if operasom not in opsom1 and operasom not in opsom4 and cont < 1:
                opsom3.append(operasom)
                cont += 1
        cont = 0
        for operasom in som:
            if operasom not in opsom2 and operasom not in opsom1 and operasom not in opsom4 and cont < 1:
                opsom6.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom1 and operasom not in opsom2 and operasom not in opsom3 and operasom not in opsom6\
                    and cont < 1:
                opsom5.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom2 and operasom not in opsom1 and operasom not in opsom4\
                    and operasom not in sentinela3 and cont < 1:
                opsom8.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom5 and operasom not in opsom8 and operasom not in sentinela3 and cont < 1:
                opsom9.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom8 and operasom not in opsom9 and operasom and operasom not in sentinela4\
                    and cont < 1:
                opsom10.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom9 and operasom not in opsom10 and operasom and cont < 1:
                opsom11.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom11 and operasom not in opsom10 and operasom and operasom not in sentinela5 and cont < 1:
                opsom12.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom11 and operasom not in opsom12 and operasom and cont < 1:
                opsom13.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom12 and operasom not in opsom13 and operasom and operasom not in sentinela6 and cont < 1:
                opsom14.append(operasom)
                cont += 1

        cont = 0
        for operasom in som:
            if operasom not in opsom13 and operasom not in opsom14 and operasom and cont < 1:
                opsom15.append(operasom)
                cont += 1

    except Exception as erro:
        print()
        print('não deu certo', erro)
        quit()
    return


def gera_volantes():
    try:
        cont = 0
        for volante in voluntarios:
            if volante not in indicadores and volante not in indicadores1 and volante not in opsom\
                    and volante not in sentinela and cont <= 1:
                volantes.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in indicadores and volante not in indicadores1 and volante not in volantes\
                    and volante not in opsom1 and cont <= 1:
                volantes1.append(volante)
                cont += 1

        for verifica in volantes:
            if verifica == indicadores1:
                volantes1.append('novo nome')


        cont = 0
        for volante in voluntarios:
            if volante not in indicadores2 and volante not in volantes1 and volante not in sentinela1\
                    and volante not in opsom4 and cont <= 1:
                volantes2.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes1 and volante not in volantes2\
                    and volante not in opsom3 and cont <= 1:
                volantes3.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes2 and volante not in volantes3 and volante not in opsom6\
                    and volante not in sentinela2 and cont <= 1:
                volantes4.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes and volante not in volantes2 and volante not in volantes3\
                    and volante not in volantes4 and volante not in opsom5 and cont <= 1:
                volantes5.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes4 and volante not in volantes5 and volante not in opsom8\
                    and volante not in sentinela3 and cont <= 1:
                volantes6.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes5 and volante not in volantes6 and volante not in opsom9 and cont <= 1:
                volantes7.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes6 and volante not in volantes7 and volante not in opsom10 \
                    and volante not in sentinela4 and cont <= 1:
                volantes8.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes7 and volante not in volantes8 and volante not in opsom11 and cont <= 1:
                volantes9.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes8 and volante not in volantes9 and volante not in opsom12\
                    and volante not in sentinela5 and cont <= 1:
                volantes10.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes9 and volante not in volantes10 and volante not in opsom13 and cont <= 1:
                volantes11.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes10 and volante not in volantes11 and volante not in opsom14 \
                    and volante not in sentinela6 and cont <= 1:
                volantes12.append(volante)
                cont += 1

        cont = 0
        for volante in voluntarios:
            if volante not in volantes11 and volante not in volantes12 and volante not in opsom15 and cont <= 1:
                volantes13.append(volante)
                cont += 1

    except Exception as erro:
        print()
        print('não deu certo', erro)
        quit()
    return


def gera_indicador():
    try:
        cont = 0
        for indicador in voluntarios:
            if indicador not in volantes and indicador not in opsom2 and indicador not in sentinela and cont <= 1:
                indicadores.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadoresaux and indicador not in indicadores and indicador not in volantes1\
                    and indicador not in opsom1 and cont <= 1:
                indicadores1.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in volantes2 and indicador not in opsom4 and indicador not in sentinela1 and cont <= 1:
                indicadores2.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores2 and indicador not in volantes3 and indicador not in opsom3 and cont <= 1:
                indicadores3.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores3 and indicador not in volantes4 and indicador not in opsom6\
                    and indicador not in sentinela2 and cont <= 1:
                indicadores4.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores4 and indicador not in volantes5 and indicador not in opsom5\
                    and cont <= 1:
                indicadores5.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores5 and indicador not in volantes6 and indicador not in opsom8\
                    and indicador not in sentinela3 and cont <= 1:
                indicadores6.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores6 and indicador not in volantes7 and indicador not in opsom9 and cont <= 1:
                indicadores7.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores7 and indicador not in volantes8 and indicador not in opsom10 \
                    and indicador not in sentinela4 and cont <= 1:
                indicadores8.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores8 and indicador not in volantes9 and indicador not in opsom11 and cont <= 1:
                indicadores9.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores9 and indicador not in volantes10 and indicador not in opsom12 \
                    and indicador not in sentinela5 and cont <= 1:
                indicadores10.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores10 and indicador not in volantes11 and indicador not in opsom13 and cont <= 1:
                indicadores11.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores11 and indicador not in volantes12 and indicador not in opsom14 \
                    and indicador not in sentinela6 and cont <= 1:
                indicadores12.append(indicador)
                cont += 1

        cont = 0
        for indicador in voluntarios:
            if indicador not in indicadores12 and indicador not in volantes13 and indicador not in opsom15 and cont <= 1:
                indicadores13.append(indicador)
                cont += 1

    except Exception as erro:
        print()
        print('não deu certo', erro)
        quit()
    return


def imprime():
    try:

        dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

        if hj.weekday() == 0:  # segunda-feira #
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

        elif hj.weekday() == 1:  # terça-feira #
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

        elif hj.weekday() == 2:  # quarta-feira #
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

        elif hj.weekday() == 3:  # quinta-feira #

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

        elif hj.weekday() == 4:  # sexta-feita #
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

        elif hj.weekday() == 5:  # sábado #
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

        futuro = quinta1
        print(f'{futuro} - Reunião Quinda  - Indicadores1: {indicadores1} Volantes1: {volantes1} Operador de Som1: {opsom1}')
        futuro = domingo1
        print(f'{futuro} - Reunião Domingo - Indicadores: {indicadores} Volantes {volantes} Operador de Som2 {opsom2} Leitor {sentinela}')
        print()

        futuro = quinta2
        print(f'{futuro} - Reunião Quinda  - Indicadores3: {indicadores3} Volantes3 {volantes3} Operador de Som3 {opsom3}')
        futuro = domingo2
        print(f'{futuro} - Reunião Domingo - Indicadores2: {indicadores2} Volantes2 {volantes2} Operador de Som4 {opsom4} Leitor1 {sentinela1}')
        print()

        futuro = quinta3
        print(f'{futuro} - Reunião Quinda  - Indicadores5: {indicadores5} Volantes5 {volantes5}'
              f' Operador de Som5 {opsom5}')
        futuro = domingo3
        print(f'{futuro} - Reunião Domingo - Indicadores4: {indicadores4} Volantes4 {volantes4}'
              f' Operador de Som6 {opsom6} Leitor2 {sentinela2}')
        print()

        futuro = quinta4
        print(f'{futuro} - Reunião Quinda  - Indicadores7: {indicadores7} Volantes7 {volantes7}'
              f' Operador de Som9 {opsom9}')
        futuro = domingo4
        print(f'{futuro} - Reunião Domingo - Indicadores6: {indicadores6} Volantes6 {volantes6}'
              f' Operador de Som8 {opsom8} Leitor3 {sentinela3}')
        print()

        futuro = quinta5
        print(f'{futuro} - Reunião Quinda  - Indicadores9: {indicadores9} Volantes9 {volantes9} Operador de Som11 {opsom11}')
        futuro = domingo5
        print(f'{futuro} - Reunião Domingo - Indicadores8: {indicadores8} Volantes8 {volantes8} Operador de Som10 {opsom10} '
              f'Leitor4 {sentinela4}')
        print()

        futuro = quinta6
        print(f'{futuro} - Reunião Quinda  - Indicadores11: {indicadores11} Volantes11 {volantes11} Operador de Som13 {opsom13}')
        futuro = domingo6
        print(f'{futuro} - Reunião Domingo - Indicadores10: {indicadores10} Volantes10 {volantes10} Operador de Som12 {opsom12} '
              f'Leitor5 {sentinela5}')
        print()

        futuro = quinta7
        print(f'{futuro} - Reunião Quinda  - Indicadores13: {indicadores13} Volantes13 {volantes13} Operador de Som15 {opsom15}')
        futuro = domingo7
        print(f'{futuro} - Reunião Domingo - Indicadores12: {indicadores12} Volantes12 {volantes12} Operador de Som14 {opsom14} '
              f'Leitor6 {sentinela6}')
        print()

    except Exception as erro:
        print()
        print('não deu certo', erro)
        quit()
    return


def main():
    print("Olá\n")
    cont = 0
    x = int(input("Digite 1 para começar a preencher o nome dos estudantes :\n"))
    if x == 1:
        gera_leitor()
        gera_opersom()
        gera_volantes()
        gera_indicador()
        imprime()
    else:
        print("Opção Inválida")



main()

