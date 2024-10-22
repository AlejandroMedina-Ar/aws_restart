"""
Lab 141 - Medina, Alejandro
"""

# Determinamos si el número es primo:
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Lista para almacenar los números primos:
primos = []

# Abrir el archivo en modo escritura y almacenamos los números primos:
with open("results.txt", "w") as archivo:
    for num in range(1, 251):
        if es_primo(num):
            primos.append(num)
            archivo.write(str(num) + "\n")

print("Números primos entre 1 y 250:")
# Imprimir los números primos por consola:
for primo in primos:
    print(primo) 