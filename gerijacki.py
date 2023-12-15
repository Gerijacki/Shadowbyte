# no pain no gain
import os
import random
import string
import glob
import pytube
import speedtest
import psutil
import socket
import platform
import cpuinfo
import requests
import platform
import json
import datetime
import csv
import qrcode
from colorama import init, Fore, Style, Back

def banner_gerijacki():
    banner = f"""
{Fore.MAGENTA} ▄███▄   ████▄██▄   ▄███▄     ▄▄▄▄███▄▄▄▄    ▄██████▄  ▄██████▄   ▄██████▄     ▄██████▄
{Fore.MAGENTA}██▀  ▀  ██▀  ▀██   ██▀  ▀       ████▀██▀   ███    ███ ██    ███ ██    ███   ██▀  ▀██
{Fore.RED}▀█▄    ██     ▀█ ██               ██     ▄█████▄  ██    ███ ██    ███  ██    ███
{Fore.RED}  ▀██  ██▄   ▄█ ██               ██    ██▀  ▀██ ██    ███ ██    ███  ██    ███
{Fore.RED}▄███▄     ▄███▄ ▀██████▄       ▀███████▀  ▄███▄██  ▀██████▀   ▀██████▀   ▀██████▀
{Fore.CYAN}▀▀▀▀    ▀▀▀▀         ▀▀                      ▀▀▀▀             ▀▀▀▀
{Style.RESET_ALL}
{Fore.GREEN}Benvingut la la meva eina multifunció programmada en python :) 
Escull un de les segunts opcions per escollir quina eina vols:
{Style.RESET_ALL}
"""
    print(banner)

# menu
def menu_gerijacki():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Info{Colors.RESET}")
    print(f"{Colors.RED}2. Direct-X{Colors.RESET}")
    print(f"{Colors.RED}3. Task{Colors.RESET}")
    print(f"{Colors.RED}4. YT-MP4{Colors.RESET}")
    print(f"{Colors.RED}5. PASSWD{Colors.RESET}")
    print(f"{Colors.RED}6. Generador QR{Colors.RESET}")
    print(f"{Colors.RED}7. Sortir{Colors.RESET}")

# colors de text
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
# INFOBYTE
def menu_infobyte():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Speed Test{Colors.RESET}")
    print(f"{Colors.RED}2. Información del sistema{Colors.RESET}")
    print(f"{Colors.RED}3. Información de red{Colors.RESET}")
    print(f"{Colors.RED}4. Información del disco{Colors.RESET}")
    print(f"{Colors.RED}5. Borrar archivos temporales{Colors.RESET}")
    print(f"{Colors.RED}6. Salir{Colors.RESET}")

def banner_infobyte():
    banner_text = f"""
    {Colors.CYAN}
    ╔═══╗─────╔╗───╔╗───╔╗
    ║╔══╝─────║║───║║──╔╝╚╗
    ║╚══╦╗╔╦══╣║╔══╣║╔═╩╗╔╬══╦═╗
    ║╔══╣║║║╔╗║║║╔═╣║║══╣║║══╬╗║
    ║╚══╣║║║╚╝║║╚╩═║╚╣══║║╠══║║║
    ╚═══╩╝╚╩══╩╩═══╩═╩══╝╚╩══╩╩╝
    
    {Colors.RESET}
    ¡Bienvenido a Tu Herramienta Multifunción!
    """

    print(f"{Colors.RED}{banner_text}{Colors.RESET}")


def temp_del():
    directorio_temporal = os.path.join(os.environ["TEMP"], '*')
    
    try:
        archivos_temporales = glob.glob(directorio_temporal)
        for archivo in archivos_temporales:
            if os.path.isfile(archivo):
                os.remove(archivo)
        print(f"{Colors.MAGENTA}Archivos temporales borrados con éxito.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.YELLOW}Error al borrar archivos temporales: {e}{Colors.RESET}")

def medir_velocidad():
    # print(f'{Colors.YELLOW}Funció no disponible de moment{Colors.RESET}')
    st = speedtest.Speedtest()

    print("Realizando prueba de velocidad...")
    print("Espere....")

    velocidad_carga = st.upload() / 10**6
    velocidad_descarga = st.download() / 10**6

    print(f"Velocidad de carga: ({Colors.MAGENTA} {velocidad_carga:.2f} Mbps{Colors.RESET})")
    print(f"Velocidad de descarga: ({Colors.MAGENTA} {velocidad_descarga:.2f} Mbps{Colors.RESET})")

def red_info():
    host_ip = socket.gethostbyname(socket.gethostname())
    interfaces = psutil.net_if_addrs()

    print(f"{Colors.GREEN}IP del host: {host_ip}{Colors.RESET}")
    print(f"\n{Colors.GREEN}Información de interfaz de red:{Colors.RESET}")
    for iface, addrs in interfaces.items():
        print(f"\t{Colors.GREEN}{iface}:{Colors.RESET}")
        for addr in addrs:
            print(f"\t\t- Tipo: {addr.family}, Dirección: {addr.address}, Máscara de red: {addr.netmask}{Colors.RESET}")

def disk_info():
    disco = psutil.disk_usage('/')

    print(f"{Colors.GREEN}Información del Disco:{Colors.RESET}")
    print(f"\t{Colors.GREEN}Total: {disco.total / (1024 ** 3):.2f} GB{Colors.RESET}")
    print(f"\t{Colors.GREEN}Usado: {disco.used / (1024 ** 3):.2f} GB{Colors.RESET}")
    print(f"\t{Colors.GREEN}Disponible: {disco.free / (1024 ** 3):.2f} GB{Colors.RESET}")
    print(f"\t{Colors.GREEN}Porcentaje de uso: {disco.percent}%{Colors.RESET}")

def sys_info():
    print(f"{Colors.GREEN}Información del sistema:{Colors.RESET}")
    print(f"\t{Colors.GREEN}Sistema operativo: {platform.system()} {platform.version()}{Colors.RESET}")
    print(f"\t{Colors.GREEN}Arquitectura del sistema: {platform.architecture()}{Colors.RESET}")
    print(f"\t{Colors.GREEN}Procesador: {platform.processor()}{Colors.RESET}")
    print(f"\t{Colors.GREEN}Versión de Python: {platform.python_version()}{Colors.RESET}")

    print(f"\n{Colors.GREEN}Información de la CPU:{Colors.RESET}")
    cpu_info = cpuinfo.get_cpu_info()

    # Intentar acceder a claves específicas
    try:
        print(f"\t{Colors.GREEN}Fabricante: {cpu_info['vendor_id_raw']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Modelo: {cpu_info['brand_raw']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Arquitectura: {cpu_info['arch']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Núcleos físicos: {psutil.cpu_count(logical=False)}{Colors.RESET}")
    except KeyError as e:
        print(f"{Colors.RED}Error: Clave no encontrada en el diccionario de información de la CPU: {e}{Colors.RESET}")

def salir():
    print(f"{Colors.GREEN}Saliendo de la aplicación. ¡Bye! :){Colors.RESET}")
    exit()

def main_info():
    esborraPantalla()
    banner_infobyte()
    while True:
        menu_infobyte()

        try:
            opcio = int(input(f"\nSelecciona una opción ({Colors.RED}1-8{Colors.RESET}): "))
            
            options = {
                1: medir_velocidad,
                2: sys_info,
                3: red_info,
                4: disk_info,
                5: temp_del,
                6: main,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.RED}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Debes introducir un número válido{Colors.RESET}")

# SHAWOBYTE

# Virus Total i logs
VIRUSTOTAL_API_KEY = ''  # api virus total
LOGS_ENABLED = False
LOGS_FOLDER = "./logs"

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
def banner_shadowbyte():
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
def menu_shadowbyte():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Mostrar llista de fitxers en directori 1{Colors.RESET}")
    print(f"{Colors.RED}2. Mostrar llista de fitxers en directori 2{Colors.RESET}")
    print(f"{Colors.RED}3. Comparar fitxers en ambdós directoris{Colors.RESET}")
    print(f"{Colors.RED}4. Comparar fitxer específic{Colors.RESET}")
    print(f"{Colors.RED}5. Penjar un fitxer a VirusTotal i verificar malware{Colors.RESET}")
    print(f"{Colors.RED}6. Canviar directoris{Colors.RESET}")
    print(f"{Colors.RED}7. Configuració{Colors.RESET}")
    print(f"{Colors.RED}8. Sortir{Colors.RESET}")


def main_dic():
    esborraPantalla()
    cargar_configuracion()
    banner_shadowbyte()
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
        menu_shadowbyte()
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
                8: main,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.YELLOW}Opció no vàlida. Siusplau, selecciona una opció vàlida.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.YELLOW}Has d'introduir un nombre vàlid{Colors.RESET}")

# TAREAS

# Inicializar colorama
init(autoreset=True)

def cargar_tareas():
    try:
        with open('tareas.csv', 'r', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            return [
                dict(
                    nombre=row[0] if len(row) > 0 else "",
                    descripcion=row[1] if len(row) > 1 else "",
                    prioridad=int(row[2]) if len(row) > 2 else 0,
                    estado=row[3] if len(row) > 3 else ""
                )
                for row in lector_csv
            ]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open('tareas.csv', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        for tarea in tareas:
            escritor_csv.writerow([tarea["nombre"], tarea["descripcion"], tarea["prioridad"], tarea["estado"]])

def mostrar_tareas(tareas):
    for idx, tarea in enumerate(tareas, start=1):
        estado_color = Fore.GREEN if tarea["estado"] == "completada" else Fore.RED
        print(f'{idx}. [{estado_color}{tarea["estado"]}{Style.RESET_ALL}] {tarea["nombre"]}, {tarea["descripcion"]}, Prioridad: {tarea["prioridad"]}')

def menu_tareas():
    print("\n--- Gestor de Tareas ---")
    print(f"1. {Fore.CYAN}Ver tareas{Style.RESET_ALL}")
    print(f"2. {Fore.CYAN}Añadir tarea{Style.RESET_ALL}")
    print(f"3. {Fore.CYAN}Marcar tarea como completada{Style.RESET_ALL}")
    print(f"4. {Fore.CYAN}Salir{Style.RESET_ALL}")

def banner_tareas():
    banner = f"""
{Fore.BLUE}  _______ _                 _______           _       
 |__   __| |               |__   __|         | |      
    | |  | |__   __ _ ______ _| | ___  _ __ | |_ ___ 
    | |  | '_ \ / _` |_  / _` | |/ _ \| '_ \| __/ __|
    | |  | | | | (_| |/ / (_| | | (_) | | | | |_\__ \\
    |_|  |_| |_|\__,_/___\__,_|_|\___/|_| |_|\__|___/{Style.RESET_ALL}
    """
    print(banner)

def nueva_tarea(tareas):
    nombre = input(f"{Fore.CYAN}Introduce el nombre de la tarea: {Style.RESET_ALL}")
    descripcion = input(f"{Fore.CYAN}Introduce la descripción de la tarea: {Style.RESET_ALL}")
    try:
        prioridad = int(input(f"{Fore.CYAN}Introduce la prioridad de la tarea (1-5): {Style.RESET_ALL}"))
        if 1 <= prioridad <= 5:
            nueva_tarea = {
                "nombre": nombre,
                "descripcion": descripcion,
                "prioridad": prioridad,
                "estado": "pendiente"
            }
            tareas.append(nueva_tarea)
            guardar_tareas(tareas)
            print(f"{Fore.GREEN}Tarea añadida correctamente.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}La prioridad debe estar entre 1 y 5.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Debes introducir un número válido para la prioridad.{Style.RESET_ALL}")

def sortir():
    print(f"{Fore.MAGENTA}Saliendo de la aplicación. ¡Hasta luego! :) {Style.RESET_ALL}")
    exit()

def status_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        idx_completada = int(input(f"{Fore.CYAN}Seleccione el número de la tarea completada: {Style.RESET_ALL}")) - 1
        if 0 <= idx_completada < len(tareas):
            tareas[idx_completada]["estado"] = "completada"
            guardar_tareas(tareas)
            print(f"{Fore.GREEN}Tarea marcada como completada.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Número de tarea inválido.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Debes introducir un número válido.{Style.RESET_ALL}")

def main_tareas():
    esborraPantalla()
    banner_tareas()
    tareas = cargar_tareas()

    while True:
        menu_tareas()

        try:
            opcio = input(f"{Fore.CYAN}Seleccione una opción: {Style.RESET_ALL}")
            options = {
                "1": lambda: mostrar_tareas(tareas),
                "2": lambda: nueva_tarea(tareas),
                "3": lambda: status_tarea(tareas),
                "4": main,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Fore.RED}Opción no válida. Por favor, selecciona una opción correcta.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Debes introducir un número válido.{Style.RESET_ALL}")
# YT
def banner_yt():
    print("""
      _____  _    _  ____  _  _____ _     _     
     |  __ \| |  | |/ __ \| |/ ____| |   | |    
     | |__) | |  | | |  | | | |    | |   | |    
     |  ___/| |  | | |  | | | |    | |   | |    
     | |    | |__| | |__| | | |____| |___| |____
     |_|     \____/ \____/|_|\_____|______|______|
    """)
    print(f"{Fore.MAGENTA}Benvingut a la eina YT_to_MP4{Style.RESET_ALL}")

def descargar_video(url, carpeta_destino, formato, calidad):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.filter(file_extension=formato, res=calidad).first()
        if stream:
            descarga = stream.download(carpeta_destino)
            print("Descarga completada")
            print(f"{Fore.GREEN}Video guardado en: {descarga}{Style.RESET_ALL}")
            return descarga
        else:
            print(f"{Fore.RED}No se encontró una corriente con el formato y calidad seleccionados.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error al descargar el video: {e}{Style.RESET_ALL}")

def main_yt():
    esborraPantalla()
    banner_yt()
    url = input(f"{Fore.MAGENTA}URL del Video: {Style.RESET_ALL}")
    carpeta_destino = input(f"{Fore.MAGENTA}Carpeta de Destino: {Style.RESET_ALL}")
    formato = input(f"{Fore.MAGENTA}Formato del Video (ej. mp4): {Style.RESET_ALL}")
    calidad = input(f"{Fore.MAGENTA}Calidad del Video (ej. 720p): {Style.RESET_ALL}")

    descargar_video(url, carpeta_destino, formato, calidad)
# PASSWD
def generar_contrasena(longitud=12, incluir_mayusculas=True, incluir_simbolos=True):
    caracteres = string.ascii_letters + string.digits
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_simbolos:
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main_passwd():
    esborraPantalla()
    banner_yt()
    print(f"{Fore.MAGENTA}Benvingut a la eina de generar contrasenyes segures :){Style.RESET_ALL}")
    longitud = int(input(f"{Fore.YELLOW}Ingrese la longitud de la contraseña: {Style.RESET_ALL}"))
    incluir_mayusculas = input(f"{Fore.YELLOW}¿Incluir mayúsculas? (s/n): {Style.RESET_ALL}").lower() == 's'
    incluir_simbolos = input(f"{Fore.YELLOW}¿Incluir símbolos? (s/n): {Style.RESET_ALL}").lower() == 's'

    contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_simbolos)
    print(f"Contraseña generada: {contrasena_generada}")
# QR
def main_qr():
    datos = input("Ingresa los datos para el código QR: ")
    generar_codigo_qr(datos)

def generar_codigo_qr(datos):
    if datos:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(datos)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color="black", back_color="white")

        imagen_qr.save("codigo_qr_temporal.png")
        print("Código QR generado y guardado como 'codigo_qr_temporal.png'")

def main():
    esborraPantalla()
    banner_gerijacki()
    
    while True:
        menu_gerijacki()

        try:
            opcio = int(input(f"\nSelecciona una opció: ({Colors.RED}1-8{Colors.RESET}): "))
            
            options = {
                1: main_info, #programa info
                2: main_dic, #programa dic compare
                3: main_tareas, #programa tareas
                4: main_yt, #programa yt
                5: main_passwd, #programa passwd
                6: main_qr,
                7: salir, #sortir
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.RED}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Debes introducir un número válido{Colors.RESET}")


if __name__ == "__main__":
    esborraPantalla()
    main()
