"""
Módulo que agrupa todas las funcionalidades
que permiten pedir entrada de números

"""
import sys


def pedirNumeroEntero():
    correcto = False
    num = 0

    while (not correcto):
        try:
            num = int(input("Eliga una opción del 1 al 4: "))
            correcto = True
        except ValueError:
            print('Error, introduce un número entero',
                  file=sys.stderr)
    return num

def pedirNumeroJuego():
    correcto = False
    num = 0

    while (not correcto):
        try:
            num = int(input("Introduzca un número: "))
            correcto = True
        except ValueError:
            print('Error, introduce un número entero',
                  file=sys.stderr)
    return num

