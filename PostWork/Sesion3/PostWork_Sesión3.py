import tarjeta.tarjeta as tj
import tarjeta.usuario as user

######################
# Caso 1: Captura 3 tarjetas
tarjetas = []
nro_capturas = 3
for i in range(nro_capturas):
    tarjeta = tj.crea_tarjeta()
    tarjetas.append(tarjeta)
    print('')

# Captura cada tarjeta
for tarjeta in tarjetas:
    tarjeta = tj.captura_nueva_deuda(tarjeta)

# Imprime las tarjetas
user.multiples_reportes(*tarjetas)

######################
# Caso 2: Genera pagos recurrentes
tarjeta2 = tj.crea_tarjeta()
tj.pago_recurrente(tarjeta2)

######################
# Caso 3: Proyecta varios pagos distintos
tarjeta3 = tj.crea_tarjeta()
tarjeta3_calc = tj.captura_nueva_deuda(tarjeta3)
tj.generar_reporte(tarjeta3_calc)
tj.pagos_multiples(tarjeta3_calc)
