# TODO: Implementa el código del ejercicio aquí
from abc import abstractmethod, ABC


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada < len(clave):
            return True

        return False

    @staticmethod
    def _contiene_mayuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True

        return False

    @staticmethod
    def _contiene_minuscula(clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True

        return False

    @staticmethod
    def _contiene_numero(clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True

        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    @staticmethod
    def contiene_caracter_especial(clave: str) -> bool:
        for caracter in clave:
            if caracter == "@" or caracter == "_" or caracter == "#" or caracter == "$" or caracter == "%":
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    @staticmethod
    def contiene_calisto(clave: str) -> bool:
        if "calisto" in str.lower(clave):
            mayusculas = sum(1 for caracter in clave if caracter.isupper())
            if 2 <= mayusculas < 7:
                return True
            return False
        return False

    def es_valida(self, clave: str) -> bool:
        pass


class Validador:
    pass
