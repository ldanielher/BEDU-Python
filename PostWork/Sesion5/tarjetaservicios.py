from tarjeta import Tarjeta

class Tarjeta_de_servicios(Tarjeta):
    """ Clase que genera un objeto tipo Tarjeta de Servicios """

    def __init__(self):
        """ Crea un objeto TServicios a partir de un diccionario con datos iniciales """
        self.datos = self.crea_tarjeta()
        self.datos['deuda_recalculada'] = 0
        self.datos['nueva_deuda'] = 0

    def crea_tarjeta(self):
        """ Recoge los datos de la tarjeta """
        nombre_tc = input("Nombre de la tarjeta: ")
        deuda = input("Escribe el monto de la deuda actual de la tarjeta: ")
        deuda = float(deuda)
        pago = input("Ingresa el pago a realizar (solo se acepta un pago igual a la deuda): ")
        pago = float(pago)

        if pago != deuda: #Si el pago es diferente a la deuda vuelve a solicitar datos
            print('El pago debe ser igual a la deuda actual!')
            self.crea_tarjeta()
        else:	
            nuevos_cargos = input("Ingresa los nuevos cargos: ")
            nuevos_cargos = float(nuevos_cargos)
            print()

            #Crear diccionario y agregar datos
            tarjeta = dict()
            tarjeta['nombre'] = nombre_tc
            tarjeta['deuda'] = deuda
            tarjeta['pago'] = pago
            tarjeta['cargos'] = nuevos_cargos
            return tarjeta		
    
    def captura_nueva_deuda(self):
        """ Captura los datos de una tarjeta e inserta los Calculos en el diccionario """ 
        deuda = float(self.datos['deuda'])
        pago = float(self.datos['pago'])
        nuevos_cargos =	float(self.datos['cargos'])

        deuda_recalculada = (deuda - pago) 
        self.datos['deuda_recalculada'] = deuda_recalculada
        nueva_deuda = deuda_recalculada + nuevos_cargos
        self.datos['nueva_deuda'] = nueva_deuda		

    def generar_reporte(self):
        """ Imprimir datos de la tarjeta """
        print("\n-----------------------------------------")
        print("-------- Tarjeta de Servicios -----------")
        print("-----------------------------------------")
        print(f"Tarjeta:    {self.datos['nombre']}")
        print("-----------------------------------------")
        print(f"Deuda actual:              {round(self.datos['deuda'],2)}")
        print(f"Monto del pago:            {round(self.datos['pago'],2)}")
        print("-----------------------------------------")
        print(f"Deuda recalculada:         {round(self.datos['deuda_recalculada'],2)}")
        print(f"Nuevos cargos del mes:     {round(self.datos['cargos'],2)}")
        print("-----------------------------------------")
        print(f"Nueva deuda del mes:       {round(self.datos['nueva_deuda'],2)} \n")	
