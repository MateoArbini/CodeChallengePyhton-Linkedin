# Desafio 2
# Crear una función que reciba una cadena de texto
# Retorne el primer caracter que aparezca en la cadena de texto mas de una vez
# NO PUEDE RETORNAR UN ESPACIO VACIO COMO EL PRIMER CARACTER REPETIDO
# En caso de no haber caracteres repetidos la funcion debera retornar None

def primera_letra_repetida(texto):
    # Aca le sacamos los espacios al texto dado, para evitar que el mismo interfiera
    texto_sin_espacios = texto.replace(" ", "")
    texto_sin_espacios = texto_sin_espacios.lower()
    for x in texto_sin_espacios:
        ocur = 0
# Count - metodo que cuenta las ocurrencias de un caracter en un string
        ocur = texto_sin_espacios.count(x)
# La condición es mayor a uno porque siempre va a haber una letra en el string, la cuestion es que haya al menos dos
        if ocur > 1:
            return x
    return None


print(primera_letra_repetida("hola"))
print(primera_letra_repetida("hola mundo"))
