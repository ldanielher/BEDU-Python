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
        tarjeta1.captura_nueva_deuda()
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
    
    def imprimir_tarjetas(self):
        """ Imprime reportes de tarjetas del usuario """
        for i in self.tarjetas:
            """ Imprimir datos de la tarjeta """
            print("\nResumen de tarjeta")
            print("-----------------------------------------")
            print(f"Tarjeta a nombre de:    {i['nombre']}")
            print(f"Tasa de interés anual:  {round(i['tasa'],2)}%")
            print("-----------------------------------------")
            print(f"Deuda actual:              {round(i['deuda'],2)}")
            print(f"Monto del pago:            {round(i['pago'],2)}")
            print("-----------------------------------------")
            print(f"Deuda después del pago:    {round(i['deuda_pago'],2)}")
            print(f"Intereses del mes:         {round(i['intereses_mes'],2)}")
            print("-----------------------------------------")
            print(f"Deuda recalculada:         {round(i['deuda_recalculada'],2)}")
            print(f"Nuevos cargos del mes:     {round(i['cargos'],2)}")
            print("-----------------------------------------")
            print(f"Nueva deuda del mes:       {round(i['nueva_deuda'],2)} \n")	

    def get_nombre(self):
        return Usuario.nombre
        


    