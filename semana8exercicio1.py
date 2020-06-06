def remove_repetidos(l):
    lista = sorted(l)
    lista2 = [lista[0]]
    x = 1
    while x < len(lista):
        if lista[x] != lista[x-1]:
            lista2.append(lista[x])
        x = x + 1
    return lista2
