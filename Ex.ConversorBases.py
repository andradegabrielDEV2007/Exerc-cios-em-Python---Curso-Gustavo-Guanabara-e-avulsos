print("Olá! Seja bem vindo! \n")
escolhaUsuario = int(input("Escolha se você quer converter para:\n-Binário(1)\n-Octal(2)\n-Hexadecimal(3)\nSó aceitamos números inteiros.\n"))

if escolhaUsuario in (1, 2, 3):

 if escolhaUsuario == 1:
    numeroUsuario = int(input("Digite o número que você deseja converter: "))
    numeroBinario = bin(numeroUsuario)
    print(f"O seu número convertido para binário é: {format(numeroBinario, 'b')}")

 elif escolhaUsuario == 2:
    numeroUsuario = int(input("Digite o número que você deseja converter: "))
    numeroOctal = oct(numeroUsuario)
    print(f"O seu número convertido para octal é: {format(numeroOctal, 'o')}")

 elif escolhaUsuario == 3:
    numeroUsuario = int(input("Digite o número que você deseja converter: "))
    numeroHexadecimal = hex(numeroUsuario)
    print(f"O seu número convertido para hexadecimal é: {format(numeroHexadecimal, 'x')}")

else:
    print("Número inválido")