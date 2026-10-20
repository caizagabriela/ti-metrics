import csv


def leer_logs(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        registros = list(lector)

    for registro in registros:
        registro["estado"] = int(registro["estado"])

    return registros