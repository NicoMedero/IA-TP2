from datos.persona import *

def britanicoCasaRoja(datos):
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'britanico':
            if persona.get('color') == Color.ROJO.value:
                return 1
            else:
                return 0

def suecoTienePerro(datos):
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'sueco':
            if persona.get('mascota') == Mascota.PERRO.value:
                return 1
            else:
                return 0

def danesTomaTe(datos):
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'danes':
            if persona.get('bebida') == Bebida.TE.value:
                return 1
            else:
                return 0


def casaVerdeIzqACasaBlanca(datos):
    casaBlanca = []
    casaVerde = []
    for index, persona in enumerate(datos):
        if persona.get('color') == Color.BLANCO.value:
            casaBlanca = persona.get('casa')
        if persona.get('color') == Color.VERDE.value:
            casaVerde = persona.get('casa')
    
    if casaBlanca == Casa.CUARTA.value:
        if casaVerde == Casa.QUINTA.value:
            return 1
        else:
            return 0
    
    if casaBlanca == Casa.TERCERA.value:
        if casaVerde == Casa.CUARTA.value:
            return 1
        else:
            return 0

    if casaBlanca == Casa.SEGUNDA.value:
        if casaVerde == Casa.TERCERA.value:
            return 1
        else:
            return 0

    if casaBlanca == Casa.PRIMERA.value:
        if casaVerde == Casa.SEGUNDA.value:
            return 1
        else:
            return 0

    return 0

def casaVerdeTomaTe(datos):
    for index, persona in enumerate(datos):
        if persona.get('color') == Color.VERDE.value:
            if persona.get('bebida') == Bebida.TE.value:
                return 1
            else:
                return 0

def fumaPallMallTienePajaro(datos):
    for index, persona in enumerate(datos):
        if persona.get('cigarrillo') == Cigarrillo.PALMALL.value:
            if persona.get('mascota') == Mascota.PAJARO.value:
                return 1
            else:
                return 0

def casaAmarillaFumaDunhill(datos):
    for index, persona in enumerate(datos):
        if persona.get('color') == Color.AMARILLO.value:
            if persona.get('cigarrillo') == Cigarrillo.DUNHILL.value:
                return 1
            else:
                return 0

def casaDelCentroTomaLeche(datos):
    return 1 if datos[2].get('bebida') == Bebida.LECHE.value else 0

def noruegoEnPrimeraCasa(datos):
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'noruego':
            if persona.get('casa') == Casa.PRIMERA.value:
                return 1
            else:
                return 0

def fumaBrendsYVecinoTieneGato(datos):
    ubicacion = 0

    for index, persona in enumerate(datos):
        if persona.get('cigarrillo') == Cigarrillo.BRENDS.value:
            ubicacion = index
            continue
    
    if ubicacion == 4:
        return 1 if datos[3].get('mascota') == Mascota.GATO.value else 0
    else:
        if ubicacion == 0:
            return 1 if datos[1].get('mascota') == Mascota.GATO.value else 0
        else:
            if (
                datos[ubicacion+1].get('mascota') == Mascota.GATO.value or
                datos[ubicacion-1].get('mascota') == Mascota.GATO.value
            ):
                return 1
            else:
                return 0

def tieneCaballoYVecinoFumaDunhill(datos):
    ubicacion = 0

    for index, persona in enumerate(datos):
        if persona.get('mascota') == Mascota.CABALLO.value:
            ubicacion = index
            continue
    
    if ubicacion == 4:
        return 1 if datos[3].get('cigarrillo') == Cigarrillo.DUNHILL.value else 0
    else:
        if ubicacion == 0:
            return 1 if datos[1].get('cigarrillo') == Cigarrillo.DUNHILL.value else 0
        else:
            if (
                datos[ubicacion+1].get('cigarrillo') == Cigarrillo.DUNHILL.value or
                datos[ubicacion-1].get('cigarrillo') == Cigarrillo.DUNHILL.value
            ):
                return 1
            else:
                return 0

def fumaBluemastersYBebeCerveza(datos):
    for index, persona in enumerate(datos):
        if persona.get('cigarrillo') == Cigarrillo.BLUEMASTERS.value:
            if persona.get('bebida') == Bebida.CERVEZA.value:
                return 1
            else:
                return 0


def alemanFumaPrince(datos):
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'aleman':
            if persona.get('cigarrillo') == Cigarrillo.PRINCE.value:
                return 1
            else:
                return 0

def noruegoJuntoACasaAzul(datos):
    ubicacion = 0
    for index, persona in enumerate(datos):
        if persona.get('nacionalidad') == 'noruego':
            ubicacion = index
            continue
    
    if ubicacion == 4:
        return 1 if datos[3].get('color') == Color.AZUL.value else 0
    else:
        if ubicacion == 0:
            return 1 if datos[1].get('color') == Color.AZUL.value else 0
        else:
            if (
                datos[ubicacion+1].get('color') == Color.AZUL.value or
                datos[ubicacion-1].get('color') == Color.AZUL.value
            ):
                return 1
            else:
                return 0


def fumaBrendsYVecinoTomaAgua(datos):
    ubicacion = 0

    for index, persona in enumerate(datos):
        if persona.get('cigarrillo') == Cigarrillo.BRENDS.value:
            ubicacion = index
            continue
    
    if ubicacion == 4:
        return 1 if datos[3].get('bebida') == Bebida.AGUA.value else 0
    else:
        if ubicacion == 0:
            return 1 if datos[1].get('bebida') == Bebida.AGUA.value else 0
        else:
            if (
                datos[ubicacion+1].get('bebida') == Bebida.AGUA.value or
                datos[ubicacion-1].get('bebida') == Bebida.AGUA.value
            ):
                return 1
            else:
                return 0