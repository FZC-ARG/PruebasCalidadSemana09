import os
def invertir_numero(n):
    
    if isinstance(n, int) and n > 0:
        num_str = str(n)
        if 2 <= len(num_str) <= 9:
            return int(num_str[::-1])
        else:
            return "error"
    else:
        return "error"

def main():
    
    os.system('cls')
    entrada = input("Introduce un número de 2 a 9 cifras: ")
    
    if entrada.isdigit():  # Verifica que la entrada es un número entero positivo
        numero = int(entrada)
        resultado = invertir_numero(numero)
    else:
        resultado = "error"

    print(f"El resultado es: {resultado}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
