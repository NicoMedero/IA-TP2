from pyeasyga import pyeasyga
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


def existenDatosDuplicados(data):
    
    for index, persona in enumerate(data):
        for index1, persona1 in enumerate(data):
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

#Defino la función Fitness
def fitnessFunction(data):
    fitness = 0

    fitness += britanicoCasaRoja(data)
    fitness += suecoTienePerro(data)
    fitness += danesTomaTe(data)
    fitness += casaVerdeIzqACasaBlanca(data)
    fitness += casaVerdeTomaTe(data)
    fitness += fumaPallMallTienePajaro(data)
    fitness += casaAmarillaFumaDunhill(data)
    fitness += casaDelCentroTomaLeche(data)
    fitness += noruegoEnPrimeraCasa(data)
    fitness += fumaBrendsYVecinoTieneGato(data)
    fitness += tieneCaballoYVecinoFumaDunhill(data)
    fitness += fumaBluemastersYBebeCerveza(data)
    fitness += alemanFumaPrince(data)
    fitness += noruegoJuntoACasaAzul(data)
    fitness += fumaBrendsYVecinoTomaAgua(data)

    return fitness


iteraciones = 100000
fitness = 0
maxFitness = 0
datos_mutados = []
datos_cruzados = []
datos_mutados = datos

print("Datos sin mutar: ")
for persona in datos:
    print(persona)

while(iteraciones > 0):

    fitness = fitnessFunction(datos)

    if maxFitness < fitness:
        maxFitness = fitness
    
    if fitness == 15:
        break

    datos_cruzados = cruzamiento(datos)

    datos_mutados = mutate(datos_cruzados)

    if not existenDatosDuplicados(datos_mutados):
        datos = datos_mutados
    
    if not existenDatosInvalidos(datos_mutados):
        datos = datos_mutados

    iteraciones -= 1

print("Fitness: ", maxFitness)
print("Existen datos duplicados: ", existenDatosDuplicados(datos))
print("Existen datos inválidos: ", existenDatosInvalidos(datos))
print("Datos mutados:")
for persona in datos:
    print(persona)