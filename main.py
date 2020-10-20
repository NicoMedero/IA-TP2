from pyeasyga.pyeasyga import GeneticAlgorithm
from datos.persona import *
from datos.condiciones import *
import random

#Primeros datos
datos = [
    {'nacionalidad': 'noruego','casa': Casa.PRIMERA.value,'color': Color.AMARILLO.value,'bebida': Bebida.AGUA.value,'cigarrillo': Cigarrillo.DUNHILL.value,'mascota': Mascota.GATO.value},
    {'nacionalidad': 'aleman','casa': Casa.SEGUNDA.value,'color': Color.AZUL.value,'bebida': Bebida.TE.value,'cigarrillo': Cigarrillo.PRINCE.value,'mascota': Mascota.CABALLO.value},
    {'nacionalidad': 'danes','casa': Casa.TERCERA.value,'color': Color.BLANCO.value,'bebida':Bebida.LECHE.value ,'cigarrillo': Cigarrillo.BLUEMASTERS.value,'mascota': Mascota.PEZ.value},
    {'nacionalidad': 'sueco','casa': Casa.CUARTA.value,'color': Color.VERDE.value,'bebida': Bebida.CAFE.value,'cigarrillo': Cigarrillo.BRENDS.value,'mascota': Mascota.PERRO.value},
    {'nacionalidad': 'britanico','casa': Casa.QUINTA.value,'color': Color.ROJO.value,'bebida': Bebida.CERVEZA.value,'cigarrillo': Cigarrillo.PALMALL.value,'mascota': Mascota.PAJARO.value}
]


def create_individual(data):
    individual = data[:]
    for persona in individual:
        persona.update({'casa': generate_valid_range(random.randrange(0,5))})
        persona.update({'color': generate_valid_range(random.randrange(0,5))})
        persona.update({'bebida': generate_valid_range(random.randrange(0,5))})
        persona.update({'cigarrillo': generate_valid_range(random.randrange(0,5))})
        persona.update({'mascota': generate_valid_range(random.randrange(0,5))})
    return individual

def generate_valid_range(range):
    
    if range == 0:
        return Values.UNO.value
    if range == 1:
        return Values.DOS.value
    if range == 2:
        return Values.TRES.value
    if range == 3:
        return Values.CUATRO.value
    if range == 4:
        return Values.CINCO.value


def existenDatosDuplicados(data):

    for index, persona in enumerate(data):
        if persona == 0 or persona == 1:
            return True
        for index1, persona1 in enumerate(data):
            if persona1 == 0 or persona1 == 1:
                return True
            if index < index1:
                if persona.get('casa') == persona1.get('casa'):
                    return True
                if persona.get('color') == persona1.get('color'):
                    return True
                if persona.get('bebida') == persona1.get('bebida'):
                    return True
                if persona.get('cigarrillo') == persona1.get('cigarrillo'):
                    return True
                if persona.get('mascota') == persona1.get('mascota'):
                    return True
    return False

def existenDatosInvalidos(data):
    
    for persona in data:
        if persona == 0 or persona == 1:
            return True
        if not aplica(persona.get('casa')):
            return True
        if not aplica(persona.get('color')):
            return True
        if not aplica(persona.get('bebida')):
            return True
        if not aplica(persona.get('cigarrillo')):
            return True
        if not aplica(persona.get('mascita')):
            return True
    
    return False


def cruzamiento(data):
    padreAIndex = random.randrange(0,4)
    padreBIndex = random.randrange(0,4)

    while(padreAIndex == padreBIndex):
        padreBIndex = random.randrange(0,4)

    padreA = data[padreAIndex]
    padreB = data[padreBIndex]

    hijoA = {'nacionalidad': padreA.get('nacionalidad'), 'casa': padreA.get('casa'), 'color': padreA.get('color'), 'bebida': padreB.get('bebida'), 'cigarrillo': padreB.get('cigarrillo'), 'mascota': padreB.get('mascota')}
    hijoB = {'nacionalidad': padreB.get('nacionalidad'), 'casa': padreB.get('casa'), 'color': padreB.get('color'), 'bebida': padreA.get('bebida'), 'cigarrillo': padreA.get('cigarrillo'), 'mascota': padreA.get('mascota')}

    nuevos_datos = []

    for index, personas in enumerate(data):
        if index == padreAIndex:
            nuevos_datos.append(hijoA)
        
        if index == padreBIndex:
            nuevos_datos.append(hijoB)
        
        if index != padreAIndex and index != padreBIndex:
            nuevos_datos.append(data[index])
    
    return nuevos_datos

# define and set the GA's mutation operation
def mutate(data):
    if random.randrange(0,1000) <= 1:
        return data

    persona_a_mutar = random.randrange(0,4)
    individuo = data[persona_a_mutar]
    
    atributo_a_mutar = random.randrange(0,4)
    bit_a_mutar = random.randrange(0,2)

    lista_mutada = []

    if atributo_a_mutar == 0:
        lista_mutada = mutarLista(individuo.get('casa'), bit_a_mutar)
        individuo.update({'casa': lista_mutada})
    
    if atributo_a_mutar == 1:
        lista_mutada = mutarLista(individuo.get('color'), bit_a_mutar)
        individuo.update({'color': lista_mutada})
    
    if atributo_a_mutar == 2:
        lista_mutada = mutarLista(individuo.get('bebida'), bit_a_mutar)
        individuo.update({'bebida': lista_mutada})
    
    if atributo_a_mutar == 3:
        lista_mutada = mutarLista(individuo.get('cigarrillo'), bit_a_mutar)
        individuo.update({'cigarrillo': lista_mutada})
    
    if atributo_a_mutar == 4:
        lista_mutada = mutarLista(individuo.get('mascota'), bit_a_mutar)
        individuo.update({'mascota': lista_mutada})

    data[persona_a_mutar].update(individuo)
    
    return data


def mutarLista(lista, bit_a_mutar):
    if lista[bit_a_mutar] == 0:
        lista[bit_a_mutar] = 1
    else:
        lista[bit_a_mutar] = 0
    
    return lista

resultantes = []

#Defino la función Fitness
def fitness(individual, data):
    fitness = 0

    if existenDatosDuplicados(individual):
        fitness -= 1
    
    if existenDatosInvalidos(individual):
        fitness -= 1

    if not existenDatosInvalidos(individual) and not existenDatosDuplicados(individual):
        fitness += britanicoCasaRoja(individual)
        fitness += suecoTienePerro(individual)
        fitness += danesTomaTe(individual)
        fitness += casaVerdeIzqACasaBlanca(individual)
        fitness += casaVerdeTomaTe(individual)
        fitness += fumaPallMallTienePajaro(individual)
        fitness += casaAmarillaFumaDunhill(individual)
        fitness += casaDelCentroTomaLeche(individual)
        fitness += noruegoEnPrimeraCasa(individual)
        fitness += fumaBrendsYVecinoTieneGato(individual)
        fitness += tieneCaballoYVecinoFumaDunhill(individual)
        fitness += fumaBluemastersYBebeCerveza(individual)
        fitness += alemanFumaPrince(individual)
        fitness += noruegoJuntoACasaAzul(individual)
        fitness += fumaBrendsYVecinoTomaAgua(individual)
        resultantes.append({'fitness': fitness, 'individual': individual})

    return fitness

ga = GeneticAlgorithm(
        datos,
        population_size=2000
    )

ga.create_individual = create_individual
ga.fitness_function = fitness

ga.run()

last = resultantes.pop()
print(last.get('individual'))