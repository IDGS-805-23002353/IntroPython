def funcion1():
    print("Hola mundo")
    
def funcion2(a, b):
    suma=a+b
    print("La suma de {} + {} = {}".format(a,b,suma))
    
def funcion3(a, b):
    return a+b

def main():
    funcion1()
    funcion2(2, 4)
    resultado = funcion3(2,4)
    print("El resultado de la funcion3 es: {}".format(resultado))

if __name__== "__main__":
    main()
    
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
    
