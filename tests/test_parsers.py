import json

from src.parsers.csv_parser import leer_logs
from src.parsers.json_parser import leer_eventos


def test_leer_logs(tmp_path):
    archivo = tmp_path / "logs.csv"
    archivo.write_text(
        "timestamp,ip,usuario,metodo,ruta,estado\n"
        "2026-10-01,8.8.8.8,Ana,GET,/login,500\n",
        encoding="utf-8"
    )

    resultado = leer_logs(archivo)

    assert len(resultado) == 1
    assert resultado[0]["estado"] == 500
    assert isinstance(resultado[0]["estado"], int)


def test_eliminar_eventos_duplicados(tmp_path):
    archivo = tmp_path / "events.json"
    eventos = [
        {"event_id": 1, "tipo": "login"},
        {"event_id": 1, "tipo": "login"},
        {"event_id": 2, "tipo": "error"}
    ]

    archivo.write_text(
        json.dumps(eventos),
        encoding="utf-8"
    )

    resultado = leer_eventos(archivo)

    assert len(resultado) == 2
    assert [evento["event_id"] for evento in resultado] == [1, 2]