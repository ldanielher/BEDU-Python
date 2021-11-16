# Formas de declarar una lista vacia
lista_vacia = [] #Dentro de los corchetes se especifican los datos
lista_vacia2 = list() #Usando La función list


#Las listas pueden inicializarse con datos
lista_int = [1, 2, 3, 4, 5]
lista_fl = [1.4, 3.1415, 2.12, 12.7, 0.22]
lista_str = ['hola','mundo','!']
print(lista_fl)

# Las listas pueden contener datos de distinto tipo
lista_mix = [1, 1.4, "hola"]

# O incluso otras listas
listas = [lista_int,lista_str,lista_fl]

#Operaciones con listas
numeros = [1,2,3,4,5]

#Acceso por indice
dato = numeros[2]
#Obtener porciones de lista
sublista = numeros[1:3]

#Agregar elementos a la lista
numeros.append(100)

#Insertar numeros en la lista
numeros.insert(2,'python') 

#Tomar elementos de lista
dato = numeros.pop(2)

#Convertir a lista una cadena
l3 = list("abc123")
print (l3)