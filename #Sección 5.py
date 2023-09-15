#Sección 5
#Crear una función que compruebe si un número es bisiesto y llamarla enviandole un año
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    anio = 2023 #Puedes cambiar el año aquí
    if es_bisiesto(anio):
        printi(f"{anio} es bisiesto")
    else:
        print(f"{anio} no es bisiesto")


#Hacer el mismo ejemplo pero con una variavle global en la que se guarde el año. 
#Luego llamar a la función sin enviarle ningún parámetro
ANIO = 2000
def es_bisiesto():
    global ANIO
    if ANIO % 4 == 0:
        if ANIO % 100 == 0:
             if ANIO % 400 == 0: 
                 return True
             else: 
                 return False
        else:
            return True
    else:
        return False
#Ejemplo de llamada a la función
if es_bisiesto():
    print(f"(ANIO) es bisiesto")


#Calcular el factorial de un número desde una función a la que le envías el número como parámetro sin usar recursividad:
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
        return resultado
    

#Calcular el factorial de un numero usando recursividad
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)
    
#Muestra los n primeros números de la serie de Fibonacci usando recursividad
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    def imprimir_fibonacci(n):
        for i in range(n):
            print(fibonacci(1))
#Ejemplo de llamada a la función
imprimir_fibonacci(10)