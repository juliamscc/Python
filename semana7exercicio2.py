largura = l = int(input("Digite a largura do retângulo: "))
altura = a = int(input("Digite a altura do retângulo: "))

while altura != 0:
    if altura == 1 or altura == a:
        while largura != 0:
            print("#",end = " ")
            largura = largura - 1
        print ()
    else:
        print("#",end = " ")
        x = l - 1
        while x > 1:
            print(" ",end = " ")
            x = x - 1
        print("#")
        largura = largura - 1
    largura = l
    altura = altura - 1

