import platform
import os

def esborraPantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def pitjaTecla(missatge):
    input(missatge)

def mostraMenu(opcions, missatge):
    cadenaOpcions = " ("
    for i in range(len(opcions)):
        print(f"{(int(i + 1))} {opcions[i]}")
        cadenaOpcions += str(int(i) + 1)
        if(i < len(opcions) - 1):
            cadenaOpcions += ", "
    cadenaOpcions += ")"
    print(f"{missatge} {cadenaOpcions}: ", end="")

def obteOpcio(arrayRebut, missatge):
    intMinim = 1
    intMaxim = len(arrayRebut)
    opcioEscollida = 0
    esCorrecte = False

    while True:
        esborraPantalla()
        mostraMenu(arrayRebut, missatge)

        try:
            cadLlegida = input()
            opcioEscollida = int(cadLlegida)
        except ValueError:
            print("\nERROR!!!\nNomés es poden entrar enters!\n\n")
            pitjaTecla("\nPîtja una tecla per continuar...")
            continue

        if intMinim <= opcioEscollida <= intMaxim:
            esCorrecte = True
            break
        else:
            print("\nERROR!!!\nEntra una opció valida!\n\n")
            pitjaTecla("\nPîtja una tecla per continuar...")

    return opcioEscollida
