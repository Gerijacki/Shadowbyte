import os
import requests
import platform
import json
import filecmp
import datetime

# Virus Total i logs
VIRUSTOTAL_API_KEY = ''  # api virus total
LOGS_ENABLED = False
LOGS_FOLDER = "./logs"

# colors de text
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

# natejar pantalla
def esborraPantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

# config 
def cargar_configuracion():
    global VIRUSTOTAL_API_KEY, LOGS_ENABLED, LOGS_FOLDER
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            VIRUSTOTAL_API_KEY = config.get("virustotal_api_key", VIRUSTOTAL_API_KEY)
            LOGS_ENABLED = config.get("logs_enabled", LOGS_ENABLED)
            LOGS_FOLDER = config.get("logs_folder", LOGS_FOLDER)
    except FileNotFoundError:
        # no config -> predeterminat
        pass

# guardar config
def guardar_configuracion():
    config = {
        "virustotal_api_key": VIRUSTOTAL_API_KEY,
        "logs_enabled": LOGS_ENABLED,
        "logs_folder": LOGS_FOLDER
    }
    with open("config.json", "w") as config_file:
        json.dump(config, config_file, indent=2)

# banner
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

# logs
def log_moviment(missatge):
    if LOGS_ENABLED:
        if not os.path.exists(LOGS_FOLDER):
            print(f"\n{Colors.YELLOW}Advertencia: El directorio de logs no existe. Creando directorio...{Colors.RESET}")
            try:
                os.makedirs(LOGS_FOLDER)
            except OSError as e:
                print(f"\n{Colors.YELLOW}Error al crear el directorio de logs: {e}{Colors.RESET}")
                print(f"{Colors.YELLOW}Cargando configuración predeterminada.{Colors.RESET}")
                cargar_configuracion()
                return

        arxiu_log = os.path.join(LOGS_FOLDER, f"{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log")
        with open(arxiu_log, 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()} - {missatge}\n")


# menu config
def mostrar_configuracion():
    print(f"\nConfiguració actual:")
    print(f"1. Clau de l'API de VirusTotal: {Colors.MAGENTA}{VIRUSTOTAL_API_KEY}{Colors.RESET}")
    print(f"2. Sistema de logs: {Colors.MAGENTA}{'Activat' if LOGS_ENABLED else 'Desactivat'}{Colors.RESET}")
    print(f"3. Carpeta de logs: {Colors.MAGENTA}{LOGS_FOLDER}{Colors.RESET}")

def configurar_programa():
    global VIRUSTOTAL_API_KEY, LOGS_ENABLED, LOGS_FOLDER
    op_config = input(f"\nSelecciona una opció de configuració ({Colors.RED}1-3{Colors.RESET}, o 'T' per tornar): ")
    
    if op_config == "1":
        VIRUSTOTAL_API_KEY = input(f"{Colors.RED}Introdueix la nova clau de l'API de VirusTotal: {Colors.RESET}")
        log_moviment("S'ha canviat la clau de l'API de VirusTotal.")
    elif op_config == "2":
        LOGS_ENABLED = not LOGS_ENABLED  # Invertir el estado actual
        print(f"Sistema de logs {'activat' if LOGS_ENABLED else 'desactivat'}.")
        log_moviment(f"S'ha {'activat' if LOGS_ENABLED else 'desactivat'} el sistema de logs.")
    elif op_config == "3":
        LOGS_FOLDER = input(f"{Colors.RED}Introdueix la nova carpeta de logs: {Colors.RESET}")
        log_moviment(f"S'ha canviat la carpeta de logs a: {LOGS_FOLDER}")
    elif op_config.lower() == "t":
        return
    else:
        print(f"{Colors.YELLOW}Opció no vàlida.{Colors.RESET}")

    guardar_configuracion()
    print(f"\n{Colors.GREEN}Configuració actualitzada amb èxit.{Colors.RESET}")
    log_moviment("S'ha guardat la configuració del programa.")

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return "{:.2f} {}".format(size, unit)

def llista_fitxers_directori(directori):
    try:
        log_moviment(f"S'ha mostrat la llista de fitxers del directori: {directori}")
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
        log_moviment("S'ha comparat la llista de fitxers en ambdós directoris.")
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

def compara_fitxer(directori1, directori2, nom_fitxer):
    try:
        log_moviment(f"S'ha comparat el fitxer: {nom_fitxer}")
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


def penja_a_virustotal(nom_fitxer):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}

    try:
        log_moviment(f"S'ha penjat el fitxer a VirusTotal: {nom_fitxer}")
        with open(nom_fitxer, 'rb') as file:
            files = {'file': (nom_fitxer, file)}
            response = requests.post(url, files=files, params=params)
            
            # resposta HTTP
            if response.status_code == 200:
                result = response.json()
                print(f"\nResultats de VirusTotal:")
                print(f"SHA-256: {result.get('sha256')}")
                print(f"Permalink: {result.get('permalink')}")
                print("Resultat de l'anàlisi:", result.get('verbose_msg'))
            else:
                print(f"\n{Colors.YELLOW}Error en la solicitud a VirusTotal. Código de respuesta HTTP: {response.status_code}{Colors.RESET}")

    except FileNotFoundError:
        print(f"\n{Colors.YELLOW}Error: Fitxer no trobat: {nom_fitxer}{Colors.RESET}")
    except requests.RequestException as e:
        print(f"\n{Colors.YELLOW}Error en la solicitud a VirusTotal: {e}{Colors.RESET}")

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

# Funció per sortir
def sortir():
    print(f"{Colors.GREEN}Sortint de l'aplicació. ¡Bye! :){Colors.RESET}")
    exit()

def config():
    mostrar_configuracion()
    configurar_programa()


# menu
def mostra_menu():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Mostrar llista de fitxers en directori 1{Colors.RESET}")
    print(f"{Colors.RED}2. Mostrar llista de fitxers en directori 2{Colors.RESET}")
    print(f"{Colors.RED}3. Comparar fitxers en ambdós directoris{Colors.RESET}")
    print(f"{Colors.RED}4. Comparar fitxer específic{Colors.RESET}")
    print(f"{Colors.RED}5. Penjar un fitxer a VirusTotal i verificar malware{Colors.RESET}")
    print(f"{Colors.RED}6. Canviar directoris{Colors.RESET}")
    print(f"{Colors.RED}7. Configuració{Colors.RESET}")
    print(f"{Colors.RED}8. Sortir{Colors.RESET}")


def main():
    cargar_configuracion()
    imprimir_banner()
    log_moviment("S'ha iniciat l'aplicació.")

    global directori1, directori2

    directori1 = input(f"{Colors.RED}Introdueix el camí del directori 1: {Colors.RESET}")
    directori2 = input(f"{Colors.RED}Introdueix el camí del directori 2: {Colors.RESET}")

    if not os.path.exists(directori1):
        print(f"\n{Colors.YELLOW}Error: El directori {directori1} no existeix.{Colors.RESET}")
        log_moviment(f"S'ha intentat accedir a un directori inexistent: {directori1}")
        exit

    if not os.path.exists(directori2):
        print(f"\n{Colors.YELLOW}Error: El directori {directori2} no existeix.{Colors.RESET}")
        log_moviment(f"S'ha intentat accedir a un directori inexistent: {directori2}")
        exit

    while True:
        mostra_menu()
        try:
            opcio = int(input(f"\nSelecciona una opció ({Colors.RED}1-6{Colors.RESET}): "))
            
            options = {
                1: lambda: llista_fitxers_directori(directori1),
                2: lambda: llista_fitxers_directori(directori2),
                3: lambda: compara_fitxers(directori1, directori2),
                4: lambda: compara_fitxer(directori1, directori2, input(f"{Colors.RED}Introdueix el nom del fitxer a comparar: {Colors.RESET}")),
                5: lambda: penja_a_virustotal(input(f"{Colors.RED}Introdueix el nom del fitxer a penjar: {Colors.RESET}")),
                6: canviar_directoris,
                7: config,
                8: sortir,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.YELLOW}Opció no vàlida. Siusplau, selecciona una opció vàlida.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.YELLOW}Has d'introduir un nombre vàlid{Colors.RESET}")

if __name__ == "__main__":
    esborraPantalla()
    main()