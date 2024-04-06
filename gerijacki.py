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
import subprocess
import platform
import json
import time
import datetime
import csv
import qrcode
from colorama import init, Fore, Style, Back

def banner_update():
    banner = f"""
    {Fore.BLUE}
    ooooo  oooo oooooooooo  ooooooooo        o      ooooooooooo ooooooooooo 
     888    88   888    888  888    88o     888     88  888  88  888    88  
     888    88   888oooo88   888    888    8  88        888      888ooo8    
     888    88   888         888    888   8oooo88       888      888    oo  
      888oo88   o888o       o888ooo88   o88o  o888o    o888o    o888ooo8888 

    {Style.RESET_ALL}"""
    print(banner)


def ejecutar_comando(comando):
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida_stdout, salida_stderr = proceso.communicate()
    salida_stdout_decodificada = salida_stdout.decode('utf-8')
    salida_stderr_decodificada = salida_stderr.decode('utf-8')
    return salida_stdout_decodificada, salida_stderr_decodificada

def update_prog(var_update, var_upgrade):
    try:
        if var_update == True:
            if platform.system() == 'Linux':
                comando = 'sudo apt update'
            else:
                comando = 'winget update'
        if var_upgrade == True:
            if platform.system() == 'Linux':
                comando = 'sudo apt upgrade'
            else:
                comando = 'winget update --all'

        salida_stdout, salida_stderr = ejecutar_comando(comando)

        print("Procesando...:")
        print(f"{Colors.GREEN}{salida_stdout}{Colors.RESET}")
    
    except Exception as e:
        print("Error: ")
        print(f"{Colors.RED}{salida_stderr}{Colors.RESET}")


def update_packet():
    try:
        print(f"{Colors.RED}Introduce el id del paquete que quiere actualizar: {Colors.RESET}", end='')
        paquete = input()
        try:
            if platform.system() == 'Linux':
                comando = f"apt-get install --only-upgrade {paquete}"
            else:
                comando = f'winget upgrade -h --id {paquete}'

            salida_stdout, salida_stderr = ejecutar_comando(comando)
            print("Procesando...:")
            print(f"{Colors.GREEN}{salida_stdout}{Colors.RESET}")
        except:
            print(f"{Colors.YELLOW}Ha sucedido algun error{Colors.RESET}")
    except:
        print(f"{Colors.YELLOW}Introduce un paquete válido!{Colors.RESET}")



# menu update
def menu_update():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Actualitzar todos los programas{Colors.RESET}")
    print(f"{Colors.RED}2. Actualizar solo un programa{Colors.RESET}")
    print(f"{Colors.RED}3. Salir{Colors.RESET}")


# main program actualizar
def main_update():
    esborraPantalla()
    print("Cargando las actualizaciones de las aplicaciones...")
    update_prog(True, False)

    while True:
        menu_update()
        try:
            opcio = int(input(f"\nSelecciona una opción ({Colors.RED}1-3{Colors.RESET}): "))
            
            options = {
                1: lambda: update_prog(False, True),
                2: lambda: update_packet(),
                3: main,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.YELLOW}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.YELLOW}Introduzca un nombre válido{Colors.RESET}")


def banner_gerijacki():
    banner = f"""
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@@%*++++===---:--=*##**+++++++++***=---=#%@@@@@@@@%=:@@@@@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@=+#@@@@@@@@@%%#+-.-=+*#%@@@@@%#*=-:-*%@@@@@@@@@@%*:+@@@@@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@#=#%@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@#%%@@@@@@@@@#=.%@@@@@%%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@+*%@@@@@@@@%%@@%#**%@@@@@@@@@@@@@@%#%%@@%%%@@@@%+.+%%#***#%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@**%@@@@@@%%@#=.  .-.-@@@@@@@@@@@*+*+===*%@%##@%*-:**+*##*##@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%%%@@@@@%+#@@@@@%@@-    -%%. @@@@@@@@@@@=*@@*====+@@*-+-:++=+*****#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#*#*+++**#+#@@##@@:      :  *@@@@@@@@@@@%==+=-=====@@*..--==++++++*@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#++++++++++*%*+%@+       .=%@@@@@@@@@@@@@@*=----===#@%+.:====+=+++*@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@*++++++==::--=#%@%:  .-+#@@@@@@@@@@@@@@@@@@@%*+===+%@%#+ -+++++**:+@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@+=+++=++=--::*%@@@@@@@@@@@@@@@@@@@#@@@@@@@%%%%@@@@@@@@%*- ==+**#**#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@+=++==+=+:-.=#@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@#+::+*#+++=*@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#*+++=+++-:.*%@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@%#= =+-::.:+@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#*++=====:.-#%@@@@@%%%@@%#*#%%%%%%%@@@@@@@@@@@@@@@@%@@@@%*:-=:-=++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@*++===--=:.+%@@@@%#%@@@@@@%%@@%%%@@@%@@@@@%@%+=%@@@##%@@%#=.=+++++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#*+++=--=-.*%@@@#*%@%%###**%@%%@@%##%%%%##**=--=#%@@@@@@@%+ =+++++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%#******+-:#@@@%%@@@%#*#%@%#*#*#%@%%%#**#@@@@@%++%%@%%@@@@#.-+++++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%#**++++++:#@@@@%@@@#+=--++-=%%##*++-:-+=----:-=-#%@@%@@@@%:-++***#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%#*******+:%@@@@@%@@%--=:  .==::........::.  :=--*@@@@@@@@@:-+=+++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%##*****++-#@@@@%*%@#-=. -%%*-: ....   :-#%#: :--%@#*%@@@@@:=+****#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%%###*##**=+@@@@%==%*--  @@@@@.        :@@@@# .--##==%@@@@%:=+++++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%##**####**-#@@@@#--+--: =%@%+          +%%#- :--+-=#@@@@@=-=+++++#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%#######**#*-#@@@@@#*+:::..:.    .:..    .:..:::+*#@@@@@@+:=+*****%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%#*++++*****+-+@@@@@@@+..                    ..*@@@@@@@#-.:::::.::#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%%=:----------::*@@@@@@#-                   .=%@@@@@@%=:----==++++%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%*******+++=--:. -#@@@@@@%+-.            :=*@@@@@@@%=:-===++*#####%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@#-+++++++=-:::-=*###%@@@@@@@@%+::....:-+%@@@@@@@@#=::---==+++##%##%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%-+**=-::-+#%%@@@@@@@%%@@@@@@#+--------+#@@@@@@%#=..:-==+++++**+++%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%-==:-+#@@@@@@@@@@@@@@@@@@@@@@#=......=#@%%@@@@@@@%+..---==---====%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%-::*%@@@@@@@@@@@@@@@@@@@@@%*@@%*+==+*%@@#*#@@@@@@@@%+.:--=====---%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@%-:*%@@@@@@@@@@@@@@@@@@@@@@@.%%%#*++*#%%%:%%#%%@@@%**+=..::::-----=+#@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@+=#@@@@@@@@@@@@@@@@@@@@@@@@.#%%#*++*#%%%.%@@%%%%%+-+**#########%%%##@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@#=#@@@%@@@@@%%#%@@@@@@@@@@%:#%%%#**#%%%%.%@%#=+===*#%%%%%%%%%%%%%%#@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@%**%@%@@@@#+=----==+==--=+*:*%%%%**%%%%%.%%::=+*=+#%@@@@@@@@@@@@%#@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@%*#%%@@@#---:-----: .:.  .:.:*%%*+%%%%%#%@@@%##+*#%@@@@@@@@@@@@%%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@%**%@@@%-:..:..  -. :-:  #%+=%%#*%%%%%%%@@+::=+#%@@@@@@@@@@@@%%%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@#+*#@%++#@%%+@%#+-:. := -+-: .%%%%%%#%%%%%%@@*..:+*#%@@@@@@@@@@@@%%@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@*++++**+**+#+**#*==*- = :+=--.-==============-::++#%@@@@@@@@@@@@%%%@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@%##%%##%*.--=+#%+--==-==-=----:---:-----:::-+*#@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@#@#%.-=++*=-----------:--:-------:----+*#%@@@@@@@@@@%%-#@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@#@@@#@#%.*###*======-=--==-=--=-=--==-==--+*#%%%%%@%@@@@@%+++@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@#@@@@%@%*+===+*%%%%%%%%%%%%%%%%%%%%%%%%%*##%@@@@@@@%###@@@@@@@#%@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@@%%##++++#@@@@@@@@@@@@@@@@%%%%%%%%#%%%###@@@##%@@@@@@@@@@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@@@@%%%%%###%%%%%%%%%%%%%%%@@@%%%%%@@%%%@@#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
{Fore.MAGENTA}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

{Fore.MAGENTA} ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄     ▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ 
{Fore.MAGENTA}    █       █  █ █  █      █      ██       █ █ ▄ █ █  ▄    █  █ █  █       █       █
{Fore.MAGENTA}    █  ▄▄▄▄▄█  █▄█  █  ▄   █  ▄    █   ▄   █ ██ ██ █ █▄█   █  █▄█  █▄     ▄█    ▄▄▄█
{Fore.MAGENTA}    █ █▄▄▄▄▄█       █ █▄█  █ █ █   █  █ █  █       █       █       █ █   █ █   █▄▄▄ 
{Fore.MAGENTA}    █▄▄▄▄▄  █   ▄   █      █ █▄█   █  █▄█  █       █  ▄   ██▄     ▄█ █   █ █    ▄▄▄█
{Fore.MAGENTA}     ▄▄▄▄▄█ █  █ █  █  ▄   █       █       █   ▄   █ █▄█   █ █   █   █   █ █   █▄▄▄ 
{Fore.MAGENTA}    █▄▄▄▄▄▄▄█▄▄█ █▄▄█▄█ █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█ █▄▄▄█   █▄▄▄█ █▄▄▄▄▄▄▄█
{Style.RESET_ALL}
{Fore.GREEN}Bienvenido a mi herramienta multifuncion en python :) 
Elije una de las siguinetes opciones:
{Style.RESET_ALL}
"""
    print(banner)

# menu
def menu_gerijacki():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Info (Informacion del sistema){Colors.RESET}")
    print(f"{Colors.RED}2. Direct-X (Comparador de directorios){Colors.RESET}")
    print(f"{Colors.RED}3. Task (Gestor de tareas){Colors.RESET}")
    print(f"{Colors.RED}4. YT-MP4 (Descargar videos de youtube){Colors.RESET}")
    print(f"{Colors.RED}5. PASSWD (Generador de contraseñas){Colors.RESET}")
    print(f"{Colors.RED}6. Generador QR (Generador de codigos QR){Colors.RESET}")
    print(f"{Colors.RED}7. Monitor consumo (Monitor del consumo de red a tiempo real){Colors.RESET}")
    print(f"{Colors.RED}8. Buscador Archivos (Buscar archivos en el sistema){Colors.RESET}")
    print(f"{Colors.RED}9. Actualizar dispositivo (Busca y actualiza las aplicaciones del sistema){Colors.RESET}")
    print(f"{Colors.RED}10. Sortir{Colors.RESET}")

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
    ooooooooooo ooooo ooooo       ooooooooooo 
    888    88   888   888         888    88  
    888ooo8     888   888         888ooo8    
    888         888   888      o  888    oo  
    o888o       o888o o888ooooo88 o888ooo8888 
                                          
    
    {Colors.RESET}
    ¡Bienvenido a INFO!
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
   ooooo oooo   oooo ooooooooooo   ooooooo   
    888   8888o  88   888    88  o888   888o 
    888   88 888o88   888ooo8    888     888 
    888   88   8888   888        888o   o888 
   o888o o88o    88  o888o         88ooo88   
                                          

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
    op_config = input(f"\nSelecciona una opcion ({Colors.RED}1-3{Colors.RESET}, o 'T' para volver): ")
    
    if op_config == "1":
        VIRUSTOTAL_API_KEY = input(f"{Colors.RED}Introduzca la nueva API de Virustotal: {Colors.RESET}")
        log_moviment("API de Virustotal modificada.")
    elif op_config == "2":
        LOGS_ENABLED = not LOGS_ENABLED  # Invertir el estado actual
        print(f"Sistema de logs {'activat' if LOGS_ENABLED else 'desactivat'}.")
        log_moviment(f"S'ha {'activat' if LOGS_ENABLED else 'desactivat'} el sistema de logs.")
    elif op_config == "3":
        LOGS_FOLDER = input(f"{Colors.RED}Introduzca la nueva carpeta para los logs: {Colors.RESET}")
        log_moviment(f"carpeta de logs modificada a: {LOGS_FOLDER}")
    elif op_config.lower() == "t":
        return
    else:
        print(f"{Colors.YELLOW}Opción no válida.{Colors.RESET}")

    guardar_configuracion()
    print(f"\n{Colors.GREEN}Configuración modificada con exito.{Colors.RESET}")
    log_moviment("Configuración guardada.")

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return "{:.2f} {}".format(size, unit)

def llista_fitxers_directori(directori):
    try:
        log_moviment(f"Se ha mostrado la lista de archivos del directorio: {directori}")
        if os.path.exists(directori):
            print(f"\nContenido de {Colors.RED}{directori}{Colors.RESET}:")
            for root, dirs, files in os.walk(directori):
                for name in dirs:
                    path = os.path.join(root, name)
                    print(f"- {Colors.CYAN}{name}{Colors.RESET} (Directori)")
                for name in files:
                    path = os.path.join(root, name)
                    size = os.path.getsize(path)
                    formatted_size = format_size(size)
                    print(f"  - {Colors.MAGENTA}{name}{Colors.RESET} ({Colors.CYAN}Archivo{Colors.RESET}, {Colors.GREEN}{formatted_size}{Colors.RESET})")
        else:
            print(f"\n{Colors.YELLOW}Error: El directorio {directori} no existe.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al mostrar la lista de archivos: {e}{Colors.RESET}")


# Comparar fitxers
def compara_fitxers(directori1, directori2):
    try:
        log_moviment("Se ha comparado los archivos de los dos directorios.")
        if os.path.exists(directori1) and os.path.exists(directori2):
            llista1 = set(os.listdir(directori1))
            llista2 = set(os.listdir(directori2))

            fitxers_comuns = llista1.intersection(llista2)
            fitxers_exclusius_directori1 = llista1 - fitxers_comuns
            fitxers_exclusius_directori2 = llista2 - fitxers_comuns

            print("\nArchivos comunes:")
            for fitxer in fitxers_comuns:
                ruta_fitxer1 = os.path.join(directori1, fitxer)
                ruta_fitxer2 = os.path.join(directori2, fitxer)

                tipus_fitxer1, mida_fitxer1 = obtenir_info_fitxer(ruta_fitxer1)
                tipus_fitxer2, mida_fitxer2 = obtenir_info_fitxer(ruta_fitxer2)

                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET}), ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")

            print("\nArchivos exclusivos del directorio 1:")
            for fitxer in fitxers_exclusius_directori1:
                ruta_fitxer1 = os.path.join(directori1, fitxer)
                tipus_fitxer1, mida_fitxer1 = obtenir_info_fitxer(ruta_fitxer1)
                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer1}{Colors.RESET}, {Colors.GREEN}{mida_fitxer1} bytes{Colors.RESET})")

            print("\nArchivos exclusivos del directorio 2:")
            for fitxer in fitxers_exclusius_directori2:
                ruta_fitxer2 = os.path.join(directori2, fitxer)
                tipus_fitxer2, mida_fitxer2 = obtenir_info_fitxer(ruta_fitxer2)
                print(f"- {Colors.MAGENTA}{fitxer}{Colors.RESET} ({Colors.CYAN}{tipus_fitxer2}{Colors.RESET}, {Colors.GREEN}{mida_fitxer2} bytes{Colors.RESET})")
        else:
            print(f"\n{Colors.YELLOW}Error: Uno de los directorios no existe.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al comparar los archivos: {e}{Colors.RESET}")

def compara_fitxer(directori1, directori2, nom_fitxer):
    try:
        log_moviment(f"Se ha comparado el archivo: {nom_fitxer}")
        path1 = os.path.join(directori1, nom_fitxer)
        path2 = os.path.join(directori2, nom_fitxer)

        if os.path.exists(path1) and os.path.exists(path2):
            print(f"\nComparando el archivo {Colors.MAGENTA}{nom_fitxer}{Colors.RESET} en los dos directorios:")
            with open(path1, 'rb') as file1, open(path2, 'rb') as file2:
                content1 = file1.read()
                content2 = file2.read()

                if content1 == content2:
                    print(f'El contenido del {Colors.GREEN}archivo és identico{Colors.RESET} en los dos directorios.')
                else:
                    print(f'El contenido del {Colors.YELLOW}archivo és distinto{Colors.RESET} en los dos directorios.')
        else:
            print(f"\n{Colors.YELLOW}Error: Archivo {nom_fitxer} no encontrado en uno de los directorios.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al comparar el archivo: {e}{Colors.RESET}")

def obtenir_info_fitxer(ruta_fitxer):
    try:
        if os.path.isfile(ruta_fitxer):
            tipus_fitxer = "Archivo"
            mida_fitxer = os.path.getsize(ruta_fitxer)
        else:
            tipus_fitxer = "Directorio"
            mida_fitxer = sum(os.path.getsize(os.path.join(ruta_fitxer, f)) for f in os.listdir(ruta_fitxer))
        return tipus_fitxer, mida_fitxer
    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al obtener la información{e}{Colors.RESET}")
        return "", 0


def penja_a_virustotal(nom_fitxer):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': VIRUSTOTAL_API_KEY}

    try:
        log_moviment(f"Se ha subido el archivo a Virustotal: {nom_fitxer}")
        with open(nom_fitxer, 'rb') as file:
            files = {'file': (nom_fitxer, file)}
            response = requests.post(url, files=files, params=params)
            
            # resposta HTTP
            if response.status_code == 200:
                result = response.json()
                print(f"\nResultado:")
                print(f"SHA-256: {result.get('sha256')}")
                print(f"Permalink: {result.get('permalink')}")
                print("Resultado:", result.get('verbose_msg'))
            else:
                print(f"\n{Colors.YELLOW}Error en la solicitud a VirusTotal. Código de respuesta HTTP: {response.status_code}{Colors.RESET}")

    except FileNotFoundError:
        print(f"\n{Colors.YELLOW}Error: Archivo no encontrado: {nom_fitxer}{Colors.RESET}")
    except requests.RequestException as e:
        print(f"\n{Colors.YELLOW}Error en la solicitud a VirusTotal: {e}{Colors.RESET}")

def canviar_directoris():
    global directori1, directori2
    nou_directori1 = input(f"{Colors.RED}Introduzca la ruta al directorio 1: {Colors.RESET}")
    nou_directori2 = input(f"{Colors.RED}Introduzca la ruta al directorio 2: {Colors.RESET}")

    try:
        if os.path.exists(nou_directori1):
            directori1 = nou_directori1
            print(f"\n{Colors.GREEN}Directori 1 modificado con exito.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directorio {nou_directori1} no existe.{Colors.RESET}")

        if os.path.exists(nou_directori2):
            directori2 = nou_directori2
            print(f"\n{Colors.GREEN}Directorio 2 modificado con exito.{Colors.RESET}")
        else:
            print(f"\n{Colors.YELLOW}Error: El directorio {nou_directori2} no existe.{Colors.RESET}")

    except Exception as e:
        print(f"\n{Colors.YELLOW}Error al modificar los directorios: {e}{Colors.RESET}")

# Funció per sortir
def sortir():
    print(f"{Colors.GREEN}Saliendo de l'aplicación. ¡Bye! :){Colors.RESET}")
    exit()

def config():
    mostrar_configuracion()
    configurar_programa()


# menu
def menu_shadowbyte():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Mostrar los archivos del directorio 1{Colors.RESET}")
    print(f"{Colors.RED}2. Mostrar los archivos del directorio 2{Colors.RESET}")
    print(f"{Colors.RED}3. Comparar los dos directorios{Colors.RESET}")
    print(f"{Colors.RED}4. Comparar un archivo específico{Colors.RESET}")
    print(f"{Colors.RED}5. Subir archivo a Virustotal i verificar Malware{Colors.RESET}")
    print(f"{Colors.RED}6. Modificar directorios{Colors.RESET}")
    print(f"{Colors.RED}7. Configuración{Colors.RESET}")
    print(f"{Colors.RED}8. Salir{Colors.RESET}")


def main_dic():
    esborraPantalla()
    cargar_configuracion()
    banner_shadowbyte()
    log_moviment("Aplicación iniciada.")

    global directori1, directori2

    directori1 = input(f"{Colors.RED}Introduzca la ruta del directorio 1: {Colors.RESET}")
    directori2 = input(f"{Colors.RED}Introduzca la ruta del directorio 2: {Colors.RESET}")

    if not os.path.exists(directori1):
        print(f"\n{Colors.YELLOW}Error: El directorio {directori1} no existe.{Colors.RESET}")
        log_moviment(f"Se ha intentado acceder a un directorio que no existe: {directori1}")
        exit

    if not os.path.exists(directori2):
        print(f"\n{Colors.YELLOW}Error: El directori {directori2} no existeix.{Colors.RESET}")
        log_moviment(f"Se ha intentado acceder a un directorio que no existe: {directori2}")
        exit

    while True:
        menu_shadowbyte()
        try:
            opcio = int(input(f"\nSelecciona una opción ({Colors.RED}1-6{Colors.RESET}): "))
            
            options = {
                1: lambda: llista_fitxers_directori(directori1),
                2: lambda: llista_fitxers_directori(directori2),
                3: lambda: compara_fitxers(directori1, directori2),
                4: lambda: compara_fitxer(directori1, directori2, input(f"{Colors.RED}Introduzca el nombre del archivo a comparar: {Colors.RESET}")),
                5: lambda: penja_a_virustotal(input(f"{Colors.RED}Introduzca el nombre del archivo a subir: {Colors.RESET}")),
                6: canviar_directoris,
                7: config,
                8: main,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.YELLOW}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.YELLOW}Introduzca un nombre válido{Colors.RESET}")

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
    {Fore.BLUE}
    ooooooooooo      o       oooooooo8  oooo   oooo  oooooooo8  
    88  888  88     888     888          888  o88   888         
        888        8  88     888oooooo   888888      888oooooo  
        888       8oooo88           888  888  88o           888 
       o888o    o88o  o888o o88oooo888  o888o o888o o88oooo888  
    {Style.RESET_ALL}
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
     oooooooo8   ooooooo   oooo   oooo ooooo  oooo ooooooooooo oooooooooo  ooooooooooo ooooooooooo oooooooooo  
    o888     88 o888   888o  8888o  88   888    88   888    88   888    888 88  888  88  888    88   888    888 
    888         888     888  88 888o88    888  88    888ooo8     888oooo88      888      888ooo8     888oooo88  
    888o     oo 888o   o888  88   8888     88888     888    oo   888  88o       888      888    oo   888  88o   
     888oooo88    88ooo88   o88o    88      888     o888ooo8888 o888o  88o8    o888o    o888ooo8888 o888o  88o8                                                                                                   
    """)
    print(f"{Fore.MAGENTA}Bienvenido a la herramienta de YT_to_MP4{Style.RESET_ALL}")

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
    print(f"{Fore.MAGENTA}Bienvenido a mi herramienta para generar contraseñas seguras :){Style.RESET_ALL}")
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
        print(f"{Fore.GREEN}Código QR generado y guardado como 'codigo_qr_temporal.png'{Style.RESET_ALL}")

# MONITOR RED
def main_monitor():
    try:
        bytes_enviados_inicial, bytes_recibidos_inicial = obtener_datos_de_red()

        while True:
            time.sleep(1)  # Espera 1 segundo
            bytes_enviados_actual, bytes_recibidos_actual = obtener_datos_de_red()

            bytes_enviados = bytes_enviados_actual - bytes_enviados_inicial
            bytes_recibidos = bytes_recibidos_actual - bytes_recibidos_inicial

            mostrar_informe(bytes_enviados, bytes_recibidos)

    except KeyboardInterrupt:
        print(f"{Fore.RED}\nMonitor de Uso de Internet detenido.{Style.RESET_ALL}")

def obtener_datos_de_red():
    datos = psutil.net_io_counters()
    return datos.bytes_sent, datos.bytes_recv

def mostrar_informe(bytes_enviados, bytes_recibidos):
    print(f"{Fore.MAGENTA}Datos Enviados: {bytes_enviados / (1024 ** 2):.2f} MB{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Datos Recibidos: {bytes_recibidos / (1024 ** 2):.2f} MB{Style.RESET_ALL}")

#BUSC FILE
def main_buscFile():
    directorio_base = input(f"{Fore.YELLOW}Ingrese el directorio base para la búsqueda: {Style.RESET_ALL}")
    extension_busqueda = input(f"{Fore.YELLOW}Ingrese la extensión de archivo a buscar (por ejemplo, '.txt'): {Style.RESET_ALL}")

    archivos_encontrados = buscar_archivos(directorio_base, extension_busqueda)

    if archivos_encontrados:
        print(f"{Fore.MAGENTA}Archivos encontrados:{Style.RESET_ALL}")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print(f"{Fore.RED}No se encontraron archivos con la extensión especificada.{Style.RESET_ALL}")
def buscar_archivos(directorio, extension):
    archivos_encontrados = []
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(extension):
                archivos_encontrados.append(os.path.join(root, file))
    return archivos_encontrados

def main():
    esborraPantalla()
    banner_gerijacki()
    
    while True:
        menu_gerijacki()

        try:
            opcio = int(input(f"\nSeleccione una opción: ({Colors.RED}1-8{Colors.RESET}): "))
            
            options = {
                1: main_info, #programa info
                2: main_dic, #programa dic compare
                3: main_tareas, #programa tareas
                4: main_yt, #programa yt
                5: main_passwd, #programa passwd
                6: main_qr, #programa gen QR
                7: main_monitor, #monitor xarxa
                8: main_buscFile, #busc extencio d'arxiu
                9: main_update, #actualitzar
                10: salir, #sortir
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.RED}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Debes introducir un número válido{Colors.RESET}")


if __name__ == "__main__":
    try:
        esborraPantalla()
        main()
    except KeyboardInterrupt:
        salir()

