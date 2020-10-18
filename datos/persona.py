from enum import Enum

class Persona:
    def __init__(self, nacionalidad, casa, color, bebida, cigarrillo, mascota):
        self.nacionalidad = nacionalidad
        self.casa = casa
        self.color = color
        self. bebida = bebida
        self.cigarrillo = cigarrillo
        self.mascota = mascota

class Values(Enum):
    UNO = [0,0,1]
    DOS = [0,1,0]
    TRES = [0,1,1]
    CUATRO = [1,0,0]
    CINCO = [1,0,1]
    NA = [1,1,0]
    NAA = [1,1,1]
    NAAA = [0,0,0]

def aplica(list):
    if(
        list == Values.NA.value or
        list == Values.NAA.value or
        list == Values.NAAA.value
    ):
        return False
    else:
        return True

class Casa(Enum):
    PRIMERA = Values.UNO.value
    SEGUNDA = Values.DOS.value
    TERCERA = Values.TRES.value
    CUARTA = Values.CUATRO.value
    QUINTA = Values.CINCO.value
    NA = Values.NA.value
    NAA = Values.NAA.value
    NAAA = Values.NAAA.value

class Color(Enum):
    ROJO = Values.UNO.value
    VERDE = Values.DOS.value
    BLANCO = Values.TRES.value
    AMARILLO = Values.CUATRO.value
    AZUL = Values.CINCO.value
    NA = Values.NA.value
    NAA = Values.NAA.value
    NAAA = Values.NAAA.value

class Bebida(Enum):
    TE = Values.UNO.value
    CAFE = Values.DOS.value
    LECHE = Values.TRES.value
    CERVEZA = Values.CUATRO.value
    AGUA = Values.CINCO.value
    NA = Values.NA.value
    NAA = Values.NAA.value
    NAAA = Values.NAAA.value

class Cigarrillo(Enum):
    PALMALL = Values.UNO.value
    DUNHILL = Values.DOS.value
    BRENDS = Values.TRES.value
    BLUEMASTERS = Values.CUATRO.value
    PRINCE = Values.CINCO.value
    NA = Values.NA.value
    NAA = Values.NAA.value
    NAAA = Values.NAAA.value

class Mascota(Enum):
    PERRO = Values.UNO.value
    PAJARO = Values.DOS.value
    GATO = Values.TRES.value
    CABALLO = Values.CUATRO.value
    PEZ = Values.CINCO.value
    NA = Values.NA.value
    NAA = Values.NAA.value
    NAAA = Values.NAAA.value