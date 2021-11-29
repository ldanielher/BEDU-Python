# Solicitar los dos números
print("Programa para encontrar el mínimo común múltiplo de dos números")
num1 = input("Ingrese el primer número: ")
num1: int = int(num1)
num2 = input("Ingrese el segundo número: ")
num2: int = int(num2)

# Encontrar el mayor
if num1 > num2: 
	mayor = num1
else: 
	mayor = num2

# Incrementar el número desde el mayor
mcm = mayor
while (mcm % num1 != 0) or (mcm % num2 != 0):
	mcm += 1

# Imprime el mcm
print(f"El mínimo comun multiplo es: {mcm}")