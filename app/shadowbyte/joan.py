import os
import platform

# Colors de text
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

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

# Variables Globals per als directoris
directori1 = ""
directori2 = ""

# Neteja de pantalla
def esborra_pantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return "{:.2f} {}".format(size, unit)

def llista_fitxers_directori(directori):
    try:
        if os.path.exists(directori):
            print(f"\nContingut de {Colors.RED}{directori}{Colors.RESET}:")
            for root, dirs, files in os.walk(directori):
                for name in dirs:
                    path = os.path.join(root, name)
                    print(f"- {Colors.CYAN}{name}{Colors.RESET} (Directori)")
                for name in files:
                    path = os.path.join(root, name)
                    size = os.path.getsize(path)
                    formatted_size = format_size(size)
                    print(f"  - {Colors.MAGENTA}{name}{Colors.RESET} ({Colors.CYAN}Fitxer{Colors.RESET}, {Colors.GREEN}{formatted_size}{Colors.RESET})")
        else:
            print(f"\n{Colors.YELLOW}Error: El directori {directori} no existeix.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al mostrar la llista de fitxers: {e}{Colors.RESET}")

# Comparar fitxers
def compara_fitxers(directori1, directori2):
    try:
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

                tipus_fitxer1, mida_fitxer1 = obtenir_info_fitxer(ruta_fitxer1)
                tipus_fitxer2, mida_fitxer2 = obtenir_info_fitxer(ruta_fitxer2)

                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET}), ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")

            print("\nFitxers exclusius en el directori 1:")
            for fitxer in fitxers_exclusius_directori1:
                ruta_fitxer1 = os.path.join(directori1, fitxer)
                tipus_fitxer1, mida_fitxer1 = obtenir_info_fitxer(ruta_fitxer1)
                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET})")

            print("\nFitxers exclusius en el directori 2:")
            for fitxer in fitxers_exclusius_directori2:
                ruta_fitxer2 = os.path.join(directori2, fitxer)
                tipus_fitxer2, mida_fitxer2 = obtenir_info_fitxer(ruta_fitxer2)
                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")
        else:
            print(f"\n{Colors.YELLOW}Error: Un dels directoris no existeix.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al comparar fitxers: {e}{Colors.RESET}")

def compara_fitxer(directori1, directori2):
    try:
        nom_fitxer = input(f"{Colors.RED}Introdueix el nom del fitxer a comparar: {Colors.RESET}")
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
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al comparar fitxer: {e}{Colors.RESET}")

def obtenir_info_fitxer(ruta_fitxer):
    try:
        if os.path.isfile(ruta_fitxer):
            tipus_fitxer = "Fitxer"
            mida_fitxer = os.path.getsize(ruta_fitxer)
        else:
            tipus_fitxer = "Directori"
            mida_fitxer = sum(os.path.getsize(os.path.join(ruta_fitxer, f)) for f in os.listdir(ruta_fitxer))
        return tipus_fitxer, mida_fitxer
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al obtenir informació del fitxer: {e}{Colors.RESET}")
        return "", 0

def mostra_menu():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Mostrar llista de fitxers en directori 1:{Colors.RESET}")
    print(f"{Colors.RED}2. Mostrar llista de fitxers en directori 2:{Colors.RESET}")
    print(f"{Colors.RED}3. Comparar directori-1 i directori-2:{Colors.RESET}")
    print(f"{Colors.RED}4. Comparar fitxer específic:{Colors.RESET}")
    print(f"{Colors.RED}5. Canviar directoris:{Colors.RESET}")
    print(f"{Colors.RED}6. Natejar Pantalla:{Colors.RESET}")
    print(f"{Colors.RED}7. Sortir:{Colors.RESET}")

# Funció per canviar directoris
def canviar_directoris():
    global directori1, directori2
    try:
        nou_directori1 = input(f"{Colors.RED}Introdueix el nou camí del directori 1: {Colors.RESET}")
        nou_directori2 = input(f"{Colors.RED}Introdueix el nou camí del directori 2: {Colors.RESET}")

        if os.path.exists(nou_directori1):
            directori1 = nou_directori1
            print(f"\n{Colors.GREEN}El {directori1} s'ha canviat amb èxit.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directori {nou_directori1} no existeix.{Colors.RESET}")

        if os.path.exists(nou_directori2):
            directori2 = nou_directori2
            print(f"\n{Colors.GREEN}El {directori2} s'ha canviat amb èxit.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directori {nou_directori2} no existeix.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error en canviar els directoris: {e}{Colors.RESET}")

# Funció per sortir
def sortir():
    print(f"{Colors.GREEN}Sortint de l'aplicació. ¡Bye! :){Colors.RESET}")
    exit()

def main():
    imprimir_banner()
    global directori1, directori2
    directori1 = input(f"{Colors.RED}Introdueix el camí del directori 1: {Colors.RESET}")
    directori2 = input(f"{Colors.RED}Introdueix el camí del directori 2: {Colors.RESET}")
    while True:
        mostra_menu()
        try:
            opcio = int(input(f"\nSelecciona una opció ({Colors.RED}1-6{Colors.RESET}): "))
            
            options = {
                1: lambda: llista_fitxers_directori(directori1),
                2: lambda: llista_fitxers_directori(directori2),
                3: lambda: compara_fitxers(directori1, directori2),
                4: lambda: compara_fitxer(directori1, directori2),
                5: canviar_directoris,
                6: esborra_pantalla,
                7: sortir,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.YELLOW}Opció no vàlida. Siusplau, selecciona una opció vàlida.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.YELLOW}Has d'introduir un nombre vàlid{Colors.RESET}")

if __name__ == "__main__":
    esborra_pantalla()
    main()
