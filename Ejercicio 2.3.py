import os

def clasificar_angulo(x, y):
    # Verificación de errores según los requisitos
    if not (isinstance(x, int) and isinstance(y, int)):
        return "error"
    if (x == 0 and y == 0) or y < 0:
        return "error"
    if x == 0 and y > 0:
        return "error"
    
    # Clasificación del ángulo
    if x > 0 and y > 0:
        return "agudo"  # Ángulo agudo (0° < ángulo < 90°)
    elif x > 0 and y == 0:
        return "recto"  # Ángulo recto (90°)
    elif x < 0 and y > 0:
        return "obtuso"  # Ángulo obtuso (90° < ángulo < 180°)
    
    return "error"

# Casos de prueba
casos_de_prueba = [
    {"entrada": (1, 2), "esperado": "agudo"},
    {"entrada": (1, 0), "esperado": "recto"},
    {"entrada": (-1, 2), "esperado": "obtuso"},
    {"entrada": (0, 1), "esperado": "error"},
    {"entrada": (0, 0), "esperado": "error"},
    {"entrada": (1, -1), "esperado": "error"},
    {"entrada": (1.5, 2), "esperado": "error"},
    {"entrada": (0, 2), "esperado": "error"}
]

# Ejecución de las pruebas
os.system('cls')
for i, caso in enumerate(casos_de_prueba, 1):
    entrada = caso["entrada"]
    esperado = caso["esperado"]
    resultado = clasificar_angulo(*entrada)
    print(f"Prueba {i}: Entrada {entrada} -> Resultado: {resultado} (Esperado: {esperado}) - {'Éxito' if resultado == esperado else 'Fallo'}")
