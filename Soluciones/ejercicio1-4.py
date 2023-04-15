# Fucion que determine si dos palabras son anagramas (contienen las mismas letras, sin importar el orden)
# Retorno: Debe retornar True si lo son y False en caso de que no lo sea
# No debe haber distincion entre mayusculas o minusculas

def es_anagrama(palabra1, palabra2):
    palabra1_min = palabra1.lower()
    palabra2_min = palabra2.lower()
    lista_letras_1 = list(palabra1_min)
    lista_letras_2 = list(palabra2_min)

    for x in lista_letras_1:
        if x in lista_letras_2:
            continue
        else:
            return False
    return True


print(es_anagrama("lama", "Mala"))
print(es_anagrama("calor", "coral"))
print(es_anagrama("cama", "casa"))
