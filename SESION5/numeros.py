import click
import tiempo

@tiempo.tiempo_ejecucion
@click.command()
@click.argument("n", type=int)
def main(n):
    """ Imprime una lista de número en la salida estándar de longitud N """
    numeros = list(range(n))
    for i in numeros:
        print(i)
        
if __name__ == "__main__":
    main()