import random
from pyeasyga import pyeasyga

# setup seed data
seed_data = [0,2,1,4,3]

# initialise the GA
ga = pyeasyga.GeneticAlgorithm(
    seed_data,
    population_size=300
    )

# define and set function to create a candidate solution representation
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual

ga.create_individual = create_individual

# define a fitness function
def fitness (individual, data):
    fitness = 0
    #print("indi: ", individual)
    for i, number in enumerate(individual):
        if i+1 < len(individual):
            if number < individual[i+1]:
                fitness += 1
            else:
                fitness -= 1
            if i != 0:
                if number > individual[i-1]:
                    fitness += 1
                else:
                    fitness -= 1
        else:
            if number > individual[i-1]:
                fitness += 1
            else:
                fitness = 0
    return fitness

ga.fitness_function = fitness       # set the GA's fitness function
ga.run()                            # run the GA

print(ga.best_individual())