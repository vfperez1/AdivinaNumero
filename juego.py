"""
Módulo que agrupa las funciones que describen la lógica interna del juego

"""

from entrada import (
    pedirNumeroEntero,
    pedirNumeroJuego,
    pedir_entrada_si_o_no,
    pedir_entrada_verdadero_o_falso,
)

import random
import sys

SIMPLE = random.randint(0, 100)
INTERMEDIO = random.randint(0, 1000)
AVANZADO = random.randint(0, 10000)

print ("BIENVENIDO AL JUEGO DE ADIVINAR EL NÚMERO")
print("1. Nivel simple (entre 0 y 100 numeros)")
print("2. Nivel intermedio (entre 0 y 1000 numeros)")
print("3. Nivel avanzado (entre 0 y 10000 numeros)")
print("4. Salir")

opcion = pedirNumeroEntero()

def ElegirNivel(opcion):
    while True:

        if opcion == 1:
            nivel = 1
            print("Nivel seleccionado SIMPLE, eliga un número del 0 al 100: ")
        elif opcion == 2:
            nivel = 2
            print("Nivel seleccionado INTERMEDIO, eliga un número del 0 al 1000: ")
        elif opcion == 3:
            nivel = 3
            print("Nivel seleccionado AVANZADO, eliga un número del 0 al 10000: ")
        elif opcion == 4:
            sys.exit()
        else:
            print("Eligue una opcion del [1-4].", file=sys.stderr)

        return nivel

def GenerarRandom():
            nivel = ElegirNivel(opcion)
            if nivel == 1:
                aleatorio = SIMPLE
            elif nivel == 2:
                aleatorio = INTERMEDIO
            elif nivel == 3:
                aleatorio = AVANZADO
            return aleatorio


def jugar_una_vez():
    opcion = GenerarRandom()
    intento = pedirNumeroJuego()
    # Se comprueba si el intento es correcto o no
    if intento < opcion:
        print("Demasiado pequeño")
        victoria = False
    elif intento > opcion:
        print("Demasiado grande")
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
    return victoria

def jugar_una_partida():
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria = jugar_una_vez()

        if (victoria):
            return

def jugar():

    while True:
        jugar_una_partida()
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return

