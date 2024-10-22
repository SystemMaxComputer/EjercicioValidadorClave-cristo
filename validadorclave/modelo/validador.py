# TODO: Implementa el código del ejercicio aquí
from abc import abstractmethod, ABC


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada #atributo protegido(se puede acceder a la clase que lo contiene y sus subclases)

    def _validar_longitud(self, clave: str) -> bool:
        return self._longitud_esperada < len(clave)

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
        for letra in clave:
            if letra.isdigit():
                return True

        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        ...


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    @staticmethod
    def contiene_caracter_especial(clave: str) -> bool:
        for letra in clave:
            if letra in "@_#$%":
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

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
