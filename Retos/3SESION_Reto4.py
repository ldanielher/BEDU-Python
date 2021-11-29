import os
from datetime import datetime

tamaño = os.path.getsize('Readme.md')
fecha = os.path.getmtime('Readme.md')

print(f'El tamaño del archivo Readme-md es: {tamaño} bytes y se modificó por última vez el día {fecha}')