"""
Módulo tiempo.py:
Contiene decoradores para calcular el rendimiento de un programa
- tiempo_ejecucion(): Obtiene e imprime el tiempo que una función ha tomado en ejecutarse en segundos
"""
import time

def tiempo_ejecucion(f):
    """
    Obtiene e imprime el tiempo que una función ha tomado en ejecutarse en segundos
    """
    def determina_tiempo(*args, **kwargs):
        """ Función interna del decorador """
        t1 = time.time()
        valor = f(*args, **kwargs)
        t2 = time.time()
        print( f"\nSegundos totales de ejecución: {t2-t1} seg\n")
        
        return valor
    
    return determina_tiempo