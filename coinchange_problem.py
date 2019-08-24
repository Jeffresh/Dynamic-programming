from math import inf


def coinchange(valor, numero_monedas, cambio):
    f = [[0] * cambio] * numero_monedas

    f[0][0] = 0

    for j in range(0, cambio):
        if valor[j] > j:
            f[0][j] = inf
        else:
            f[0][j] = 1 + f[0][j - valor[0]]

    for i in range(1, numero_monedas):
        for j in range(0, cambio):

            if valor[i] > j:
                f[i][j] = f[i - 1][j]
            else:
                f[i][j] = min(f[i - 1][j], 1 + f[i][j - valor[i]])

    resultado = f[-1][-1]

    return resultado


if __name__ == '__main__':
    num_columnas = 4
    num_filas = 3

    f = [[0] * num_columnas] * num_filas
    f[-1][-1] = 10

    print(f[num_filas-1][num_columnas-1])
