import tarjetacredito as tc

class Usuario():
    """ Clase que genera un objeto tipo Usuario """
    def __init__(self, nombre: str):
        """ Crea un objeto Usuario a partir de un nombre """
        self.nombre = nombre
        self.tarjetas = []

    # def __del__(self):
    #     print(f'Usuario {self.__nombre} dado de baja!')

    def agregar_tarjeta(self):
        tarjeta1 = tc.TarjetaCredito()
        self.tarjetas.append(tarjeta1.datos)
        
    def borrar_tarjeta(self, nombre):
        indice = 0
        flag_busqueda = 0
        for i in self.tarjetas:
            if i['nombre'] == nombre:
                del self.tarjetas[indice]
                flag_busqueda = 1
                print(f'\nTarjeta {nombre} dada de baja!')
            indice +=1
        
        if flag_busqueda == 0: 
            print(f'\nTarjeta {nombre} no encontrada!')
    
    def get_nombre(self):
        return Usuario.nombre
        


    