a = 25
b = -1

try:
	print(a**b)
except ZeroDivisionError:
	print("No es posble dividir entre cero")