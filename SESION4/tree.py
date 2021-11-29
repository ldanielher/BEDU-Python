import click
# import ...

class Archivo():
    pass

class Carpeta():
    pass

def imprime_en_texto(lista):
    pass

@click.command()
@click.argument("carpeta", default=".", type=click.Path(exists=True))
def main(carpeta):
    """
    Imprime la lista de archivos y carpetas de la carpeta actual o de la
    CARPETA proporcionada por el usuario.
    """
    print("Valor de la variable carpeta =", carpeta)
    carpeta_obj = Carpeta(carpeta)
    print(carpeta_obj)
    elementos = carpeta_obj.lista_elementos()
    imprime_en_texto(lista_elementos)

if __name__ == '__main__':
    main()
