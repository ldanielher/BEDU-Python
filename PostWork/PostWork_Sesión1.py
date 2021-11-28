# Solicitar datos
nombre_tc = input("Nombre de la tarjeta: ")
tasa = input("Tasa de interés anual de la tarjeta (%): ")
tasa = float(tasa)
deuda = input("Escribe el monto de la deuda actual de la tarjeta: ")
deuda = float(deuda)
pago = input("Ingresa el pago a realizar: ")
pago = float(pago)

if pago > deuda:
	print('No es posible realizar un pago mayor a la deuda!')
else:	
	nuevos_cargos = input("Ingresa los nuevos cargos: ")
	nuevos_cargos = float(nuevos_cargos)
	""" Cálculos"""
	int_mensual = (tasa/12)/100
	deuda_pago = deuda - pago
	intereses_mes = deuda_pago * int_mensual
	deuda_recalculada = (deuda - pago) * (1 + int_mensual)
	nueva_deuda = deuda_recalculada + nuevos_cargos

	""" Imprimir datos """
	print("\nResumen de tarjeta")
	print("-----------------------------------------")
	print(f"Tarjeta a nombre de:    {nombre_tc}")
	print(f"Tasa de interés anual:  {round(tasa,2)}%")
	print("-----------------------------------------")
	print(f"Deuda actual:              {round(deuda,2)}")
	print(f"Monto del pago:            {round(pago,2)}")
	print("-----------------------------------------")
	print(f"Deuda después del pago:    {round(deuda_pago,2)}")
	print(f"Intereses del mes:         {round(intereses_mes,2)}")
	print("-----------------------------------------")
	print(f"Deuda recalculada:         {round(deuda_recalculada,2)}")
	print(f"Nuevos cargos del mes:     {round(nuevos_cargos,2)}")
	print("-----------------------------------------")
	print(f"Nueva deuda del mes:       {round(nueva_deuda,2)}")



