from datetime import date

hj = date.today()
dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')


if hj.weekday() == 0:
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

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

elif hj.weekday() == 1:
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

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')
    print(quinta1)
    print(domingo1)
    print(quinta2)
    print(domingo2)
    print(quinta3)
    print(domingo3)
    print(quinta4)
    print(domingo4)

elif hj.weekday() == 2:
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

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

elif hj.weekday() == 3:
    domingo1 = date.fromordinal(hj.toordinal() + 3)
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

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para o próximo Domingo dia: {domingo1}')

elif hj.weekday() == 4:
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

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para o próximo Domingo dia: {domingo1}')

elif hj.weekday() == 5:
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

    print("Hoje é", dias[hj.weekday()])
    print(f'A data será gerada para o próximo Domingo dia: {domingo1}')
elif hj.weekday() == 6:
    quinta1 = date.fromordinal(hj.toordinal() + 4)
    ordinario_number = quinta1.toordinal()
    domingo2 = date.fromordinal(ordinario_number + 3)
    ordinario_number = domingo2.toordinal()
    quinta2 = date.fromordinal(ordinario_number + 4)
    ordinario_number = quinta2.toordinal()
    domingo3 = date.fromordinal(ordinario_number + 3)
    ordinario_number = domingo3.toordinal()
    quinta4 = date.fromordinal(ordinario_number + 4)
    ordinario_number = quinta4.toordinal()
    domingo4 = date.fromordinal(ordinario_number + 3)

    print("Hoje é", dias[hj.weekday()])
    print(f'\nA data será gerada para a próxima Quinta-Feira dia: {quinta1}')

