def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
    if fatorial(7) == 5040:
        print("Funciona para 7")
    else:
        print("Não funciona para 7")
    if fatorial(-5) == -120:
        print("Funciona para -5")
    else:
        print("Não funciona para -5")
    if fatorial(-7) == -5040:
        print("Funciona para -7")
    else:
        print("Não funciona para -7")

def testa_numero_binomial():
    if numero_binomial(3,2) == 3:
        print("Funciona para 3,2")
    else:
        print("Não funciona para 3,2")
    if numero_binomial(10,5) == 252:
        print("Funciona para 10,5")
    else:
        print("Não funciona para 10,5")
    if numero_binomial(9,0) == 1:
        print("Funciona para 9,0")
    else:
        print("Não funciona para 9,0")
    if numero_binomial(6,5) == 6:
        print("Funciona para 6,5")
    else:
        print("Não funciona para 6,5")

