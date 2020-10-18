from pyeasyga import pyeasyga
import random

# setup data
data = [{'name': 'box1', 'value': 4, 'weight': 12},
        {'name': 'box2', 'value': 2, 'weight': 1},
        {'name': 'box3', 'value': 10, 'weight': 4},
        {'name': 'box4', 'value': 1, 'weight': 1},
        {'name': 'box5', 'value': 2, 'weight': 2}]

ga = pyeasyga.GeneticAlgorithm(data)        # initialise the GA with data

def mutate(individual):
    index = random.randrange(len(individual))
    individual[index] = 0
    print(individual)

ga.mutate_function = mutate

# define a fitness function
def fitness(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        #print("Selected: ", selected, "; Box: ", box)
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 15:
        values = 0
    return values

ga.fitness_function = fitness               # set the GA's fitness function
ga.run()                                    # run the GA
print(ga.best_individual())                 # print the GA's best solution