import random

class Brujula:

    def __init__(self, puntos=None):
        if puntos is not None:
            if len(puntos) == 0:
                raise ValueError("Debe haber al menos un punto cardinal")
            self.__puntos_cardinales = puntos
        self.__puntos_cardinales = ("N", "E", "S", "O")

    def es_punto_cardinal(self,punto):
        return punto in self.__puntos_cardinales

    def __comprobar_punto_cardinal(self,punto):
        if not self.es_punto_cardinal(punto):
            raise ValueError("No es un punto cardinal")

    def derecha(self, punto):
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos_cardinales.index(punto) + 1
        return self.__puntos_cardinales[pos % len(self.__puntos_cardinales)]

    def izquierda(self,punto):
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos_cardinales.index(punto) - 1
        return self.__puntos_cardinales[pos]

    def punto_aleatorio(self):
        return random.choice(self.__puntos_cardinales)

class Robot:
    __numero_serie = 0

    @staticmethod
    def es_generacion_valida(generacion):
        return generacion in ("A", "B", "M")

    def __init__(self, alias, generacion):
        Robot.__numero_serie += 1
        self.__numero_serie = Robot.__numero_serie
        self.set_alias(alias)
        self.set_generacion(generacion)
        self.__brujula = Brujula()
        self.__direccion = self.__brujula.punto_aleatorio()

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.numero_serie() == otro.numero_serie()

    def numero_serie(self):
        return self.__numero_serie

    def alias(self):
        return self.__alias

    def set_alias(self, alias):
        self.__alias = alias

    def generacion(self):
        return self.__generacion

    def set_generacion(self, generacion):
        if not Robot.es_generacion_valida(generacion):
            raise ValueError("La generacion no es válida")
        self.__generacion = generacion

    def direccion(self):
        return self.__direccion
