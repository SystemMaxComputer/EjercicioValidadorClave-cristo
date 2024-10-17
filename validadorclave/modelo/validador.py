# TODO: Implementa el código del ejercicio aquí
from abc import abstractmethod, ABC


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada > len(clave):
            return True
        return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for letra in clave:
            if letra.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        pass

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        pass

    def contiene_caracter_especial(self, clave: str) -> bool:
        pass

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def es_valida(self, clave: str) -> bool:
        pass


class Validador:
    pass
