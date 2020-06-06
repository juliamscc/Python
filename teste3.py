cartao = int(input("Digite o número do seu cartão de crédito"))
cartaoLido = 1
meuCartao= False

while cartaoLido != 0 and not meuCartao:
    cartaoLido= int(input("Digite o número do próximo cartão de crédito"))
    if cartaoLido == meuCartao:
        meuCartao = True

if meuCartao:
    print("Seu cartão está na lista.")
else:
    print("Seu cartão não está na lista.")
