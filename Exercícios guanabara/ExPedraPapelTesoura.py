import random

opcoes = ('pedra', 'papel', 'tesoura')

vence = {'papel': 'pedra',
         'pedra': 'tesoura',
         'tesoura': 'papel'}

resultado_jogador = input('Esolha entre pedra, papel ou tesoura: ').strip().lower()

if resultado_jogador not in opcoes:
    print( f'escolha inválida, por favor, tente novamente.')
else:
    resultado_computador = random.choice(opcoes)

    while resultado_computador == resultado_jogador:
         resultado_computador = random.choice(opcoes)

    print('Você escolheu:', resultado_jogador)
    print('Computador:', resultado_computador)

    if vence[resultado_jogador] == resultado_computador:
        print('Carregando...')
        print('Parabéns! Você venceu! Uhuu')
    else:
        print('Carregando...')
        print('Ixi, não foi dessa vez!')

