zodiaco = {
    "Aries": ["Sagitario", "Leo", "Acuario"],
    "Tauro": ["Cáncer", "Libra", "Virgo"],
    "Géminis": ["Leo", "Libra", "Géminis", "Capricornio", "Sagitario"],
}

# lee un signo desde el usuario
signo = input("Ingresa un signo zodiacal: ")

# obten signos compatibles
if signo in zodiaco.keys():
    resultado = ",".join(zodiaco[signo])
else:
    resultado = "Error: Signo no encontrado!"
print(f"Signos compatibles: {resultado}")

# genera una cadena con todos los signos
signos = zodiaco.values()

# imprime el resultado
print( signos) 