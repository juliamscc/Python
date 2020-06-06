numero_str = input("Digite um número inteiro: ")
numero = int(numero_str)
l = int(len(numero_str))
variavel=0
soma=0

while variavel < l:
    resto = numero % 10
    soma = soma + resto
    numero = numero // 10
    variavel=variavel+1

print("A soma dos algarismos é", soma)
    

