from abc import ABC, abstractmethod


class BaseLogParser(ABC):

    def __init__(self, ruta_archivo):
        self._ruta_archivo = ruta_archivo

    @property
    def ruta_archivo(self):
        return self._ruta_archivo

    @abstractmethod
    def leer(self):
        pass