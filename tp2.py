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

ga = GeneticAlgorithm(data, population_size=100,
                            generations=20,
                            crossover_probability=0.8,
                            mutation_probability=0.9,
                            elitism=True,
                            maximise_fitness=True)

def fitness (individual, data):
    fitness = 0
    materiasRep = []
    
    #materiasSelec = []

    if individual.count(1) <= 6:        #con esto controlo cuantas materias selecciono de data. (ahora me quedo solo con individuos que tienen 6 materias MAX)
        for (selected, (materia)) in zip(individual, data):
            if selected:                #con esto veo unicamente las materias seleccionadas (una por una)
                #print(materia.get('materia'))
                #print(individual.count(1))
                
                fitness -= materiasRep.count(materia.get('materia'))    #resto la cantidad de veces que se repite una materia
                
                materiasRep.append(materia.get('materia'))
                #materiasSelec.append(materia)
                
                if (materia.get('materia') == [1, 0, 0]):
                    fitness += 1

                #print(materia)
    return fitness

ga.fitness_function = fitness
ga.run()
print (ga.best_individual()[1][0].get('materia'))