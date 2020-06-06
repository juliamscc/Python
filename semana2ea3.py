numero=int(input("Digite um número inteiro: "))

a=numero%100
b=numero%10
c=a-b
dezena=c//10

print("O dígito das dezenas é",dezena)
