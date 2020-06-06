def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", mínima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), "C.")

def mínima(temps):
    min = temps[0]
    i  = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def máxima(temps):
    max = temps[0]
    i  = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max





def teste_pontualMin(temp, valor_esperado):
    valor_calculado = mínima(temp)
    if valor_calculado != valor_esperado:
        print("Valor esperado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)
        
def testa_mínima():
    print("Iniciando os testes")
    teste_pontualMin([0],0)
    teste_pontualMin([0,0,0,0,0,0,0],0)
    teste_pontualMin([0,1,2,3,4,5,6,7,8,9,10],0)
    teste_pontualMin([30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,22,23,25,25,28,28,32,32,31,29,28,31,33],22)
    teste_pontualMin([-15,-12,20,30],-15)
    print("Finalizando os testes")

def teste_pontualMax(temp, valor_esperado):
    valor_calculado = máxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor esperado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)

def testa_máxima():
    print("Iniciando os testes")
    teste_pontualMax([0],0)
    teste_pontualMax([0,0,0,0,0,0,0],0)
    teste_pontualMax([0,1,2,3,4,5,6,7,8,9,10],10)
    teste_pontualMax([30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,22,23,25,25,28,28,32,32,31,29,28,31,33],33)
    teste_pontualMax([-15,-12,20,30],30)
    teste_pontualMax([-20, -4, -17, -15, -15], -4)
    print("Finalizando os testes")

    
