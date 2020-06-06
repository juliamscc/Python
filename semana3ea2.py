a= float(input("Digite o valor de A: "))
b= float(input("Digite o valor de B: "))
c= float(input("Digite o valor de C: "))

delta= b**2-4*a*c
if delta==0:
    raizD0= (-b)/(2*a)
    print("a raiz desta equação é",raizD0)
else:
    if delta<0:
     print("esta equação não possui raízes reais")
    else:
     rdelta= int(delta**(1/2))
     raiz1= (-b+rdelta)/(2*a)
     raiz2= (-b-rdelta)/(2*a)
     if raiz1>raiz2:
         print("as raízes da equação são",raiz2,"e",raiz1)
     else:
         print("as raízes da equação são",raiz1,"e",raiz2)
