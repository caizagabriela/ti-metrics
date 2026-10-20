from unittest.mock import Mock, patch

from src.services.api_client import obtener_geolocalizacion


@patch("src.services.api_client.requests.get")
def test_obtener_geolocalizacion(mock_get):
    respuesta = Mock()
    respuesta.json.return_value = {
        "status": "success",
        "query": "8.8.8.8",
        "country": "United States",
        "regionName": "Virginia",
        "city": "Ashburn"
    }
    respuesta.raise_for_status.return_value = None
    mock_get.return_value = respuesta

    resultado = obtener_geolocalizacion("8.8.8.8")

    assert resultado["estado"] == "ok"
    assert resultado["ip"] == "8.8.8.8"
    assert resultado["pais"] == "United States"
    mock_get.assert_called_once()


@patch("src.services.api_client.requests.get")
def test_error_de_conexion(mock_get):
    import requests

    mock_get.side_effect = requests.ConnectionError("Sin conexión")

    resultado = obtener_geolocalizacion("8.8.8.8")

    assert resultado["estado"] == "error"
    assert "mensaje" in resultado