# Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print( type(numero1), type(numero1) )

# Para convertir a entero 
entero = int(numero1)
print( type(entero) )

# Para convertir a flotante
flotante = float(numero2)
print( type(flotante) )

num = 300
cadena = str(num)
print(type(cadena))

# Leyendo una cadena
nombre = input("Dame tu nombre: ")
print( nombre, type(nombre) )

# Leyendo un entero
edad = int( input("Dame tu edad: ") )
print( edad, type(edad) )