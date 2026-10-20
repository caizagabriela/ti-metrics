import requests


def obtener_geolocalizacion(ip):
    url = f"http://ip-api.com/json/{ip}"
    parametros = {
        "fields": "status,message,query,country,regionName,city"
    }

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=5
        )
        respuesta.raise_for_status()
        datos = respuesta.json()

        if datos.get("status") != "success":
            return {
                "ip": ip,
                "estado": "error",
                "mensaje": datos.get("message", "IP no disponible")
            }

        return {
            "ip": datos.get("query", ip),
            "estado": "ok",
            "pais": datos.get("country"),
            "region": datos.get("regionName"),
            "ciudad": datos.get("city")
        }

    except (requests.RequestException, ValueError) as error:
        return {
            "ip": ip,
            "estado": "error",
            "mensaje": str(error)
        }