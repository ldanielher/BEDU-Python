def crea_tarjeta():
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
		crea_tarjeta()
	else:	
		nuevos_cargos = input("Ingresa los nuevos cargos: ")
		nuevos_cargos = float(nuevos_cargos)

		#Crear diccionario y agregar datos
		tarjeta = dict()
		tarjeta['nombre'] = nombre_tc
		tarjeta['tasa'] = tasa
		tarjeta['deuda'] = deuda
		tarjeta['pago'] = pago
		tarjeta['cargos'] = nuevos_cargos
		return tarjeta		

def captura_nueva_deuda(tarjeta_dict):
	""" Captura los datos de una tarjeta e inserta los Cálculos en el diccionario """ 
	tasa = float(tarjeta_dict['tasa'])
	deuda = float(tarjeta_dict['deuda'])
	pago = float(tarjeta_dict['pago'])
	nuevos_cargos =	float(tarjeta_dict['cargos'])

	int_mensual = (tasa/12)/100
	deuda_pago = deuda - pago
	tarjeta_dict['deuda_pago'] = deuda_pago
	intereses_mes = deuda_pago * int_mensual
	tarjeta_dict['intereses_mes'] = intereses_mes
	deuda_recalculada = (deuda - pago) * (1 + int_mensual)
	tarjeta_dict['deuda_recalculada'] = deuda_recalculada
	nueva_deuda = deuda_recalculada + nuevos_cargos
	tarjeta_dict['nueva_deuda'] = nueva_deuda
	return tarjeta_dict

def generar_reporte(tarjeta_dict):
	""" Imprimir datos de la tarjeta """
	print("\nResumen de tarjeta")
	print("-----------------------------------------")
	print(f"Tarjeta a nombre de:    {tarjeta_dict['nombre']}")
	print(f"Tasa de interés anual:  {round(tarjeta_dict['tasa'],2)}%")
	print("-----------------------------------------")
	print(f"Deuda actual:              {round(tarjeta_dict['deuda'],2)}")
	print(f"Monto del pago:            {round(tarjeta_dict['pago'],2)}")
	print("-----------------------------------------")
	print(f"Deuda después del pago:    {round(tarjeta_dict['deuda_pago'],2)}")
	print(f"Intereses del mes:         {round(tarjeta_dict['intereses_mes'],2)}")
	print("-----------------------------------------")
	print(f"Deuda recalculada:         {round(tarjeta_dict['deuda_recalculada'],2)}")
	print(f"Nuevos cargos del mes:     {round(tarjeta_dict['cargos'],2)}")
	print("-----------------------------------------")
	print(f"Nueva deuda del mes:       {round(tarjeta_dict['nueva_deuda'],2)} \n")	

def imprimir_tarjetas(n):
	""" Genera una lista de tarjetas e imprime sus reportes """
	lista_tarjetas = []
	numeros = list(range(n))
	for i in numeros:
		print(f"\nTarjeta {i+1}")
		lista_tarjetas.append( crea_tarjeta() )

	for j in lista_tarjetas:
		generar_reporte( captura_nueva_deuda(j) )

def pago_recurrente(tarjeta_dict):
	""" Genera pagos recurrentes según el valor de pago ingresado """
	pago = float(tarjeta_dict['pago'])
	deuda = float(tarjeta_dict['deuda'])
	while pago < deuda:
		generar_reporte( captura_nueva_deuda( tarjeta_dict ) )
		deuda_nueva =  captura_nueva_deuda( tarjeta_dict )
		tarjeta_dict['deuda'] = deuda_nueva['nueva_deuda']
		deuda = float(tarjeta_dict['deuda'])
		tarjeta_dict['cargos'] = 0

	tarjeta_dict['pago'] = deuda
	generar_reporte( captura_nueva_deuda( tarjeta_dict ) )


tarjeta = crea_tarjeta()
tarjeta_calculos = captura_nueva_deuda(tarjeta)
generar_reporte( tarjeta_calculos )
#imprimir_tarjetas(3)
#pago_recurrente( tarjeta )



