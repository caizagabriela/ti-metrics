import json


def leer_eventos(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        eventos = json.load(archivo)

    eventos_unicos = []
    ids_vistos = set()

    for evento in eventos:
        event_id = evento["event_id"]

        if event_id not in ids_vistos:
            eventos_unicos.append(evento)
            ids_vistos.add(event_id)

    return eventos_unicos