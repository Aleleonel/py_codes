from funcoes import *

print('Olá, qual é o seu nome?')
nome = pegaNome(resposta())
resp = respondeNome(nome)
print(resp)


def saiPrograma():
    while True:
        resp = resposta()
        if resp == 'tchau':
            break
        else:
            for pl in palavras:
                pass

            print('digite outra coisa')

    print('Tchau tchau')


