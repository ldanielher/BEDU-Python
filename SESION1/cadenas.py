#Esto es una cadena                                                                                            
d = "Hola mundo"                                                

# Podemos comprobar el dato con type(), en inglés se les conoce como string                                                                                                                                              
print(type(d))

# Podemos utilizar comillas simples, o tres comillas dobles                                                                                                                         
e = 'Saludos'
f = """What's your name?"""

#Las cadenas pueden tener unicamente 1 caracter, o incluso 0
un_caracter = 'a'
print(type(un_caracter))

cadena_vacia = ''
print(type(cadena_vacia))

# Operaciones con cadenas
print("Hola" * 5) #'* Repite la misma cadena n-veces'
print("Hola" + " Mundo") #'+ concatena cadenas'

#Format sirve para añadir variables dentro de una cadena durante la ejecución
nombre = "Luis"  
print("Hola, mi nombre es {}".format(nombre)) #'Hola!, mi nombre es Luis'

#Incluso se pueden agregar variables que no son cadenas
edad = 28
print("Tengo {} años".format(edad))

#O se pueden agregar multiples datos
print("{} + {} = {}".format(4, 5, 4+5))  #4 + 5 = 9

# Añadir variables dentro de una cadena durante la ejecución
nombre = "Luis"  
print( f"Hola, mi nombre es {nombre}" )

# Incluso se pueden agregar variables que no son cadenas
edad = 28
print( f"Tengo {edad} años" )

# O se pueden agregar multiples datos
print(f"{4} + {5} = {4+5}")