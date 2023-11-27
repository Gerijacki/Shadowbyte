import os
import requests
import platform

VIRUSTOTAL_API_KEY = '964ff6a97060a4512bf3a8047f09964b5a0b6f53055ce5e540e130eb09204b4b'  # api virus total

class Colors:
    # Codi d'escape ANSI per colors de text
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def esborraPantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def imprimir_banner():
    banner = f"""
{Colors.BLUE} _______  __   __  _______  _______  __    _ 
 ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄     ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
█       █  █ █  █      █      ██       █ █ ▄ █ █  ▄    █  █ █  █       █       █
█  ▄▄▄▄▄█  █▄█  █  ▄   █  ▄    █   ▄   █ ██ ██ █ █▄█   █  █▄█  █▄     ▄█    ▄▄▄█
█ █▄▄▄▄▄█       █ █▄█  █ █ █   █  █ █  █       █       █       █ █   █ █   █▄▄▄ 
█▄▄▄▄▄  █   ▄   █      █ █▄█   █  █▄█  █       █  ▄   ██▄     ▄█ █   █ █    ▄▄▄█
 ▄▄▄▄▄█ █  █ █  █  ▄   █       █       █   ▄   █ █▄█   █ █   █   █   █ █   █▄▄▄ 
█▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄▄▄▄▄█

    """

    print(f"{Colors.RED}{banner}{Colors.RESET}")

def mostra_menu():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Mostrar llista de fitxers en directori 1{Colors.RESET}")
    print(f"{Colors.RED}2. Mostrar llista de fitxers en directori 2{Colors.RESET}")
    print(f"{Colors.RED}3. Comparar fitxers en ambdós directoris{Colors.RESET}")
    print(f"{Colors.RED}4. Comparar fitxer específic{Colors.RESET}")
    print(f"{Colors.RED}5. Penjar un fitxer a VirusTotal i verificar malware{Colors.RESET}")
    print(f"{Colors.RED}6. Canviar directoris{Colors.RESET}")
    print(f"{Colors.RED}7. Sortir{Colors.RESET}")

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

def compara_fitxers(directori1, directori2):
    if os.path.exists(directori1) and os.path.exists(directori2):
        llista1 = set(os.listdir(directori1))
        llista2 = set(os.listdir(directori2))

        fitxers_comuns = llista1.intersection(llista2)

        print(f"\nFitxers comuns en ambdós directoris:")
        for fitxer in fitxers_comuns:
            print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET}")
    else:
        print(f"\n{Colors.YELLOW}Error: Un dels directoris no existeix.{Colors.RESET}")

def compara_fitxer(directori1, directori2, nom_fitxer):
    path1 = os.path.join(directori1, nom_fitxer)
    path2 = os.path.join(directori2, nom_fitxer)

    if os.path.exists(path1) and os.path.exists(path2):
        print(f"\nComparant contingut del fitxer {Colors.MAGENTA}{nom_fitxer}{Colors.RESET} en ambdós directoris:")
        with open(path1, 'r') as file1, open(path2, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

            if content1 == content2:
                print(f'El contingut del {Colors.GREEN}fitxer és idèntic{Colors.RESET} en ambdós directoris.')
            else:
                print(f'El contingut del {Colors.YELLOW}fitxer és diferent{Colors.RESET} en ambdós directoris.')
    else:
        print(f"\n{Colors.YELLOW}Error: Fitxer {nom_fitxer} no trobat en un dels directoris.{Colors.RESET}")

def penja_a_virustotal(nom_fitxer):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}

    with open(nom_fitxer, 'rb') as file:
        files = {'file': (nom_fitxer, file)}
        response = requests.post(url, files=files, params=params)

    result = response.json()
    print(f"\nResultats de VirusTotal:")
    print(f"SHA-256: {result.get('sha256')}")
    print(f"Permalink: {result.get('permalink')}")
    print("Resultat de l'anàlisi:", result.get('verbose_msg'))

def canviar_directoris():
    global directori1, directori2
    nou_directori1 = input(f"{Colors.RED}Introdueix el nou camí del directori 1: {Colors.RESET}")
    nou_directori2 = input(f"{Colors.RED}Introdueix el nou camí del directori 2: {Colors.RESET}")

    if not os.path.exists(nou_directori1):
        print(f"\n{Colors.YELLOW}Error: El directori {nou_directori1} no existeix.{Colors.RESET}")
    else:
        directori1 = nou_directori1

    if not os.path.exists(nou_directori2):
        print(f"\n{Colors.YELLOW}Error: El directori {nou_directori2} no existeix.{Colors.RESET}")
    else:
        directori2 = nou_directori2

    print(f"\n{Colors.GREEN}Directoris canviats amb èxit.{Colors.RESET}")

def main():
    imprimir_banner()

    directori1 = input(f"{Colors.RED}Introdueix el camí del directori 1: {Colors.RESET}")
    directori2 = input(f"{Colors.RED}Introdueix el camí del directori 2: {Colors.RESET}")

    if not os.path.exists(directori1):
        print(f"\n{Colors.YELLOW}Error: El directori {directori1} no existeix.{Colors.RESET}")
        # os.makedirs(directori1)
        # print(f"{Colors.GREEN}Directori {directori1} creat amb èxit.{Colors.RESET}")

    if not os.path.exists(directori2):
        print(f"\n{Colors.YELLOW}Error: El directori {directori2} no existeix.{Colors.RESET}")
        # os.makedirs(directori2)
        # print(f"{Colors.GREEN}Directori {directori2} creat amb èxit.{Colors.RESET}")

    while True:
        mostra_menu()

        opcio = input(f"\nSelecciona una opció ({Colors.RED}1-6{Colors.RESET}): ")

        if opcio == "1":
            llista_fitxers_directori(directori1)
        elif opcio == "2":
            llista_fitxers_directori(directori2)
        elif opcio == "3":
            compara_fitxers(directori1, directori2)
        elif opcio == "4":
            nom_fitxer = input(f"{Colors.RED}Introdueix el nom del fitxer a comparar: {Colors.RESET}")
            compara_fitxer(directori1, directori2, nom_fitxer)
        elif opcio == "5":
            nom_fitxer = input(f"{Colors.RED}Introdueix el nom del fitxer a penjar a VirusTotal: {Colors.RESET}")
            penja_a_virustotal(nom_fitxer)
        elif opcio == "6":
            canviar_directoris()
        elif opcio == "7":
            print("Sortint de l'aplicació. Bye :)")
            break
        else:
            print(f"Opció no vàlida. Si us plau, selecciona una opció correcta.")

if __name__ == "__main__":
    esborraPantalla()
    main()
