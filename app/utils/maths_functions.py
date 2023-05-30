import math

def comparar_valor_con_media(valor, media, desvio):
    if valor < media:
        diferencia = abs(valor - media)
        if diferencia > desvio:
            message = "El valor se encuentra por debajo de la media y el desvio es mayor al establecido."
        else:
            message = "El valor se encuentra por debajo de la media pero la diferencia está dentro de los valores del desvío estandar."
    else:
        message = "El valor no está por debajo de la media."
    return message

import statistics
from scipy.stats import t

# Funcion para utilizar Umbral Grubbs
def calcular_umbral_grubbs(lista_valores, alpha):
    n = len(lista_valores)
    t_dist = t(n - 2)
    s = statistics.stdev(lista_valores)
    x_bar = statistics.mean(lista_valores)
    g_max = max(abs(val - x_bar) for val in lista_valores) / s
    t_alpha = t_dist.ppf(1 - alpha / (2 * n))
    umbral = ((n - 1) / (n ** 0.5)) * ((t_alpha ** 2) / (n - 2 + (t_alpha ** 2))) * ((n * (n - 1)) / ((n - 2 + (t_alpha ** 2)) * (n - 2)))
    return umbral * s

def detectar_valor_atipico(lista_valores, nuevo_valor):
    alpha = 0.05
    # umbral = calcular_umbral_grubbs(lista_valores, alpha)
    umbral = 2
    media = statistics.mean(lista_valores)
    desviacion = statistics.stdev(lista_valores)
    z_score = (nuevo_valor - media) / desviacion
    
    if abs(z_score) > umbral:
        message = "El nuevo valor es atípico."
    else:
        if z_score < -1:
            message = f"El nuevo valor no es atípico, pero está {abs(round(z_score, 2))} desviaciones estándar por debajo de la media."
        elif z_score > 1:
            message = f"El nuevo valor no es atípico, pero está {abs(round(z_score, 2))} desviaciones estándar por encima de la media."
        else:
            message = "El nuevo valor no es atípico y se encuentra en los valores de la media esperada."
    return message

import numpy as np

def generar_array_aleatorio(low, high, size):
    return np.random.uniform(low, high, size)