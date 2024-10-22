# TODO: Implementa el código del ejercicio aquí
from abc import abstractmethod, ABC

from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


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
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 8 caracteres")
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError("La clave debe tener al menos una letra mayúscula")
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError("la clave debe tener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe tener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError("La clave debe tener al menos un caracter especial (@, _, #, $, %)")
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    @staticmethod
    def contiene_calisto(clave: str) -> bool:
        clave_temp: str = clave.lower()
        palabra: str = "calisto"
        index_calisto = 0

        while (index_calisto + len(palabra)) <= len(clave):
            index_calisto = clave_temp.find(palabra, index_calisto)
            if index_calisto >= 0:
                pi = index_calisto
                pf = index_calisto + len(palabra)
                palabra_org = clave[pi:pf]

                contador_may = 0
                for letra in palabra_org:
                    if letra.isupper():
                        contador_may += 1

                if 2 <= contador_may < len(palabra):
                    return True
                else:
                    index_calisto += len(palabra)
            else:
                return False
        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más de 6 caracteres")
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError("La clave debe tener al menos un número")
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError("La clave debe tener la palabra calisto con al menos dos letras mayúsculas pero no todas")
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave) -> bool:
        return self.regla.es_valida(clave)
