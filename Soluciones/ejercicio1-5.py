# Desafio: Crear una funcion que reciba una cadena de texto y retorne la misma en forma de slug
# En esa cadena, no pueden haber caracteres que no sean alfanumericos
# Todos los espacios en la cadena de texto deben ser separados por un guion
# Solo se puede usar la libreria re si es necesario

def slugify(texto):
    texto_min = texto.lower()
    slug = ""
    abecedario_min = "abcdefghijklmnñopqrstuvwxyz"
    list_letras_abc_min = list(abecedario_min)

    for x in texto_min:
        if x not in list_letras_abc_min and x != " ":
            continue
        else:
            slug += x

    slugify_final = slug.replace(" ", "-")
    return slugify_final


print(slugify("texto$% con caracteres/& especial-es"))
print(slugify("Este es un ejemplo!!!"))
