def conferindoTriangulo (medidaA, medidaB, medidaC):


    medidas = (medidaA, medidaB, medidaC)

    if medidaA + medidaB < medidaC and medidaA + medidaC < medidaB and medidaB + medidaC < medidaA:
        return f'As medidas fornecidas não são de um triângulo, reenvie as informações'

    elif len(set(medidas)) == 1:
        return f'As medidas fornecidas formam um triângulo equilátero'

    elif len(set(medidas)) == 3:
        return f'As medidas fornecidas formam um triângulo escaleno'

    else:
        return f'As medidas fornecidas formam um triângulo isósceles'



medidaA, medidaB, medidaC = map(int, input('Digite as medidas do seu triângulo\n').split())
print(conferindoTriangulo(medidaA, medidaB, medidaC))
