import json

# Cargar datos desde un archivo JSON
def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna una lista vacía si el archivo no existe o está corrupto

# Guardar datos en un archivo JSON
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
