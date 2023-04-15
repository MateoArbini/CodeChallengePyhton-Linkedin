# Crear una funcion que permita identificar si un numero entero positivo es primo
# Return: Si es primo, retorna True, de lo contrario retorna False
# Un numero primo es aquel que solo es divisible entre 1 y el mismo numero.
# El numero 1 NO es primo, y en caso de que la funcion reciba este, se debe retornar False.

def es_numero_primo(numero):
    # Con este checker, corroboro las iteraciones del for y los resultados de las operaciones
    # Arranca en dos, porque el numero siempre va a ser divisible entre 1 y el mismo numero
    checker = 2
    if numero == 1:
        # Si el numero dado es uno, por convencion no es primo
        return False
    elif numero == 2:
        # Para esta funcion, con esta condicion descartamos el caso del 2
        return True
    else:
        lista_divisores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for x in lista_divisores:
            if x != numero:
                res_div = numero / x
                # Si no hay resto en la division, y esa opracion no es entre uno o el mismo numero, el numero en cuestion ya no es primo
                if res_div % 2 == 0:
                    checker += 1
            else:
                continue
    # Corroboramos si el numero es primo o no a traves del valor del checker.
    # Si es mayor a dos, no es primo, ya que la division con otro numero dio como resultado un numero entero, de lo contrario es primo.
    if checker == 2:
        return True
    else:
        return False


print(es_numero_primo(2))
print(es_numero_primo(3))
print(es_numero_primo(5))
print(es_numero_primo(6))
print(es_numero_primo(7))
print(es_numero_primo(12))
print(es_numero_primo(13))
print(es_numero_primo(17))
print(es_numero_primo(19))
print(es_numero_primo(23))
print(es_numero_primo(29))
print(es_numero_primo(97))
print(es_numero_primo(103))
print(es_numero_primo(107))
print(es_numero_primo(108))
