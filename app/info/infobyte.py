import os
import shutil
import glob
import speedtest
import psutil
import socket
import platform
import cpuinfo

class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def menu():
    print("\n----- MENU -----")
    print(f"{Colors.RED}1. Speed Test{Colors.RESET}")
    print(f"{Colors.RED}2. Información del sistema{Colors.RESET}")
    print(f"{Colors.RED}3. Información de red{Colors.RESET}")
    print(f"{Colors.RED}4. Información del disco{Colors.RESET}")
    print(f"{Colors.RED}5. Borrar archivos temporales{Colors.RESET}")
    print(f"{Colors.RED}6. Salir{Colors.RESET}")

def banner():
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

def main():
    banner()
    while True:
        menu()

        try:
            opcio = int(input(f"\nSelecciona una opción ({Colors.RED}1-8{Colors.RESET}): "))
            
            options = {
                1: medir_velocidad,
                2: sys_info,
                3: red_info,
                4: disk_info,
                5: temp_del,
                6: salir,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Colors.RED}Opción no válida. Por favor, selecciona una opción correcta.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Debes introducir un número válido{Colors.RESET}")

if __name__ == "__main__":
    main()
