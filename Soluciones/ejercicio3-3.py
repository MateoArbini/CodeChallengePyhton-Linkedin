# Listas anidadas son aquellas listas que se encuentran dentro de otras listas
# Convertir una lista anidada de dos dimensiones a una lista unidimensional. (Flatten a list)
# Recibir una lista anidada de dos dimensiones
# Retornar una nueva lista de una sola dimension
# Debe contener todos los elementos de la lista exterior y la lista anidada
# En el mismo orden

#Funcion que aplica para listas bidimensionales
def aplanar_lista(lista):
    new_list = []
    for x in lista:
        if type(x) != list:
            new_list.append(x)
        else:
            for j in x:
                new_list.append(j)

    return new_list


print(aplanar_lista([2, 3, 4, [3, 2]]))
print(aplanar_lista([2, 3, 4, [[2]]]))
