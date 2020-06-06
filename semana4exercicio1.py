#fatorial
n = int(input("Digite um número inteiro para ser calculado o fatorial :"))
a = n - 1

if n == 0:
        print(1)
else:
    while a > 0:
        n = n * a
        a = a - 1
    print(n)

        
        
