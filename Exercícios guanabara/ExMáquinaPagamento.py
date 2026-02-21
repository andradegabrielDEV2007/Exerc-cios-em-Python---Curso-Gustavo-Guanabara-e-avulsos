def pagamento (tipoPagamento, valorProduto):
    if tipoPagamento == 1:
        valorProduto = valorProduto * 0.9

        return (f'Você escolheu o método de pagamento à vista em dinheiro.\nO total a ser '
                f'pago é: R$ {valorProduto:.2f}\nVocê recebeu 10% de desconto.')
    elif tipoPagamento == 2:
        valorProduto = valorProduto * 0.95

        return (f'Você escolheu o método de pagamento à vista '
                f'no cartão.\nO total a ser pago é: '
                f'R$ {valorProduto:.2f}\nVocê recebeu 5% de desconto.')
    elif tipoPagamento == 3:

        return (f'Você escolheu o método de pagamento parcelado '
                f'em até 2x sem juros.\nO valor a ser pago é: R$ {valorProduto:.2f}')
    elif tipoPagamento == 4:
        valorProduto = valorProduto * 1.2

        return (f'Você escolheu o método de pagamento parcelado em mais de 2x.\nO valor a ser'
                f' pago com 20% de juros é: R$ {valorProduto:.2f}')
    else:
        return f'Forma de pagamento inválida. Tente novamente.'
valorProduto = float(input('Digite o valor do produto: '))
tipoPagamento = int(input('Escolha o tipo de pagamento\n1. Dinheiro\n'
                          '2. Débito à vista\n3. Crédito até 2x\n4. Crédito mais de 2x: '))

print(pagamento(tipoPagamento, valorProduto))
