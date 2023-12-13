import os
import shutil
import glob
import speedtest
import psutil
import socket
import platform
import cpuinfo
import requests
import filecmp
import datetime
import json

# Clase para colores en la consola
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

# Funciones para INFO
def mostrar_menu_info():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Speed Test{Colors.RESET}")
    print(f"{Colors.RED}2. Información del sistema{Colors.RESET}")
    print(f"{Colors.RED}3. Información de red{Colors.RESET}")
    print(f"{Colors.RED}4. Información del disco{Colors.RESET}")
    print(f"{Colors.RED}5. Borrar archivos temporales{Colors.RESET}")
    print(f"{Colors.RED}6. Cambiar directorios{Colors.RESET}")
    print(f"{Colors.RED}7. Configuración{Colors.RESET}")
    print(f"{Colors.RED}8. Salir{Colors.RESET}")

def imprimir_banner_info():
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

def sys_info():
    sistema = platform.system()
    arquitectura = platform.architecture()
    procesador = cpuinfo.get_cpu_info()["brand_raw"]

    print(f"{Colors.GREEN}Información del Sistema:{Colors.RESET}")
    print(f"\t{Colors.GREEN}Sistema Operativo: {sistema}{Colors.RESET}")
    print(f"\t{Colors.GREEN}Arquitectura del Sistema: {arquitectura[0]} {arquitectura[1]}{Colors.RESET}")
    print(f"\t{Colors.GREEN}Procesador: {procesador}{Colors.RESET}")

def salir():
    print(f"{Colors.MAGENTA}¡Hasta luego!{Colors.RESET}")
    exit()

# Clase para DicCompare
class DicCompare:
    def __init__(self):
        self.api_key_virustotal = "964ff6a97060a4512bf3a8047f09964b5a0b6f53055ce5e540e130eb09204b4b"  # Ingresa tu clave API de VirusTotal aquí
        self.configuracion = {
            "directorio_1": "",
            "directorio_2": "",
            "log_file": "diccompare.log",
            "color": True
        }

    def esborraPantalla(self):
        sistema_operativo = platform.system()
        if sistema_operativo == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def cargar_configuracion(self):
        try:
            with open('config.json', 'r') as file:
                self.configuracion = json.load(file)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"{Colors.YELLOW}Error al cargar la configuración: {e}{Colors.RESET}")

    def guardar_configuracion(self):
        try:
            with open('config.json', 'w') as file:
                json.dump(self.configuracion, file, indent=4)
        except Exception as e:
            print(f"{Colors.YELLOW}Error al guardar la configuración: {e}{Colors.RESET}")

    def imprimir_banner_diccompare(self):
        banner_text = f"""
        {Colors.CYAN}
        ╔═══╗───────────╔╗───╔╗
        ║╔═╗║───────────║║───║║
        ║║─╚╬══╦══╦══╦══╣║╔═╗║║╔══╦══╗
        ║║─╔╣╔╗║╔╗║╔╗║╔╗║║║═╣║║║═╣══╣
        ║╚═╝║╔╗║╚╝║╔╗║╚╝║╚╣═╣║║║═╬══║
        ╚═══╩╝╚╩══╩╝╚╩══╩═╩═╝╚╩══╩══╝
        
        {Colors.RESET}
        ¡Bienvenido a DicCompare!
        """

        print(f"{Colors.RED}{banner_text}{Colors.RESET}")

    def log_moviment(self, mensaje):
        with open(self.configuracion["log_file"], 'a') as file:
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{fecha_hora}: {mensaje}\n")

    def mostrar_configuracion(self):
        print(f"{Colors.GREEN}Configuración actual:{Colors.RESET}")
        print(f"\t{Colors.GREEN}Directorio 1: {self.configuracion['directorio_1']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Directorio 2: {self.configuracion['directorio_2']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Archivo de log: {self.configuracion['log_file']}{Colors.RESET}")
        print(f"\t{Colors.GREEN}Color en la consola: {self.configuracion['color']}{Colors.RESET}")

    def configurar_programa(self):
        directorio_1 = input("Ingrese el primer directorio: ")
        directorio_2 = input("Ingrese el segundo directorio: ")
        color_habilitado = input("¿Habilitar color en la consola? (Sí/No): ").lower() == 'si'

        self.configuracion["directorio_1"] = directorio_1
        self.configuracion["directorio_2"] = directorio_2
        self.configuracion["color"] = color_habilitado

        print(f"{Colors.MAGENTA}Configuración actualizada con éxito.{Colors.RESET}")

    def mostra_menu_diccompare(self):
        print("\n----- DicCompare -----")
        print(f"{Colors.RED}1. Listar archivos de un directorio{Colors.RESET}")
        print(f"{Colors.RED}2. Comparar dos directorios{Colors.RESET}")
        print(f"{Colors.RED}3. Comparar contenido de un archivo{Colors.RESET}")
        print(f"{Colors.RED}4. Obtener información de un archivo{Colors.RESET}")
        print(f"{Colors.RED}5. Subir archivo a VirusTotal{Colors.RESET}")
        print(f"{Colors.RED}6. Cambiar directorios{Colors.RESET}")
        print(f"{Colors.RED}7. Configuración{Colors.RESET}")
        print(f"{Colors.RED}8. Salir{Colors.RESET}")

    def llista_fitxers_directori(self, directorio):
        try:
            archivos = os.listdir(directorio)
            print(f"\n{Colors.GREEN}Archivos en el directorio {directorio}:{Colors.RESET}")
            for archivo in archivos:
                print(f"\t- {archivo}")
        except Exception as e:
            print(f"{Colors.YELLOW}Error al listar archivos: {e}{Colors.RESET}")

    def compara_fitxers(self, directorio_1, directorio_2):
        try:
            diferencias = filecmp.dircmp(directorio_1, directorio_2)
            print(f"\n{Colors.GREEN}Diferencias entre {directorio_1} y {directorio_2}:{Colors.RESET}")
            print(f"\t{Colors.GREEN}Archivos únicos en {directorio_1}: {diferencias.left_only}{Colors.RESET}")
            print(f"\t{Colors.GREEN}Archivos únicos en {directorio_2}: {diferencias.right_only}{Colors.RESET}")
            print(f"\t{Colors.GREEN}Archivos diferentes: {diferencias.diff_files}{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}Error al comparar archivos: {e}{Colors.RESET}")

    def compara_fitxer(self, fitxer, directorio_1, directorio_2):
        path_fitxer_1 = os.path.join(directorio_1, fitxer)
        path_fitxer_2 = os.path.join(directorio_2, fitxer)
        try:
            with open(path_fitxer_1, 'r') as f1, open(path_fitxer_2, 'r') as f2:
                contenido_1 = f1.read()
                contenido_2 = f2.read()

                if contenido_1 == contenido_2:
                    print(f"\n{Colors.GREEN}Los contenidos de los archivos {fitxer} son idénticos.{Colors.RESET}")
                else:
                    print(f"\n{Colors.YELLOW}Los contenidos de los archivos {fitxer} son diferentes.{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}Error al comparar el contenido del archivo: {e}{Colors.RESET}")

    def informacio_fitxer(self, fitxer, directorio):
        try:
            path_fitxer = os.path.join(directorio, fitxer)
            info = os.stat(path_fitxer)

            print(f"\n{Colors.GREEN}Información del archivo {fitxer}:{Colors.RESET}")
            print(f"\t{Colors.GREEN}Ruta: {path_fitxer}{Colors.RESET}")
            print(f"\t{Colors.GREEN}Tamaño: {info.st_size} bytes{Colors.RESET}")
            print(f"\t{Colors.GREEN}Fecha de creación: {datetime.datetime.fromtimestamp(info.st_ctime)}{Colors.RESET}")
            print(f"\t{Colors.GREEN}Fecha de última modificación: {datetime.datetime.fromtimestamp(info.st_mtime)}{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}Error al obtener información del archivo: {e}{Colors.RESET}")

    def subir_a_virustotal(self, fitxer, directorio):
        try:
            import requests

            path_fitxer = os.path.join(directorio, fitxer)

            with open(path_fitxer, "rb") as archivo:
                files = {"file": archivo}
                params = {"apikey": self.api_key_virustotal}
                url = "https://www.virustotal.com/vtapi/v2/file/scan"

                response = requests.post(url, files=files, params=params)
                resultado = response.json()

                if resultado["response_code"] == 1:
                    print(f"\n{Colors.GREEN}El archivo {fitxer} ha sido enviado a VirusTotal con éxito.{Colors.RESET}")
                    print(f"{Colors.GREEN}Enlace para ver el informe: {resultado['permalink']}{Colors.RESET}")
                else:
                    print(f"{Colors.YELLOW}Error al enviar el archivo a VirusTotal: {resultado['verbose_msg']}{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.YELLOW}Error al enviar el archivo a VirusTotal: {e}{Colors.RESET}")

# Instanciar y ejecutar el programa
if __name__ == "__main__":
    diccompare = DicCompare()
    diccompare.cargar_configuracion()

    while True:
        diccompare.esborraPantalla()
        diccompare.imprimir_banner_diccompare()
        diccompare.mostra_menu_diccompare()

        opcion = input("\nSelecciona una opción: ")

        if opcion == '1':
            directorio = input("\nIngrese el directorio para listar archivos: ")
            diccompare.llista_fitxers_directori(directorio)
        elif opcion == '2':
            directorio_1 = input("\nIngrese el primer directorio: ")
            directorio_2 = input("Ingrese el segundo directorio: ")
            diccompare.compara_fitxers(directorio_1, directorio_2)
        elif opcion == '3':
            fitxer = input("\nIngrese el nombre del archivo para comparar contenido: ")
            directorio_1 = input("Ingrese el primer directorio: ")
            directorio_2 = input("Ingrese el segundo directorio: ")
            diccompare.compara_fitxer(fitxer, directorio_1, directorio_2)
        elif opcion == '4':
            fitxer = input("\nIngrese el nombre del archivo para obtener información: ")
            directorio = input("Ingrese el directorio del archivo: ")
            diccompare.informacio_fitxer(fitxer, directorio)
        elif opcion == '5':
            fitxer = input("\nIngrese el nombre del archivo para subir a VirusTotal: ")
            directorio = input("Ingrese el directorio del archivo: ")
            diccompare.subir_a_virustotal(fitxer, directorio)
        elif opcion == '6':
            diccompare.cargar_configuracion()
            diccompare.mostrar_configuracion()
        elif opcion == '7':
            diccompare.configurar_programa()
            diccompare.guardar_configuracion()
        elif opcion == '8':
            diccompare.salir()
        else:
            print(f"{Colors.YELLOW}Opción no válida. Intente de nuevo.{Colors.RESET}")


       
