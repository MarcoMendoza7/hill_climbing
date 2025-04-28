import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Regreso al inicio
    return total

def hill_climbing(ciudades, coord):
    ruta = ciudades[:]
    random.shuffle(ruta)
    mejora = True

    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta, coord)

        for i in range(len(ruta)):
            for j in range(i + 1, len(ruta)):
                ruta_tmp = ruta[:]
                ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                nueva_dist = evalua_ruta(ruta_tmp, coord)

                if nueva_dist < dist_actual:
                    ruta = ruta_tmp
                    mejora = True
                    dist_actual = nueva_dist

    return ruta, dist_actual
