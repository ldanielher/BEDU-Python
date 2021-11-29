import tarjetacredito 
import usuario 

# Crear usuario
nombre = input('Ingrese su nombre: ')
usuario1 = usuario.Usuario(nombre)

# Agregar 3 tarjetas
usuario1.agregar_tarjeta()
usuario1.agregar_tarjeta()
usuario1.agregar_tarjeta()

# Elimina la 3er tarjeta
usuario1.borrar_tarjeta("Tarjeta3")

# Imprime las tarjetas del usuario
usuario1.imprimir_tarjetas()
