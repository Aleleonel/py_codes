voluntarios = ['José Ferreira',
               'Leonardo Verzi',
               'Eduardo Ferraz',
               'João Melo',
               'Natanael Silva',
               'Leonardo Santos',
               'Renato Verzi',
               'Ronaldo Flores',
               'Alexandre Monticelli',
               'Claudio Goveia',
               'Alexandre Leonel',
               'Nelson Custódio']

leitores = ['Alexandre Leonel',
            'Leonardo Verzi',
            'Renato Verzi',
            'Ronaldo Flores',
            'Eduardo Ferraz',
            'Nelson Custódio',
            'Alexandre Monticelli']

som = ['Natanael Silva',
       'Eduardo Ferraz',
       'Leonardo Verzi',
       'Alexandre Leonel']


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

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import json

class Voluntarios(App):
    title = 'Voluntários'

    def build(self):
        box = BoxLayout(orientation='vertical')
        self.label = Label(text='Privilégios Mecânicos ', font_size=30)
        button = Button(text='Gerar Lista', font_size=30, on_release=self.gerar)
        button2 = Button(text='Limpar', font_size=30, on_release=self.limpar)
        button3 = Button(text='Gerar Arquivo', font_size=30, on_release=self.gerar_json)
        box.add_widget(self.label)
        box.add_widget(button)
        box.add_widget(button3)
        box.add_widget(button2)
        return box

    def gerar_json(self, button3):


        print()  # Gera uma dicionário

        privilegios = {}

        volun_domingo = {}
        volun_quinta = {}

        volun_domingo2 = {}
        volun_quinta2 = {}

        volun_domingo3 = {}
        volun_quinta3 = {}

        volun_domingo4 = {}
        volun_quinta4 = {}

        volun_domingo['Indicadores'] = indicadores_domingo
        volun_domingo['Volantes'] = volantes_domingo
        volun_domingo['Operador de Som'] = som_domingo
        volun_domingo['Leitor'] = leitor

        volun_quinta['Indicadores'] = indicadores_quinta
        volun_quinta['Volantes'] = volantes_quinta
        volun_quinta['Operador de Som'] = som_quinta

        volun_domingo2['Indicadores'] = indicadores_domingo2
        volun_domingo2['Volantes'] = volantes_domingo2
        volun_domingo2['Operador de Som'] = som_domingo2
        volun_domingo2['Leitor'] = leitor2

        volun_quinta2['Indicadores'] = indicadores_quinta2
        volun_quinta2['Volantes'] = volantes_quinta2
        volun_quinta2['Operador de Som'] = som_quinta2

        volun_domingo3['Indicadores'] = indicadores_domingo3
        volun_domingo3['Volantes'] = volantes_domingo3
        volun_domingo3['Operador de Som'] = som_domingo3
        volun_domingo3['Leitor'] = leitor3

        volun_quinta3['Indicadores'] = indicadores_quinta3
        volun_quinta3['Volantes'] = volantes_quinta3
        volun_quinta3['Operador de Som'] = som_quinta3

        volun_domingo4['Indicadores'] = indicadores_domingo4
        volun_domingo4['Volantes'] = volantes_domingo4
        volun_domingo4['Operador de Som'] = som_domingo4
        volun_domingo4['Leitor'] = leitor4

        volun_quinta4['Indicadores'] = indicadores_quinta4
        volun_quinta4['Volantes'] = volantes_quinta4
        volun_quinta4['Operador de Som'] = som_quinta4

        privilegios['Primeiro_Domingo'] = volun_domingo
        privilegios['Primeira_Quinta'] = volun_quinta

        privilegios['Segundo_Domingo'] = volun_domingo2
        privilegios['Segunda_Quinta'] = volun_quinta2

        privilegios['Terceiro_Domingo'] = volun_domingo3
        privilegios['Terceira_Quinta'] = volun_quinta3

        privilegios['Quarto_Domingo'] = volun_domingo4
        privilegios['Quarta_Quinta'] = volun_quinta4

        def escrever_json(arq01):
            with open('aq01.json', 'w', encoding='utf8') as f:
                json.dump(arq01, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

        escrever_json(privilegios)


        print()
        print(f'Domingo - {volun_domingo}')
        print(f'Quinta-feira - {volun_quinta}')
        print()
        print(f'Domingo - {volun_domingo2}')
        print(f'Quinta-feira - {volun_quinta2}')
        print()
        print(f'Domingo - {volun_domingo3}')
        print(f'Quinta-feira - {volun_quinta3}')
        print()
        print(f'Domingo - {volun_domingo4}')
        print(f'Quinta-feira - {volun_quinta4}')

    def limpar(self, button2):
        print(f'limpando')

        indicadores_quinta.clear()
        volantes_quinta.clear()
        som_quinta.clear()

        indicadores_domingo.clear()
        volantes_domingo.clear()
        som_domingo.clear()
        leitor.clear()

        indicadores_quinta2.clear()
        volantes_quinta2.clear()
        som_quinta2.clear()

        indicadores_domingo2.clear()
        volantes_domingo2.clear()
        som_domingo2.clear()
        leitor2.clear()

        indicadores_quinta3.clear()
        volantes_quinta3.clear()
        som_quinta3.clear()

        indicadores_domingo3.clear()
        volantes_domingo3.clear()
        som_domingo3.clear()
        leitor3.clear()

        indicadores_quinta4.clear()
        volantes_quinta4.clear()
        som_quinta4.clear()

        indicadores_domingo4.clear()
        volantes_domingo4.clear()
        som_domingo4.clear()
        leitor4.clear()

    def gerar(self, button):

        self.label.text = 'Voluntarios da semana - teste'

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
        # print(voluntarios_Domingo)


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
        # print(voluntarios_Quinta)

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
        # print(voluntarios_Domingo2)

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
        # print(voluntarios_Quinta3)

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
        # print(voluntarios_Domingo3)

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
                    and som[s] not in som_domingo3 and som[s] not in leitor3 \
                    and voluntarios[v] not in voluntarios_Quinta3:
                voluntarios_Quinta4.append(som[s])
        print()
        # print(voluntarios_Quinta4)

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
        # print(voluntarios_Domingo4)

        # voluntarios do domingo Quarta semana
        cont = 0
        for v in range(len(voluntarios_Domingo4)):
            # indicadores de Domingo
            if voluntarios_Domingo4[v] not in indicadores_domingo4 and voluntarios_Domingo4[v] \
                    not in volantes_domingo4 and voluntarios_Domingo4[v] not in som_domingo4 \
                    and voluntarios_Domingo4[v] not in leitor and cont <= 1:
                indicadores_domingo4.append(voluntarios_Domingo4[v])
                cont += 1

        cont = 0
        for v in range(len(voluntarios_Domingo4)):
            # volantes de  Domingo
            if voluntarios_Domingo4[v] not in indicadores_domingo4 and voluntarios_Domingo4[v] \
                    not in volantes_domingo4 and voluntarios_Domingo4[v] not in som_domingo4 \
                    and voluntarios_Domingo4[v] not in leitor and cont <= 1:
                volantes_domingo4.append(voluntarios_Domingo4[v])
                cont += 1

        # verifica se tem apenas um volante e acrescenta + 1
        for v in range(len(voluntarios_Domingo4)):

            if len(volantes_domingo4) < 2:
                cont = 0
                for ind in range(len(indicadores_quinta4)):
                    if indicadores_quinta4[ind] not in volantes_domingo4:
                        volantes_domingo4.append(indicadores_quinta4)
                cont += 1

        cont = 0
        for s in range(len(som)):
            # Operadores do Som - Domingo
            if som[s] not in indicadores_domingo4 and som[s] not in volantes_domingo4 and som[s] not in som_domingo3 \
                    and som[s] not in som_domingo4 \
                    and som[s] not in som_quinta3 and cont < 1:
                som_domingo4.append(som[s])
                cont += 1

        cont = 0
        for l in range(len(leitores)):
            # Leitor - Domingo
            if leitores[l] not in indicadores_domingo4 and leitores[l] not in volantes_domingo4 \
                    and leitores[l] not in leitor3 \
                    and leitores[l] not in som_domingo4 and cont < 1:
                leitor4.append(leitores[l])
                cont += 1

        print() # imprime na tela
        print(f'Indicadores Domingo: {indicadores_domingo4}')
        print(f'Volantes Domingo: {volantes_domingo4}')
        print(f'Operadores de som Domingo: {som_domingo4}')
        print(f'Leitor de A Sentinela: {leitor4}')




Voluntarios().run()