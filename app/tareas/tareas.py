import csv
import platform
import os
from colorama import init, Fore, Style

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

def esborraPantalla():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def main():
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
                "4": sortir,
            }

            if opcio in options:
                options[opcio]()
            else:
                print(f"{Fore.RED}Opción no válida. Por favor, selecciona una opción correcta.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Debes introducir un número válido.{Style.RESET_ALL}")

if __name__ == "__main__":
    esborraPantalla()
    main()

