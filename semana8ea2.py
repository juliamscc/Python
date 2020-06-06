lista = []
numero = 1
while numero != 0:
    numero = int(input("Digite um número inteiro ou zero para finalizar: "))
    lista.append(numero)
x = len(lista)
aux = x - 2
while aux >= 0:
    print(lista[aux])
    aux = aux - 1
    
    
