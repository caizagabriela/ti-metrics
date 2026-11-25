import pytest
from src.parsers.csv_parser import CSVLogParser
from src.parsers.json_parser import JSONLogParser


def test_leer_logs():
    parser = CSVLogParser("data/logs.csv")

    registros = parser.leer()

    assert len(registros) == 6
    assert isinstance(registros[0]["estado"], int)


def test_leer_eventos():
    parser = JSONLogParser("data/events.json")

    eventos = parser.leer()

    assert len(eventos) == 3

    ids = [evento["event_id"] for evento in eventos]

    assert len(ids) == len(set(ids))

def test_encapsulamiento_ruta_archivo():
    parser = CSVLogParser("data/logs.csv")

    assert parser.ruta_archivo == "data/logs.csv"

    with pytest.raises(AttributeError):
        parser.ruta_archivo = "otra_ruta.csv"