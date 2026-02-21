print("Seja bem vindo à calculadora que compara números\n")

a, b = map(int, input("Digite os números que você deseja comparar:\n").split())

if a == b:
        print(f"Os números {a} e {b} são iguais")
elif a > b:
        print(f"O número {a} é maior que o número {b}")
elif a < b:
        print(f"O número {b} é maior que o número {a}")


