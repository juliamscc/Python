x1= float(input("Digite um número para x: "))
y1= float(input("Digite um número para y: "))
x2= float(input("Digite um número para x': "))
y2= float(input("Digite um número para y': "))

import math
distancia= math.sqrt((x1-x2)**2+(y1-y2)**2)

if distancia>=10:
    print("longe")
else:
    print("perto")
