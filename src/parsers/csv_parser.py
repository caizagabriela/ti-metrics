import csv
from src.parsers.base_parser import BaseLogParser


class CSVLogParser(BaseLogParser):

    def leer(self):
        with open(
            self.ruta_archivo,
            "r",
            encoding="utf-8",
            newline=""
        ) as archivo:

            lector = csv.DictReader(archivo)
            registros = list(lector)

        for registro in registros:
            registro["estado"] = int(registro["estado"])

        return registros