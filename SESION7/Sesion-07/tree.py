import click
import csv
import os
import time

class Archivo():
    def __init__(self, ruta):
        """ Crea un objeto Archivo a partir de ruta """
        self.__ruta = ruta
        try:
            self.tamanio = os.path.getsize(ruta)
            self.fecha = os.path.getmtime(ruta)
        except FileNotFoundError:
            pass
        except OSError:
            pass

    @property
    def get_ruta(self):
        """ Obtiene el valor de ruta """
        return self.__ruta

    def __str__(self):
        """ Define la represrentación en str de Archivo """
        return self.__ruta

    @property
    def fecha_str(self):
        """ Representación en cadena de el atributo fecha """
        fecha: tuple = time.localtime(self.fecha)
        fecha: str = time.strftime("%d-%m-%Y %H:%M:%S", fecha)
        return fecha

    def texto(self):
        """ Representación en texto plano de un Archivo """
        return f"{self.tamanio:12}  {self.fecha_str:19}  {self.__ruta}"

    @property
    def tupla_str(self):
        """ Representación en tupla de un Archivo con fecha en cadena """
        return (self.tamanio, self.fecha_str, self.get_ruta)


class Carpeta(Archivo):
    def lista_elementos(self):
        """ Obtener la lista de elementos de la Carpeta """
        try:
            archivos: list = os.listdir(self.get_ruta)  # archivos -> ["uno.py", "dos.py", ...]
        except PermissionError:
            archivos = []
        # elementos -> [Archivo("uno.py"), Archivo("dos.py"), Carpeta("datos"), ....]
        elementos = []
        for arch in archivos:
            # arch -> ruta + "uno.py", "datos"
            ruta = os.path.join(self.get_ruta, arch)  # "/home/rcotrr/uno.py"
            if os.path.isdir(ruta):
                carpeta = Carpeta(ruta)
                elementos.append( carpeta )
                # elementos = elementos + Carpeta(ruta).lista_elementos()
                elementos += carpeta.lista_elementos()
                # i = i + 1
                # i += 5
                # i -= 5
                # i *= 2 -> i = i * 2
                # i++ <- No existe en Python
            else:
                elementos.append( Archivo(ruta) )
        return elementos

    def texto(self):
        """ Representación en texto plano de un Archivo """
        return super().texto() + "/"


def imprime_en_texto(lista):
    """
    Imprime los elementos de lista en la salida estándar en
    formato texto plano.
    """
    for arch in lista:  # lista -> [Archivo(), Carpeta(), Archuvo(), ...]
        # type(arch) ? , str [x], Archivo() o Carpeta()
        print( arch.texto() )

def guarda_en_archivo(lista, ruta):
    """
    Guarda los elementos de lista en el archivo en ruta en formato texto
    """
    with open(ruta, "w") as arch_texto:
        for elemento in lista:  # lista -> [Archivo(), Carpeta(), Archuvo(), ...]
            # type(arch) ? , str [x], Archivo() o Carpeta()
            # arch_texto.write(elemento.texto())
            # arch_texto.write("\n")
            arch_texto.write(elemento.texto() + "\n")

def guarda_en_archivo_csv(lista, ruta):
    """
    Guarda los elementos de lista en el archivo en ruta en formato csv
    """
    with open(ruta, "w", encoding="utf-8") as arch_texto:  # "iso8859-1", "latin-1"
        escritor_csv = csv.writer(arch_texto, delimiter=';', newline="")
        for elemento in lista:  # lista -> [Archivo(), Carpeta(), Archuvo(), ...]
            # type(arch) ? , str [x], Archivo() o Carpeta()
            # arch_texto.write(elemento.texto())
            # arch_texto.write("\n")
            escritor_csv.writerow(elemento.tupla_str)  # [col1, col2, ...]

def genera_html(lista):
    """ Regresa la lista formateada en HTML """
    filas = []
    for ele in lista:  # ele -> Archivo, Carpeta
        fila = f"<li>{ele.tamanio} | {ele.fecha_str} | {ele.get_ruta}</li>"
        filas.append(fila)
    filas: str = "\n".join(filas)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>Lista de archivos</h1>
        <hr />
        <ul>
        {filas}    
        </ul>
    </body>
    </html>
    """
    return html

@click.command()
@click.argument("carpeta", default=".", type=click.Path(exists=True))
@click.option("--csv", "salida_csv", is_flag=True,
                help="Guarda los resultados en formato CSV")
def main(carpeta, salida_csv):
    """
    Imprime la lista de archivos y carpetas de la carpeta actual o de la
    CARPETA proporcionada por el usuario.
    """
    carpeta_obj = Carpeta(carpeta)
    elementos: list = carpeta_obj.lista_elementos()
    # imprime_en_texto(elementos)
    if salida_csv:
        guarda_en_archivo_csv(elementos, "salida.csv")
    else:
        guarda_en_archivo(elementos, "salida.txt")

if __name__ == '__main__':
    main()
