def es_palindrome(texto):
    # Primero se pasa todo el texto a minuscula
    # Luego se quitan los espacios
    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    copy_texto_sin_espacios = texto_sin_espacios[::-1]
    if copy_texto_sin_espacios == texto_sin_espacios:
        return True
    else:
        return False


print(es_palindrome("Anita lava la tina"))  # True
print(es_palindrome("palindromo"))  # False
