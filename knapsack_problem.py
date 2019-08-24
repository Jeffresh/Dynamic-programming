
def knapsack(valor, peso, numero_objetos, capacidad):
    f = [[0] * capacidad] * numero_objetos
    for j in range(0, capacidad):
        if j < peso[j]:
            f[0][j] = 0
        else:
            f[0 ][j] = valor[j]

    for i in range(0, numero_objetos):
        for j in range(0, capacidad):
            if j < peso[i]:
                f[i][j] = f[i - 1][j]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - peso[i]] + valor[i])

    resultado = f[-1][-1]

    return resultado


if __name__ == '__main__':
    pass
# TODO Implement example