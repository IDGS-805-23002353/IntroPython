import os

x=0
tem=''
res = 0
a=int(input("Dame un numero: "))
b=int(input("numero base: "))

while x<b:
    
    res = res+a
    tem += str(a)
    if x < b - 1:
        tem += "+"
    x += 1
    
os.system('cls')
print("Resultado de multiplicación: "+tem +"= {}".format(res))





'''
practica1.py
operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3=12

'''
    
   