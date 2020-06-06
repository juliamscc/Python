def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", mínima(temperaturas), "C.")
    print("A maior temperatura do mês foi: ", máxima(temperaturas), "C.")

def mínima(temps):
    t = sorted(temps)
    return t[0]

def máxima(temps):
    t = sorted(temps)
    return t[-1]
