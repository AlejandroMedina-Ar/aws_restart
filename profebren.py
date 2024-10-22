# Definir la cantidad de bananas
bananas = 0  # Puedes cambiar este número para probar diferentes resultados


# Evaluar las condiciones
if bananas >= 5:
    print("Tengo un montón de bananas (I have a large bunch of bananas).")
elif 1 <= bananas <= 4:
    print("Tengo algunas bananas (I have a small bunch of bananas).")
else:
    print("No tengo bananas (I don't have any bananas).")


# Definir la cantidad de bananas
bananas = 5  # Puedes cambiar este número para probar diferentes resultados


while bananas >0:
    if bananas >=5:
        print("Tengo un montón de bananas (I have a large bunch of bananas).")
    elif 1 <= bananas <= 4:
        print("Tengo algunas bananas (I have a small bunch of bananas).")


    bananas -= 1 #disminuye en uno el numero de bananas
if bananas == 0:
    print('No tenemos bananas')

    # Definir la cantidad de bananas
bananas = 0  # Puedes cambiar este número para probar diferentes resultados


# Evaluar las condiciones
if bananas >= 5:
    print("Tengo un montón de bananas (I have a large bunch of bananas).")
elif 1 <= bananas <= 4:
    print("Tengo algunas bananas (I have a small bunch of bananas).")
else:
    print("No tengo bananas (I don't have any bananas).")

# Crear una lista con diferentes tipos de datos
mi_lista = ['Brenda', 30, True, 2, ['Chocolate', 'Caramelos', 'Cheesecake']]
print(mi_lista)
# Imprimir la lista
for elemento in mi_lista:
    print(elemento)
    
    mi_diccionario = {
    'nombre': 'Brenda',
    'edad': 30,
    'ciudad': 'mendoza',
    'trabajo': 'QA'
}
print('Diccionario:', mi_diccionario)
print('La ciudad donde vive:', mi_diccionario['nombre'], 'es:', mi_diccionario['ciudad'])

import math


x= -7.25
valorAbsoluto = math.fabs(x)
print(f'El valor absoluto de {x} es: {valorAbsoluto}')


y=3.9
enteroFloor=math.floor(y)
print(f'El entero mas cercano de {y} es: {enteroFloor}')


print(f'Usando la funcion fabs de {x}, obtuvimos el valor valor absoluto {valorAbsoluto}')
print(f'Aplicando la funcion floor a {y} obtuvimos el entero {enteroFloor}')