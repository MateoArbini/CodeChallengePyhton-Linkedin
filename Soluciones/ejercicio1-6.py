# Crear una funcion que revise una cadena de caracteres que solamente va a contener parentesis
# Return: La funcion debe retornar True si los parentesis estan bien balanceados, o False de lo contrario.

def parentesis_balanceados(texto):
    cantidad_signo_apertura = 0
    cantidad_signo_clausura = 0
    if texto[0] == ")":
        return False
    else:
        for x in texto:
            if x == "(":
                cantidad_signo_apertura += 1
            else:
                cantidad_signo_clausura += 1

    if cantidad_signo_clausura == cantidad_signo_apertura:
        return True
    else:
        return False


print(parentesis_balanceados("((()))()"))
print(parentesis_balanceados(")(()"))
print(parentesis_balanceados("(()"))
