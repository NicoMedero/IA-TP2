from pyeasyga.pyeasyga import GeneticAlgorithm
from pyeasyga import pyeasyga
from random import random
from datos.materia import *

data = [
    {'materia': Materia.CERO.value, 'dia1': Dia.LUNES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CERO.value, 'dia1': Dia.MIERCOLES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.UNO.value, 'dia1': Dia.JUEVES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.UNO.value, 'dia1': Dia.SABADO.value, 'dia2': Dia.NA.value, 'turno1': Turno.MAÑANA.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.DOS.value, 'dia1': Dia.MARTES.value, 'dia2': Dia.NA.value, 'turno1': Turno.MAÑANA.value, 'turno2': Turno.NA.value, 'horario1i': Horario.UNO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CUATRO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.DOS.value, 'dia1': Dia.VIERNES.value, 'dia2': Dia.NA.value, 'turno1': Turno.MAÑANA.value, 'turno2': Turno.NA.value, 'horario1i': Horario.UNO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CUATRO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.TRES.value, 'dia1': Dia.VIERNES.value, 'dia2': Dia.LUNES.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NOCHE.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.CERO.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.TRES.value},
    {'materia': Materia.TRES.value, 'dia1': Dia.VIERNES.value, 'dia2': Dia.JUEVES.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NOCHE.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.CERO.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.TRES.value},
    {'materia': Materia.TRES.value, 'dia1': Dia.MARTES.value, 'dia2': Dia.MIERCOLES.value, 'turno1': Turno.MAÑANA.value, 'turno2': Turno.MAÑANA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.TRES.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.TRES.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.LUNES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.MARTES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.MIERCOLES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.JUEVES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.VIERNES.value, 'dia2': Dia.NA.value, 'turno1': Turno.NOCHE.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
    {'materia': Materia.CUATRO.value, 'dia1': Dia.SABADO.value, 'dia2': Dia.NA.value, 'turno1': Turno.MAÑANA.value, 'turno2': Turno.NA.value, 'horario1i': Horario.CERO.value, 'horario2i': Horario.NA.value, 'horario1f': Horario.CINCO.value, 'horario2f': Horario.NA.value},
]

ga = GeneticAlgorithm(data, population_size=1000,
                            generations=20,
                            crossover_probability=0.8,
                            mutation_probability=0.04,
                            elitism=True,
                            maximise_fitness=True)


def supHorario(M1_H1I, M1_H1F, M1_H2I, M1_H2F, M2_H1I, M2_H1F, M2_H2I, M2_H2F):
    if ( M1_H1F < M2_H1I ) and ( M1_H1I > M2_H1F ):
        return False
    else:
        return True

def supDia(M1D1, M1D2, M2D1, M2D2):
    if M1D2 == [1,1,0] or M2D2 == [1,1,0]:
        return M1D1 == M2D1 or M1D2 == M2D1 or M1D1 == M2D2
    else:
        return M1D1 == M2D1 or M1D2 == M2D1 or M1D1 == M2D2 or M1D2 == M2D2


def supTurno(M1T1, M1T2, M2T1, M2T2):
    if M1T2 == [1,1] or M2T2 == [1,1]:
        return M1T1 == M2T1 or M1T2 == M2T1 or M1T1 == M2T2
    else:
        return M1T1 == M2T1 or M1T2 == M2T1 or M1T1 == M2T2 or M1T2 == M2T2

def restricciones(materias):

    suma = 0

    materiaDesc = []

    for m in range(len(materias)):
        for n in range(m + 1, len(materias)):

            if ( supDia(materias[m].get('dia1'),materias[m].get('dia2'),materias[n].get('dia1'),materias[n].get('dia2')) ):

                if ( supTurno(materias[m].get('turno1'), materias[m].get('turno2'), materias[n].get('turno1'), materias[n].get('turno2')) ):

                    if supHorario(
                            materias[m].get('horario1i'), materias[m].get('horario1f'), materias[m].get('horario2i'), materias[m].get('horario2f'), 
                            materias[n].get('horario1i'), materias[n].get('horario1f'), materias[n].get('horario2i'), materias[n].get('horario2f')
                        ):
                        suma += -30

                    else:
                        suma += 10
                else:
                    suma += 20
            else:
                suma += 30

        materiaDesc.append(materias[m].get('materia'))

        if materiaDesc.count(materias[m].get('materia')) > 1:
            suma -= 100


    return suma


def fitness (individual, data):
    fitness = 0
    
    materiasSelec = []

    if individual.count(1) <= 5:        #con esto controlo cuantas materias selecciono de data. (ahora me quedo solo con individuos que tienen 6 materias MAX)
        for (selected, (materia)) in zip(individual, data):
            if selected:                #con esto veo unicamente las materias seleccionadas (una por una)

                materiasSelec.append(materia)

        fitness += restricciones(materiasSelec)

    return fitness

ga.fitness_function = fitness
ga.run()

print (ga.best_individual())

for index, materia in enumerate(ga.best_individual()[1]):
    if materia == 1:
        print(data[index])