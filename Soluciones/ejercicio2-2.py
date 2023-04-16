# Calcular el factorial de un numero creando tu propia funcion
# El factorial de un numero entero positivo n se define como la multiplicacion de todos los numeros enteros
# desde el 1 hasta el numero n
# Crear una funcion que calcule el factorial usando un ciclo o una funcion recursiva

def calcular_factorial(numero):
    resultado = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero+1):
            resultado *= x
    return resultado


print(calcular_factorial(0))
print(calcular_factorial(1))
print(calcular_factorial(2))
print(calcular_factorial(3))
print(calcular_factorial(4))
print(calcular_factorial(5))
