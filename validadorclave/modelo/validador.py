# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion[ABC]:
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        pass

    def _contiene_mayuscula(self, clave: str) -> bool:
        pass

    def _contiene_minuscula(self, clave: str) -> bool:
        pass

    def _contiene_numero(self, clave: str) -> bool:
        pass
    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass
