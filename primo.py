def numero_primo(n):
    aux = n - 1
    resto = 1
    resto0 = False
    if n == 1:
        return False
    else:
        while aux > 1 and not resto0:
            resto = n % aux
            aux = aux - 1
            if resto == 0:
                resto0 = True
        if resto0:
            return False
        else:
            return True
