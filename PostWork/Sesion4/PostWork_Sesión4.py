import tarjetacredito 
import usuario 

usuario1 = usuario.Usuario("Daniel")
print(usuario1.nombre)

usuario1.agregar_tarjeta()
print(f'{usuario1.nombre}: {usuario1.tarjetas}')
usuario1.borrar_tarjeta("Visa")
print(f'{usuario1.nombre}: {usuario1.tarjetas}')
