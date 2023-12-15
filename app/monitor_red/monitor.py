import psutil
import time


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
        print("\nMonitor de Uso de Internet detenido.")

def obtener_datos_de_red():
    datos = psutil.net_io_counters()
    return datos.bytes_sent, datos.bytes_recv

def mostrar_informe(bytes_enviados, bytes_recibidos):
    print(f"Datos Enviados: {bytes_enviados / (1024 ** 2):.2f} MB")
    print(f"Datos Recibidos: {bytes_recibidos / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    main_monitor()