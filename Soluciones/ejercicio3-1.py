# Ordenar una lista de numeros enteros de menor a mayor usando el algoritmo de "ordenamiento burbuja"
# Este ordenamiento, consta de revisar cada elemento de la lista y compararlo con el siguiente
# Elementos comparados cambian su posicion si estan en el orden incorrecto
# Revisar la lista todas las veces que sea necesario hasta garantizar que todos los elementos estan en el orden correcto.

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


print(ordenamiento_burbuja([3, 8, 4, 1, 2]))
