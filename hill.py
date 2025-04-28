import math
import random

# Coordenadas de las ciudades
coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754472859146, -103.34625354877137),
    'Monterrey': (25.69161110159454, -100.321838480256),
    'QuintanaRoo': (21.163111924844458, -86.80231502121464),
    'Michohacan': (19.701400113725654, -101.20829680213464),
    'Aguascalientes': (21.87641043660486, -102.26438663286967),
    'CDMX': (19.432713075976878, -99.13318344772986),
    'QRO': (20.59719437542255, -100.38667040246602)
}

# Calcular distancia euclidiana entre dos coordenadas
def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Evaluar la distancia total de una ruta
def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    # Regreso a la ciudad de inicio
    total += distancia(coord[ruta[-1]], coord[ruta[0]])
    return total

# Algoritmo Hill Climbing
def hill_climbing():
    ruta = list(coord.keys())  # Lista de nombres de ciudades
    random.shuffle(ruta)  # Mezcla inicial
    mejora = True

    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta)

        for i in range(len(ruta)):
            for j in range(i + 1, len(ruta)):
                ruta_tmp = ruta[:]
                # Intercambiar dos ciudades
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                dist = evalua_ruta(ruta_tmp)
                if dist < dist_actual:
                    ruta = ruta_tmp
                    mejora = True
                    break
            if mejora:
                break
    return ruta

if __name__ == "__main__":
    ruta_optima = hill_climbing()
    print("Ruta óptima:", ruta_optima)
    print("Distancia total:", evalua_ruta(ruta_optima))

