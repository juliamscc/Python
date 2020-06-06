def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

x = int(input("Digite um número inteiro e positivo: "))
while x >= 0:
    f = fatorial(x)
    print (f)
    x = int(input("Digite um número inteiro e positivo: "))
