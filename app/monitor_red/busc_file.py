import os

def main_buscFile():
    directorio_base = input("Ingrese el directorio base para la búsqueda: ")
    extension_busqueda = input("Ingrese la extensión de archivo a buscar (por ejemplo, '.txt'): ")

    archivos_encontrados = buscar_archivos(directorio_base, extension_busqueda)

    if archivos_encontrados:
        print("Archivos encontrados:")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print("No se encontraron archivos con la extensión especificada.")
def buscar_archivos(directorio, extension):
    archivos_encontrados = []
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(extension):
                archivos_encontrados.append(os.path.join(root, file))
    return archivos_encontrados

if __name__ == "__main__":
    main_buscFile()
