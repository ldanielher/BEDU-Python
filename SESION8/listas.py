"""
Sesion-02, Reto final: Listas de números:

1. Definir una lista de números
2. Realiza una función que tome como entrada una lista de números
    1. Que ordene la lista de números
    2. Eliminar repeticiones
    3. Que devuelva una lista resultante
3. Almacenar el resultado de la función en una variable
4. Imprimir los valores de la variabel resultante uno a uno
"""

import random

def procesa(lista):
    """ Toma lista de número, la ordena, elimina duplicados y regresa la lista resultante """   
    sin_repeticiones: set = set(lista)              #Quita duplicados
    sin_repeticiones: list = list(sin_repeticiones)
    # sin_repeticiones.sort()
    return sin_repeticiones


lista = [random.randrange(100) for i in range(500)]
print("Lista original con", len(lista), "números")
print(lista)
lista_procesada = procesa(lista)
print("Lista procesada con", len(lista_procesada), "números")
print(lista_procesada)
