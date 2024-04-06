import subprocess
import platform

def banner_update():
    banner = f"""
   ____  _              ____
  / ___|(_)_ __   __ _  | __ ) _   _ _ __ ___   __ _ 
 | |  _| | '_ \ / _` | |  _ \| | | | '_ ` _ \ / _` |
 | |_| | | | | | (_| | | |_) | |_| | | | | | | (_| |
  \____|_|_| |_|\__, | |____/ \__, |_| |_| |_|\__,_|
                |___/         |___/                 
"""
    print(banner)


def ejecutar_comando(comando):
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida_stdout, salida_stderr = proceso.communicate()
    salida_stdout_decodificada = salida_stdout.decode('utf-8')
    salida_stderr_decodificada = salida_stderr.decode('utf-8')
    return salida_stdout_decodificada, salida_stderr_decodificada

def update_prog(var_update, var_upgrade):
    try:
        if var_update:
            if platform.system() == 'Linux':
                comando = 'sudo apt update'
            else:
                comando = 'winget update'
        elif var_upgrade:
            if platform.system() == 'Linux':
                comando = 'sudo apt upgrade'
            else:
                comando = 'winget update --all'

        salida_stdout, salida_stderr = ejecutar_comando(comando)

        print("Salida estándar:")
        print(salida_stdout)
    
    except Exception as e:
        print("Error: ")
        print(salida_stderr)



def update_packet():
    try:
        print(f"Introduce el id del paquete que quiere actualizar: ", end='')
        paquete = input()
        try:
            if platform.system() == 'Linux':
                comando = f"apt-get install --only-upgrade {paquete}"
            else:
                comando = f'winget upgrade -h --id {paquete}'

            salida_stdout, salida_stderr = ejecutar_comando(comando)
            print("Salida estándar:")
            print(salida_stdout)
        except:
            print(f"Ha sucedido algun error")
            print(salida_stderr)
    except:
        print(f"Introduce un paquete válido")



# menu
def menu_update():
    print("\n----- MENU -----")
    print(f"1. Actualitzar tots els programes")
    print(f"2. Actualitzar només un programa")
    print(f"3. Salir")



def main_update():
    
    print("Carregant les actualitzacións de les aplicacións...")
    update_prog(True, False)

    while True:
        menu_update()
        try:
            opcio = int(input(f"\nSelecciona una opción (1-6): "))
            
            options = {
                1: lambda: update_prog(False, True),
                2: lambda: update_packet(),
                }

            if opcio in options:
                options[opcio]()
            else:
                print(f"Opción no válida. Por favor, selecciona una opción correcta.")
        except ValueError:
            print(f"Introduzca un nombre válido")


if __name__ == "__main__":
    main_update()
    
