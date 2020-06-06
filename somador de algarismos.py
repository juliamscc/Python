n_str = input("Digite um número inteiro: ")
l = int(len(n_str))
variavel=0
soma=0

while variavel < l:
    soma = soma + int(n_str[variavel])
    variavel = variavel + 1

print("A soma dos algarismos é", soma)
    

