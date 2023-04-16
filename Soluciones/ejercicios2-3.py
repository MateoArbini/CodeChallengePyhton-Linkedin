#Un numero triangular es un numero que resulta de haber sumado numeros naturales sucesivos
#Pueden representarse como conjunto de puntos de manera que forman un triangulo equilatero
#En la primera fila un solo punto
#Representa el numero 1
#Cada fila siguiente contiene la cantidad de puntos del siguiente numero natural
#Para obtener cada numero triangular debemos sumar la cantidad de puntos desde la punta hasta alguna de las filas del triangulo
#Crear una funcion que reciba el numero de la fila del triangulo de puntos
#Calcular el numero triangular correspondiente a la fila
#Ex. Si la fila es 3, la funcion debera retornar 6, si la fila es 4, debera retornar 10

def numero_triangular(fila):
    resultado = 0
    for x in range(1,fila+1):
        resultado+=x
    
    return resultado

print(numero_triangular(1))
print(numero_triangular(2))
print(numero_triangular(3))
print(numero_triangular(4))
print(numero_triangular(5))
print(numero_triangular(6))