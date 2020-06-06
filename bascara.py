def bascara():
    print("Para encontrar o(s) valor(es) de x na equação Ax^2+Bx+C=0")
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    raizes(a,b,c)


def raizes(a,b,c):
    delta= b**2-4*a*c
    if delta==0:
        raizD0= (-b)/(2*a)
        print("O valor de x é",raizD0,".")
    elif delta<0:
             print("Essa equação não possui raíses reais.")
    else:
        raiz1= (-b+(delta**(1/2)))/(2*a)
        raiz2= (-b-(delta**(1/2)))/(2*a)
        if raiz1<raiz2:
            print("Os valores de x são",raiz1,"e",raiz2,".")
        else:
            print("Os valores de x são",raiz2,"e",raiz1,".")
    

    
    
