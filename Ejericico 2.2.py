import os
def validar_hora(hora):
   
    try:
        partes = hora.split(":")
        
        if len(partes) != 2:
            return "error"
        
        horas = int(partes[0])
        minutos = int(partes[1])
        
        if 0 <= horas <= 23 and 0 <= minutos <= 59:
            return "Hora correcta"
        else:
            return "error"
    except ValueError:
        return "error"

# Pruebas
os.system('cls')
print(validar_hora("00:00"))  # Hora correcta
print(validar_hora("23:59"))  # Hora correcta
print(validar_hora("24:00"))  # error
print(validar_hora("12:60"))  # error
print(validar_hora("hh:mm"))  # error
print(validar_hora("12.30"))  # error
print(validar_hora("12:"))    # error
