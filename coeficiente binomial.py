def fatorial(n):
        if n >= 0:
                a = 1
                while n > 1:
                        a = a * n
                        n = n - 1
                return a
        else:
                n = n * (-1)
                a = 1
                while n > 1:
                    a = a * n
                    n = n - 1
                return a * (-1)

def numero_binomial(n,p):
    return fatorial(n) // (fatorial(p) * fatorial(n - p))



