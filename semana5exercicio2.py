def primo_true(x):
    resto0 = False
    resto = 1
    aux = x - 1
    while aux > 1 and not resto0:
        resto = x % aux
        aux = aux - 1
        if resto == 0:
            resto0 = True
    if not resto0:
        return x
    else:
        return 0
    

def maior_primo(n):
    while n >= 2:
        if primo_true(n) == 0:
            n = n - 1
        else:
            return n
        
    
