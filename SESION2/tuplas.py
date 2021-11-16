# Creando una tupla vacia
t1 = ()
t2 = tuple()


# Tupla de un elemento

t3 = (1, )  # Sin la coma no se detecta como tupla

# Asignacion multiple con tupla

a, b = (10, 20)

#No se puede modificar una tupla, quitar comentarios para comprobar

t1.insert(0, 1)
t1.append(10)

a = t3[0]

l1 = list(t3)