"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    conteo = {}

    with open('files\input\data.csv', "r") as file:
        next(file)  # saltar encabezado si lo hay

        for linea in file:
            partes = linea.strip().split(",")

            if not partes or partes[0] == "":
                continue

            letra = partes[0]  # primera columna

            if letra not in conteo:
                conteo[letra] = 0

            conteo[letra] += 1

    # Convertir a lista de tuplas
    resultado = [(k, conteo[k]) for k in conteo]

    return resultado
if __name__ == "__main__":
    print(pregunta_02())
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
