# TI-Metrics — Hito 1

**Engine de Analítica de Logs y Monitoreo de Infraestructura - Programación II.**

## Descripción

TI-Metrics es un proyecto en Python que procesa registros de logs en CSV y eventos en JSON para obtener métricas básicas y consultar información geográfica aproximada de direcciones IP mediante una API pública.

## Funcionalidades

- Lectura de registros CSV.
- Lectura de eventos JSON y eliminación de duplicados por `event_id`.
- Cálculo del total de logs y de los errores HTTP 500.
- Cálculo del porcentaje de errores HTTP 500.
- Identificación de IPs críticas con dos o más errores HTTP 500.
- Consulta de geolocalización aproximada mediante una API pública.
- Generación de un reporte JSON.
- Pruebas automatizadas con `pytest`.

## Requisitos

- Python 3.
- Dependencias indicadas en `requirements.txt`.

## Instalación

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python main.py
```

El reporte se genera en `data/resumen.json`.

## Pruebas

```bash
pytest -v
```

## Estructura del proyecto

- `data/`: archivos de entrada y reporte generado.
- `src/parsers/`: lectura de CSV y JSON.
- `src/services/`: consultas a la API.
- `tests/`: pruebas automatizadas.
- `main.py`: ejecución principal del programa.

## Consideraciones

La geolocalización por IP es aproximada y depende de la disponibilidad de la API. Los datos de ejemplo son ficticios y las direcciones IP utilizadas no demuestran que sus propietarios hayan generado los registros.

---

**Este proceso corresponde al Hito 1.**




Hito 2: Refactorización con Programación Orientada a Objetos (POO)

En este segundo hito se realizó una refactorización del proyecto TI-Metrics, aplicando los principios de la Programación Orientada a Objetos para mejorar la organización, reutilización y mantenimiento del código.

Objetivos implementados

- Abstracción: creación de la clase abstracta "BaseLogParser", que establece una estructura común para los analizadores de archivos.
- Herencia: implementación de las clases "CSVLogParser" y "JSONLogParser", que heredan de "BaseLogParser".
- Encapsulamiento: utilización del atributo protegido "_ruta_archivo" y del decorador "@property" para controlar el acceso a la ruta del archivo.
- Polimorfismo: utilización del método "leer()" en diferentes objetos parsers, permitiendo que cada clase procese su respectivo formato de archivo.
- Diagrama UML: documentación visual de las clases, sus atributos, métodos y relaciones de herencia.

Estructura incorporada

- "src/parsers/base_parser.py": contiene la clase abstracta "BaseLogParser".
- "src/parsers/csv_parser.py": contiene la clase "CSVLogParser".
- "src/parsers/json_parser.py": contiene la clase "JSONLogParser".
- "docs/diagrama_clases.md": contiene el código Mermaid del diagrama UML.
- "docs/diagrama_clases.png": contiene la representación gráfica del diagrama UML.

Pruebas automatizadas

Se actualizaron las pruebas para verificar el funcionamiento de las clases y sus funcionalidades.

Para ejecutar las pruebas se utiliza:

pytest -v

Resultado obtenido:

5 pruebas superadas (5 passed).

Las pruebas verifican:

- Lectura de registros CSV.
- Lectura de eventos JSON y eliminación de duplicados.
- Encapsulamiento de la ruta del archivo.
- Consulta de geolocalización.
- Manejo de errores de conexión.

Resultado del Hito 2

El proyecto mantiene las funcionalidades desarrolladas en Hito 1 y cuenta con una estructura orientada a objetos, clases reutilizables, documentación UML y pruebas automatizadas satisfactorias.