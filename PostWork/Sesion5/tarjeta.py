class Tarjeta():
	""" Clase que genera un objeto tipo Tarjeta de Crédito """
	def __init__(self):
		""" Crea un objeto TC a partir de un diccionario con datos iniciales """
		self.datos = self.crea_tarjeta()
		self.datos['deuda_pago'] = 0
		self.datos['intereses_mes'] = 0
		self.datos['deuda_recalculada'] = 0
		self.datos['nueva_deuda'] = 0
	
	# def __del__(self):
	# 	nombre = self.datos['nombre']
	# 	print(f'{nombre} dada de baja!')

	def crea_tarjeta(self):
		""" Recoge los datos de la tarjeta """
		nombre_tc = input("Nombre de la tarjeta: ")
		tasa = input("Tasa de interés anual de la tarjeta (%): ")
		tasa = float(tasa)
		deuda = input("Escribe el monto de la deuda actual de la tarjeta: ")
		deuda = float(deuda)
		pago = input("Ingresa el pago a realizar: ")
		pago = float(pago)
		
		if pago > deuda: #Si el pago es mayor a la deuda vuelve a solicitar datos
			print('No es posible realizar un pago mayor a la deuda!')
			self.crea_tarjeta()
		else:	
			nuevos_cargos = input("Ingresa los nuevos cargos: ")
			nuevos_cargos = float(nuevos_cargos)
			print()

			#Crear diccionario y agregar datos
			tarjeta = dict()
			tarjeta['nombre'] = nombre_tc
			tarjeta['tasa'] = tasa
			tarjeta['deuda'] = deuda
			tarjeta['pago'] = pago
			tarjeta['cargos'] = nuevos_cargos
			return tarjeta		        

	def captura_nueva_deuda(self):
		""" Captura los datos de una tarjeta e inserta los Calculos en el diccionario """ 
		tasa = float(self.datos['tasa'])
		deuda = float(self.datos['deuda'])
		pago = float(self.datos['pago'])
		nuevos_cargos =	float(self.datos['cargos'])

		int_mensual = (tasa/12)/100
		deuda_pago = deuda - pago
		self.datos['deuda_pago'] = deuda_pago
		intereses_mes = deuda_pago * int_mensual
		self.datos['intereses_mes'] = intereses_mes
		deuda_recalculada = (deuda - pago) * (1 + int_mensual)
		self.datos['deuda_recalculada'] = deuda_recalculada
		nueva_deuda = deuda_recalculada + nuevos_cargos
		self.datos['nueva_deuda'] = nueva_deuda		


	def generar_reporte(self):
		""" Imprimir datos de la tarjeta """
		print("\nResumen de tarjeta")
		print("-----------------------------------------")
		print(f"Tarjeta a nombre de:    {self.datos['nombre']}")
		print(f"Tasa de interés anual:  {round(self.datos['tasa'],2)}%")
		print("-----------------------------------------")
		print(f"Deuda actual:              {round(self.datos['deuda'],2)}")
		print(f"Monto del pago:            {round(self.datos['pago'],2)}")
		print("-----------------------------------------")
		print(f"Deuda después del pago:    {round(self.datos['deuda_pago'],2)}")
		print(f"Intereses del mes:         {round(self.datos['intereses_mes'],2)}")
		print("-----------------------------------------")
		print(f"Deuda recalculada:         {round(self.datos['deuda_recalculada'],2)}")
		print(f"Nuevos cargos del mes:     {round(self.datos['cargos'],2)}")
		print("-----------------------------------------")
		print(f"Nueva deuda del mes:       {round(self.datos['nueva_deuda'],2)} \n")	


	def imprimir_tarjetas(self, n):
		""" Captura una lista de tarjetas e imprime sus reportes """
		lista_tarjetas = []
		for i in range(n):
			print(f"\nTarjeta {i+1}")
			lista_tarjetas.append( self.crea_tarjeta() )

		for j in lista_tarjetas:
			self.generar_reporte( self.captura_nueva_deuda(j) )


	def pago_recurrente(self):
		""" Genera pagos recurrentes segun el valor de pago ingresado """
		pago = float(self.datos['pago'])
		deuda = float(self.datos['deuda'])
		while pago < deuda:
			self.captura_nueva_deuda()
			self.generar_reporte()
			self.datos['deuda'] = self.datos['nueva_deuda']
			self.datos['cargos'] = 0
			deuda = float(self.datos['deuda'])

		self.datos['pago'] = deuda
		self.captura_nueva_deuda()
		self.generar_reporte()


	def pagos_multiples(self):
		""" Genera pagos multiples ingresando cada pago manualmente """
		# Solicita pagos múltiples
		pago = 1
		pagos = []
		while pago != 0:
			pago = input("Escribe la cantidad del siguiente pago (escribe 0 para terminar): ")
			pago = float(pago)
			if pago != 0:
				pagos.append(pago)

		# Aplica pagos ingresados
		self.datos['cargos'] = 0
		for pago in pagos:	
			self.datos['deuda'] = self.datos['nueva_deuda']
			self.datos['pago'] = pago
			self.captura_nueva_deuda()
			self.generar_reporte()
			
		




