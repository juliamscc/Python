numero = int(input("Digite um número inteiro: ")) #identifica alg iguais
alg_a = numero % 10
n = numero // 10
alg_iguais = False

while n > 0 and not alg_iguais:
    x = n % 10
    if x == alg_a:
        alg_iguais = True
    n = n // 10
    alg_a = x

if alg_iguais:
    print("sim")
else:
    print("não")
