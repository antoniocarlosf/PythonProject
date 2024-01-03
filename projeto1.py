# import random
from time import sleep
print('-*'*20)
print('Bem Vindo ao RPG de Turnos (Teste)')
print('-*'*20)
print('''Qual Personagem quer ser?
[1] Cavalheiro
[2] Arqueiro''')

while True:
    personagem = int(input('Opção: '))
    if personagem == 1:
        sleep(1)
        escolha = input('Você escolheu o Cavalheiro. Esta certo disto? [S/N]: ').upper()
        if escolha == 'N':
            print('''Escolha novamente:
            [1] Cavaleiro
            [2] Arqueiro''')
            personagem = int(input('Opção: '))
        elif escolha == 'S':
            sleep(1)
            print('''Você é um cavalheiro.
Seu dano é de: 7
Sua vida é de: 15
Voce bate de perto.''')
            print('-*'*30)
            break
    if personagem == 2:
        escolha = input('Você escolheu o Arqueiro. Esta certo disto? [S/N]: ').upper()
        if escolha == 'N':
            print('''Escolha novamente:
            [1] Cavaleiro
            [2] Arqueiro''')
            personagem = int(input('Opção: '))
        elif escolha == 'S':
            sleep(1)
            print('''Você é um Arqueiro.
Seu dano é de: 10
Sua vida é de: 8
Voce bate de longe.''')
            print('-*'*30)
            break
sleep(1)
print('''Voce tem 2 areas para poder explorar
[Floresta]
[Cidade]
Qual deseja explorar primeiro?''')
while True:
    area = input('[Cidade] ou [Floresta]? ').lower()
    if area == 'floresta':
        sleep(1)
        fazer = input('Voce entrou na floresta. Continuar se aprofundando? [S/N]: ').upper()
        if fazer == 'S':
            sleep(1)
            print('''Você se aprofundou na floresta e encontrou um Lobo. Oque fazer?
            [1] Atacar
            [2] Tentar passar despercebido
            [3] Voltar''')
            acao = input('Ação: ')
            if acao == 1:
                sleep(1)
                print('Voce atacou o lobo e conseguiu derrota-lo com 1 ataque.')

            elif acao == 2:
                sleep(1)
                print('Você tentou passar despercebido e o lobo te atacou. [-2 De Vida]')

            elif acao == 3:
                sleep(1)
                print('Você voltou para area inicial.')
                print('-*'*30)
                print('''Voce tem 2 areas para explorar
                [Floresta]
                [Cidade]
                Qual deseja explorar primeiro?''')
                break
    elif area == 'cidade':
        sleep(1)
        print('-*'*30)
        print('Voce entrou na cidade. Há muitos mercadores querendo tirar seu dinheiro! TENHA CUIDADO')
        print('-*'*30)
        print('''Oque fazer agora?
        [1] Ir na loja de suprimentos
        [2] Ir na loja de armaduras
        [3] Procurar uma missão''')
        acao2 = input('Oque fazer agora: ')
        if acao2 == 1:
            sleep(1)
            ls = input('Você adentrou a loja de suprimentos. Quer ver oque há no estoque? [S/N] ').upper()
            if ls == 'S':
                sleep(1)
                print('''Maçã - 5 Moedas de Prata
                Pacote de viajante - 30 Moedas de Prata''')
                print('Você ainda não tem dinheiro! Procure uma missão para conseguir moedas.')
            elif ls == 'N':
                sleep(1)
                print('''Oque fazer agora?
                [1] Ir na loja de suprimentos
                [2] Ir na loja de armadura
                [3] Procurar uma missão''')
                acao2 = input('Oque fazer agora: ')
                if acao2 == 2:
                    sleep(1)
                    la = input('Você adentrou a loja de armaduras. Quer ver oque há no estoque? [S/N] ').upper()
                    if la == 'S':
                        print('''Armadura de couro - 20 Moedas de Prata (+5 De Vida)
                        Armadura de Ferro - 1 Moeda de Ouro (+ 12 De Vida)''')
                        print('Você ainda não tem dinheiro! Procure uma missão para conseguir moedas.')
                        break
