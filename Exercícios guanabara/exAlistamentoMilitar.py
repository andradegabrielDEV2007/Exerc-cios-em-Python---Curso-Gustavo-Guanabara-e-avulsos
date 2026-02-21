from datetime import date

def verificando (ano_nascimento, nomeCandidato):
    ano_atual = date.today().year
    idadeCandidato = ano_atual - ano_nascimento

    if idadeCandidato < 18:
        tempoRestante = 18 - idadeCandidato
        ano_texto = 'ano' if tempoRestante == 1 else 'anos'
        return f'{nomeCandidato}, ainda faltam {tempoRestante} {ano_texto} para você se alistar!'

    elif idadeCandidato == 18:
        return f'{nomeCandidato}, você está no tempo certo de se alistar!'

    elif idadeCandidato > 18:
        tempoUltrapassado = idadeCandidato - 18
        ano_texto = 'ano' if tempoUltrapassado == 1 else 'anos'
        return (f'{nomeCandidato}, você passou do tempo de se alistar, você deveria '
                f'ter feito o alistamento a {tempoUltrapassado} {ano_texto}.\nProcure '
                f'regularizar seu cadastro')
nome = input("Digite seu nome: ")
ano = int(input('Digite o ano de nascimento: '))
print(verificando(ano, nome))
