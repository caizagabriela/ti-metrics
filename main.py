import json
from pathlib import Path
from collections import Counter

from src.parsers.csv_parser import leer_logs
from src.parsers.json_parser import leer_eventos
from src.services.api_client import obtener_geolocalizacion


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

logs = leer_logs(DATA_DIR / "logs.csv")
eventos = leer_eventos(DATA_DIR / "events.json")

total_logs = len(logs)

errores_500 = [
    log for log in logs
    if log["estado"] == 500
]

porcentaje_errores = (
    len(errores_500) / total_logs * 100
    if total_logs else 0
)

errores_por_ip = Counter(
    log["ip"] for log in errores_500
)

ips_criticas = [
    ip for ip, cantidad in errores_por_ip.items()
    if cantidad >= 2
]

ips_unicas = list(dict.fromkeys(
    log["ip"] for log in logs
))

geolocalizacion = [
    obtener_geolocalizacion(ip)
    for ip in ips_unicas
]

resumen = {
    "total_logs": total_logs,
    "errores_http_500": len(errores_500),
    "porcentaje_errores_500": round(porcentaje_errores, 2),
    "eventos_unicos": len(eventos),
    "ips_criticas": ips_criticas,
    "geolocalizacion": geolocalizacion
}

ruta_reporte = DATA_DIR / "resumen.json"

with open(ruta_reporte, "w", encoding="utf-8") as archivo:
    json.dump(resumen, archivo, indent=4, ensure_ascii=False)

print("=== TI-METRICS ===")
print(f"Total de logs: {total_logs}")
print(f"Errores HTTP 500: {len(errores_500)}")
print(f"Porcentaje de errores: {porcentaje_errores:.2f}%")
print(f"Eventos únicos: {len(eventos)}")
print(f"IPs críticas: {ips_criticas}")
print(f"Reporte generado: {ruta_reporte}")


