import math
from math import gcd as mcd

# Usando funciones de math
numero = input("Ingrese un número: ")
numero: int = int(numero)
factorial = math.factorial(numero)
raiz = math.sqrt(numero)

# Imprime resultados
print(f"El factorial del número es: {factorial}")
print(f"La raíz cuadrada del número es: {raiz}")

# Usando Máximo común divisor de math
print("\nVamos a hallar el Máximo común divisor de dos números")

numero1 = input("Ingrese el primer número: ")
numero1: int = int(numero1)
numero2 = input("Ingrese el segundo número: ")
numero2: int = int(numero2)
respuesta = mcd(numero1, numero2) 

# Imprime resultados
print(f'El Máximo común divisor es {respuesta}')