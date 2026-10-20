TI-Metrics — Hito 1

Descripción:

TI-Metrics es un proyecto en Python que procesa registros de logs en CSV y eventos 
en JSON para obtener métricas básicas y consultar información geográfica 
aproximada de direcciones IP mediante una API pública.

Funcionalidades:

- Lectura de registros CSV.
- Lectura de eventos JSON y eliminación de duplicados por "event_id".
- Cálculo del total de logs y de los errores HTTP 500.
- Cálculo del porcentaje de errores HTTP 500.
- Identificación de IPs críticas con dos o más errores HTTP 500.
- Consulta de geolocalización aproximada mediante una API pública.
- Generación de un reporte JSON.
- Pruebas automatizadas con "pytest".

Requisitos:

- Python 3.
- Dependencias indicadas en "requirements.txt".

Instalación:

python -m pip install -r requirements.txt

Ejecución:

Desde la carpeta principal del proyecto:

python main.py

El reporte se genera en "data/resumen.json".

Pruebas:

pytest -v

Estructura del proyecto:

- "data/": archivos de entrada y reporte generado.
- "src/parsers/": lectura de CSV y JSON.
- "src/services/": consultas a la API.
- "tests/": pruebas automatizadas.
- "main.py": ejecución principal del programa.

Consideraciones:

La geolocalización por IP es aproximada y depende de la disponibilidad de la API. 
Los datos de ejemplo son ficticios y las direcciones IP utilizadas no demuestran 
que sus propietarios hayan generado los registros.

Este proceso corresponde al Hito 1.