# Mètodes per l'ageda

import platform, os

def esborraPantalla():
    if platform.system == 'Linux':
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
        if(i<len(opcions)-1) :
            cadenaOpcions += ", "
    cadenaOpcions += ")"
    print(f"{missatge} {cadenaOpcions}: ", end="")

def obteOpcio(arrayRebut, missatge):
    intMinim = int()
    intMaxim = int()
    opcioEscollida = int()
    esCorrecte = bool()
    esEnter = bool()
    cadLlegida=str()
    
    intMinim = 1
    intMaxim = len(arrayRebut)
    opcioEscollida = 0
    esCorrecte = False
    while True:
        esEnter = True
        esborraPantalla()
        mostraMenu(arrayRebut, missatge)
        opcioEscollida = int(input())
        try:
            if not type(opcioEscollida) is int:
                raise TypeError("\nNomés es poden entrar enters!\n\n")
        except:
            esEnter = False
        
        if((esEnter)&(opcioEscollida>=intMinim)&(opcioEscollida<=intMaxim)):
            esCorrecte = True
            break
        else:
            print("\nERROR!!!\nEntra una opció valida!\n\n")
            pitjaTecla("\nPîtja una tecla per continuar...")
    return opcioEscollida
