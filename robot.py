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
        if alias == "":
            raise ValueError("El alias no puede ser un campo vacío")
        Robot.__numero_serie += 1
        self.__numero_serie = Robot.__numero_serie
        self.__alias_robot = alias
        self.set_generacion(generacion)
        self.__brujula = Brujula()
        self.__direccion_robot = self.__brujula.punto_aleatorio()
        self.__distancia_recorrida = 0
        self.__posicion_robot = {"N": 0, "E": 0, "S": 0, "O": 0}

    def __eq__(self, otro):
        if not isinstance(otro, type(self)):
            return NotImplemented
        return self.__numero() == otro.__numero()

    def __numero(self):
        return self.__numero_serie

    def __alias(self):
        return self.__alias_robot

    def __generacion(self):
        return self.__generacion_robot

    def __distancia(self):
        return self.__distancia_recorrida

    def __direccion(self):
        return self.__direccion_robot

    def __posicion(self):
        return self.__posicion_robot

    def __codigo(self):
        return self.__generacion() + str(self.__numero())

    def set_generacion(self, generacion):
        if not Robot.es_generacion_valida(generacion):
            raise ValueError("La generacion no es válida")
        self.__generacion_robot = generacion

    def __anyadir_distancia(self, metros):
        self.__distancia_recorrida += metros

    def __cambiar_posicion(self, metros):
        self.__posicion()[self.__direccion()] += metros

    def girar(self):
        self.__direccion_robot = self.__brujula.derecha(self.__direccion())

    def avanzar(self, metros = 1):
        self.__anyadir_distancia(metros)
        self.__cambiar_posicion(metros)

    def saludar(self):
        print(self.__codigo() + "" + self.__alias(), ": ¡Hola cachocarne!")

    def informacion(self):
        print("Nombre =", self.__alias(),\
              "\nOrientacion =", self.__direccion(),\
              "\nDistancia Total Recorrida =", self.__distancia(),\
              "\nPosición: N =", self.__posicion()["N"],\
                          "E =", self.__posicion()["E"],\
                          "S =", self.__posicion()["S"],\
                          "O =", self.__posicion()["O"])

robot1 = Robot("Bender", "B")
robot1.saludar()
robot1.informacion()
robot1.avanzar()
robot1.girar()
robot1.avanzar(5)
robot1.informacion()
