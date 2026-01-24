import os
'''
    practica2.py
    Crear un programa que tenga un menú con las siguientes opciones:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
    
    Cada opcion debe ser una funcion diferente 
    
    Debe limpiar y volver a mostrar el menu
    
    '''
    
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresiona Enter para continuar...")

def suma():
    limpiar()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("La suma de {} + {} = {}".format(a,b, a + b))
    pausa()
    
def resta():
    limpiar()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("La resta de {} - {} = {}".format(a,b, a - b))
    pausa()
    
def multiplicacion():
    limpiar()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print("La multiplicación de {} x {} = {}".format(a,b, a * b))
    pausa()
    
def division():
    limpiar()
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    if b != 0:
        print("La división de {} / {} = {}".format(a,b, a / b))
    else:
        print("Error: no se puede dividir entre cero")
        
    

def main():
    while True:
      limpiar()
      print("\n")
      print("**************************************")
      print("Menú")
      print("**************************************")

      print("1. Suma")
      print("2. Resta")
      print("3. Multiplicación")
      print("4. División")
      print("5. Salir")
      
      opc = input("\nSelecciona una opción: ")

      if opc == "1":
            suma()
      elif opc == "2":
            resta()
      elif opc == "3":
            multiplicacion()
      elif opc == "4":
            division()
      elif opc == "5":
            print("Saliendo del programa...")
            break
      else:
            print("Opción no válida")


if __name__== "__main__":
    main()
    