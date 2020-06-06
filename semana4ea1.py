numero = int(input("Digite um número inteiro e positivo: "))
n = numero - 1
resto = 1
resto0 = False

if numero == 1:
        print("não primo")
else:
        while n > 1 and not resto0:
                resto = numero % n
                n = n - 1
                if resto == 0:
                        resto0 = True
        if resto0:
                print("não primo")
        else:print("primo")

    
