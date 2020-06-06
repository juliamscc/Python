largura = l = int(input("Digite a largura do retângulo: "))
altura = a = int(input("Digite a altura do retângulo: "))

while altura != 0:
    while largura != 0:
        print("#",end = " ")
        largura = largura - 1
    print()
    largura = l
    altura = altura - 1

