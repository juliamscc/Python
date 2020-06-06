qtde = int(input("Digite a quantidade de números ímpares a serem visualizados :"))
v = 0
n = 1

while v < qtde:
    if not (n % 2 == 0):
        print(n)
        v = v + 1
    n = n + 1
    
