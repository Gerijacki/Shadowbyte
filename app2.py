import os
import platform
import json
import datetime

import metAgenda

# colors de text
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

# directorios por defecto
# directori1 = "/path/to/directori1"
# directori2 = "/path/to/directori2"

# natejar pantalla
def esborraPantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def llista_fitxers_directori(directori):
    if os.path.exists(directori):
        try:
            llista_fitxers = os.listdir(directori)
            print(f"\nFitxers en {Colors.RED}{directori}{Colors.RESET}:")
            for fitxer in llista_fitxers:
                ruta_fitxer = os.path.join(directori, fitxer)
                tamany_mb = os.path.getsize(ruta_fitxer) / (1024 * 1024)  # Tamany en megabytes
                tipus_fitxer = "Fitxer" if os.path.isfile(ruta_fitxer) else "Directori"
                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({tamany_mb:.2f} MB, {Colors.CYAN}{tipus_fitxer}{Colors.RESET})")
        except FileNotFoundError:
            print(f"\n{Colors.YELLOW}Error: El directori {directori} no existeix.{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}Error: El directori {directori} no existeix.{Colors.RESET}")

# comprarar arx
def compara_fitxers(directori1, directori2):
    if os.path.exists(directori1) and os.path.exists(directori2):
        llista1 = set(os.listdir(directori1))
        llista2 = set(os.listdir(directori2))

        fitxers_comuns = llista1.intersection(llista2)
        fitxers_exclusius_directori1 = llista1 - fitxers_comuns
        fitxers_exclusius_directori2 = llista2 - fitxers_comuns

        print("\nFitxers comuns en ambdós directoris:")
        for fitxer in fitxers_comuns:
            ruta_fitxer1 = os.path.join(directori1, fitxer)
            ruta_fitxer2 = os.path.join(directori2, fitxer)

            if os.path.isfile(ruta_fitxer1):
                tipus_fitxer1 = "Fitxer"
                mida_fitxer1 = os.path.getsize(ruta_fitxer1)
            else:
                tipus_fitxer1 = "Directori"
                mida_fitxer1 = sum(os.path.getsize(os.path.join(ruta_fitxer1, f)) for f in os.listdir(ruta_fitxer1))

            if os.path.isfile(ruta_fitxer2):
                tipus_fitxer2 = "Fitxer"
                mida_fitxer2 = os.path.getsize(ruta_fitxer2)
            else:
                tipus_fitxer2 = "Directori"
                mida_fitxer2 = sum(os.path.getsize(os.path.join(ruta_fitxer2, f)) for f in os.listdir(ruta_fitxer2))

            print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET}), ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")

        print("\nFitxers exclusius en el directori 1:")
        for fitxer in fitxers_exclusius_directori1:
            ruta_fitxer1 = os.path.join(directori1, fitxer)

            if os.path.isfile(ruta_fitxer1):
                tipus_fitxer1 = "Fitxer"
                mida_fitxer1 = os.path.getsize(ruta_fitxer1)
            else:
                tipus_fitxer1 = "Directori"
                mida_fitxer1 = sum(os.path.getsize(os.path.join(ruta_fitxer1, f)) for f in os.listdir(ruta_fitxer1))

            print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET})")

        print("\nFitxers exclusius en el directori 2:")
        for fitxer in fitxers_exclusius_directori2:
            ruta_fitxer2 = os.path.join(directori2, fitxer)

            if os.path.isfile(ruta_fitxer2):
                tipus_fitxer2 = "Fitxer"
                mida_fitxer2 = os.path.getsize(ruta_fitxer2)
            else:
                tipus_fitxer2 = "Directori"
                mida_fitxer2 = sum(os.path.getsize(os.path.join(ruta_fitxer2, f)) for f in os.listdir(ruta_fitxer2))

            print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")
    else:
        print(f"\n{Colors.YELLOW}Error: Un dels directoris no existeix.{Colors.RESET}")

# comparar
def compara_fitxer(directori1, directori2, nom_fitxer):
    path1 = os.path.join(directori1, nom_fitxer)
    path2 = os.path.join(directori2, nom_fitxer)

    if os.path.exists(path1) and os.path.exists(path2):
        print(f"\nComparant contingut del fitxer {Colors.MAGENTA}{nom_fitxer}{Colors.RESET} en ambdós directoris:")
        with open(path1, 'rb') as file1, open(path2, 'rb') as file2:
            content1 = file1.read()
            content2 = file2.read()

            if content1 == content2:
                print(f'El contingut del {Colors.GREEN}fitxer és idèntic{Colors.RESET} en ambdós directoris.')
            else:
                print(f'El contingut del {Colors.YELLOW}fitxer és diferent{Colors.RESET} en ambdós directoris.')
    else:
        print(f"\n{Colors.YELLOW}Error: Fitxer {nom_fitxer} no trobat en un dels directoris.{Colors.RESET}")

def imprimir_banner():
    banner = f"""
    {Colors.BLUE}
     ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄     ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
    █       █  █ █  █      █      ██       █ █ ▄ █ █  ▄    █  █ █  █       █       █
    █  ▄▄▄▄▄█  █▄█  █  ▄   █  ▄    █   ▄   █ ██ ██ █ █▄█   █  █▄█  █▄     ▄█    ▄▄▄█
    █ █▄▄▄▄▄█       █ █▄█  █ █ █   █  █ █  █       █       █       █ █   █ █   █▄▄▄ 
    █▄▄▄▄▄  █   ▄   █      █ █▄█   █  █▄█  █       █  ▄   ██▄     ▄█ █   █ █    ▄▄▄█
     ▄▄▄▄▄█ █  █ █  █  ▄   █       █       █   ▄   █ █▄█   █ █   █   █   █ █   █▄▄▄ 
    █▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄▄▄▄▄█

    """
    print(f"{Colors.RED}{banner}{Colors.RESET}")

def canviar_directoris():
    global directori1, directori2
    nou_directori1 = input(f"{Colors.RED}Introdueix el nou camí del directori 1: {Colors.RESET}")
    nou_directori2 = input(f"{Colors.RED}Introdueix el nou camí del directori 2: {Colors.RESET}")

    try:
        if os.path.exists(nou_directori1):
            directori1 = nou_directori1
            print(f"\n{Colors.GREEN}Directori 1 canviat amb èxit.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directori {nou_directori1} no existeix.{Colors.RESET}")

        if os.path.exists(nou_directori2):
            directori2 = nou_directori2
            print(f"\n{Colors.GREEN}Directori 2 canviat amb èxit.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directori {nou_directori2} no existeix.{Colors.RESET}")

    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al canviar els directoris: {e}{Colors.RESET}")

def main():
    imprimir_banner()
    directori1 = input(f"{Colors.RED}Introdueix el camí del directori 1: {Colors.RESET}")
    directori2 = input(f"{Colors.RED}Introdueix el camí del directori 2: {Colors.RESET}")
    while True:
        etMenu1 = ["Mostrar llista de fitxers en directori 1",
                   "Mostrar llista de fitxers en directori 2",
                   "Comparar fitxers en ambdós directoris",
                   "Comparar fitxer específic",
                   "Canviar directoris",
                   "Sortir"]

        opcioEscollida = metAgenda.obteOpcio(etMenu1, "Selecciona una opció: ")

        if opcioEscollida == 1:
            llista_fitxers_directori(directori1)
        elif opcioEscollida == 2:
            llista_fitxers_directori(directori2)
        elif opcioEscollida == 3:
            compara_fitxers(directori1, directori2)
        elif opcioEscollida == 4:
            nom_fitxer = input(f"{Colors.RED}Introdueix el nom del fitxer a comparar: {Colors.RESET}")
            compara_fitxer(directori1, directori2, nom_fitxer)
        elif opcioEscollida == 5:
            canviar_directoris()
        elif opcioEscollida == 6:
            print("Sortint de l'aplicació. Bye :)")
            break
        else:
            print(f"Opció no vàlida. Si us plau, selecciona una opció correcta.")

if __name__ == "__main__":
    esborraPantalla()
    main()
