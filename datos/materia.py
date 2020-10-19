from enum import Enum

class MateriaClass:
    def __init__(self, name, dia1, dia2, t1, t2, hi1, hi2, hf1, hf2):
        self.name = name
        self.dia1 = dia1
        self.dia2 = dia2
        self.t1 = t1
        self.t2 = t2
        self.hi1 = hi1
        self.hi2 = hi2
        self.hf1 = hf1
        self.hf2 = hf2

class SimpleMateria:
    def __init__(self, name):
        self.name = name


class Values3(Enum):
    CERO = [0,0,0]
    UNO = [0,0,1]
    DOS = [0,1,0]
    TRES = [0,1,1]
    CUATRO = [1,0,0]
    CINCO = [1,0,1]
    SEIS = [1,1,0]
    SIETE = [1,1,1]
    

class Values2(Enum):
    CERO = [0,0]
    UNO = [0,1]
    DOS = [1,0]
    TRES = [1,1]


class Materia(Enum):
    CERO = Values3.CERO.value
    UNO = Values3.UNO.value
    DOS = Values3.DOS.value
    TRES = Values3.TRES.value
    CUATRO = Values3.CUATRO.value
    CINCO = Values3.CINCO.value
    SEIS = Values3.SEIS.value
    SIETE = Values3.SIETE.value

class Turno(Enum):
    MAÑANA = Values2.CERO.value
    TARDE = Values2.UNO.value
    NOCHE = Values2.DOS.value
    NA = Values2.TRES.value

class Dia(Enum):
    LUNES = Values3.CERO.value
    MARTES = Values3.UNO.value
    MIERCOLES = Values3.DOS.value
    JUEVES = Values3.TRES.value
    VIERNES = Values3.CUATRO.value
    SABADO = Values3.CINCO.value
    NA = Values3.SEIS.value
    NAA = Values3.SIETE.value

class Horario(Enum):
    CERO = Values3.CERO.value
    UNO = Values3.UNO.value
    DOS = Values3.DOS.value
    TRES = Values3.TRES.value
    CUATRO = Values3.CUATRO.value
    CINCO = Values3.CINCO.value
    NA = Values3.SEIS.value
    NAA = Values3.SIETE.value


def aplica(list):
    if(
        list == Values3.CERO.value or
        list == Values3.SEIS.value or
        list == Values3.SIETE.value
    ):
        return False
    else:
        return True