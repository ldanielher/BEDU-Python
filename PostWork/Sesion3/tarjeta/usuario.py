def multiples_reportes(*tarjetas: dict):
    """ Imprime múltiples reportes de tarjetas """
    for tarj in tarjetas:
        """ Imprimir datos de la tarjeta """
        print("\nResumen de tarjeta")
        print("-----------------------------------------")
        print(f"Tarjeta a nombre de:    {tarj['nombre']}")
        print(f"Tasa de interés anual:  {round(tarj['tasa'],2)}%")
        print("-----------------------------------------")
        print(f"Deuda actual:              {round(tarj['deuda'],2)}")
        print(f"Monto del pago:            {round(tarj['pago'],2)}")
        print("-----------------------------------------")
        print(f"Deuda después del pago:    {round(tarj['deuda_pago'],2)}")
        print(f"Intereses del mes:         {round(tarj['intereses_mes'],2)}")
        print("-----------------------------------------")
        print(f"Deuda recalculada:         {round(tarj['deuda_recalculada'],2)}")
        print(f"Nuevos cargos del mes:     {round(tarj['cargos'],2)}")
        print("-----------------------------------------")
        print(f"Nueva deuda del mes:       {round(tarj['nueva_deuda'],2)} \n")	
