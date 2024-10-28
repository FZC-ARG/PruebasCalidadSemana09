import os
# Diccionario de palabras prohibidas
palabras_prohibidas = {"user%10", "us3r%aa"}

def es_clave_valida(clave):
    # Verificación de longitud
    if len(clave) < 5 or len(clave) > 7:
        return False
    
    # Verificación de caracteres permitidos y restricciones
    if not (clave[0].isalpha() and clave[-1].isalpha()):
        return False
    
    # Contar tipos de caracteres
    tiene_digito = any(c.isdigit() for c in clave)
    alfabéticos = sum(1 for c in clave if c.isalpha())
    caracteres_validos = all(c.isalnum() or c in {'%', '#'} for c in clave)
    
    # Verificación de diccionario de palabras prohibidas
    if clave in palabras_prohibidas:
        return False
    
    # Validación final
    return caracteres_validos and tiene_digito and alfabéticos >= 2

# Casos de prueba
casos_de_prueba = [
    {"entrada": "a1B#cd", "esperado": True},
    {"entrada": "Abc%123", "esperado": True},
    {"entrada": "a2B#", "esperado": True},
    {"entrada": "Abc123#", "esperado": True},
    {"entrada": "a1B#", "esperado": False},
    {"entrada": "a1B#cdefg", "esperado": False},
    {"entrada": "abcdefg", "esperado": False},
    {"entrada": "a1%23", "esperado": False},
    {"entrada": "abc%def", "esperado": False},
    {"entrada": "1abc%de", "esperado": False},
    {"entrada": "abc%de1", "esperado": False},
    {"entrada": "abc*123", "esperado": False},
    {"entrada": "user%10", "esperado": False},
    {"entrada": "us3r%aa", "esperado": False}
]

# Ejecución de las pruebas
os.system('cls')
for i, caso in enumerate(casos_de_prueba, 1):
    entrada = caso["entrada"]
    esperado = caso["esperado"]
    resultado = es_clave_valida(entrada)
    print(f"Prueba {i}: Entrada '{entrada}' -> Resultado: {resultado} (Esperado: {esperado}) - {'Éxito' if resultado == esperado else 'Fallo'}")
