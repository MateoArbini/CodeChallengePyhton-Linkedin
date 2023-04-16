# Recibe una lista de elementos
# Retorna una nueva lista unicamente con los elementos repetidos de la lista recibida
# En caso de que la lista inicial no tenga elementos repetidos, la funcion debera retornar una lista vacia

def encontrar_duplicados(lista):
    new_list = []
    ocur = 0
    if len(lista) == 0:
        return new_list
    else:
        for x in lista:
            ocur = lista.count(x)
            if ocur > 1 and x not in new_list:
                new_list.append(x)
                ocur = 0
            else:
                continue
    return new_list


print(encontrar_duplicados(["ana", "paco", "paco", "emilio", "javier", "ana"]))
