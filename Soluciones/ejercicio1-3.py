# Crear una función que reciba una cadena de texto que contenga la hora en formato de 12 hs
# Ejemplo: Horas:Minutos AM/PM
# Return: La funcion retornara una cadena de texto con la hora formato 24 horas
# Ejemplo de resultado: Horas:Minutos

def convertir_horario(hora):
    # formatear los datos
    data = hora.lower()  # paso a minusculas
    horas = int(data[0] + data[1])  # horas en int

    minutos = data[3] + data[4]  # minutos en int
    tarde_mañana = data[-2] + data[-1]  # am o pm

    if tarde_mañana == "am":
        if horas < 12:
            horafinal = "{}:{}".format(horas, str(minutos))
            return horafinal
        else:
            horafinal = "00:{}".format(str(minutos))
            return horafinal
    else:
        if horas == 12:
            horafinal = "{}:{}".format(horas, str(minutos))
            return horafinal
        else:
            hora_tarde = horas + 12
            horafinal = "{}:{}".format(hora_tarde, str(minutos))
            return horafinal


print(convertir_horario("12:01am"))
print(convertir_horario("11:59AM"))
print(convertir_horario("12:40AM"))
print(convertir_horario("04:59pm"))
print(convertir_horario("10:00:00PM"))
print(convertir_horario("01:01:00PM"))
