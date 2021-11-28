# Solicitar datos
a = input("Escriba el número 1: ")
b = input("Escriba el número 2: ")
oper = input("Selecciona la operación a realizar +, -, *, /: ")
a: int = int(a)
b: int = int(b)

# Operar según opción escogida
error: int = 0

if oper == "+": 
	resultado = a+b
elif oper == "-":
	resultado = a-b
elif oper == "*":
	resultado = a*b
elif oper == "/": 
	if(b==0):
		error = 1
	else:
		resultado = a/b
else: #error
	error = 2

# Devolver resultados
if error == 1:
	mensaje = "No se puede dividir entre cero"	
elif error == 2:
	mensaje = "Elegiste una opción incorrecta"
else:
	mensaje = f"El resultado de {a} {oper} {b} es de {resultado}"

print(mensaje)
