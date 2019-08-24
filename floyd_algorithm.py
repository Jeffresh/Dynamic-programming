def floyd(matriz_costes, matriz_caminos, numero_vertices):
    """
    Algoritmo de Floyd con recuperación de caminos
    """
    for i in range(0, numero_vertices):
        matriz_costes[i][i] = 0

    for k in range(0, numero_vertices):
        for i in range(0, numero_vertices):
            for j in range(0, numero_vertices):

                coste_ikj = matriz_costes[i][k] + matriz_costes[k][j]

                if matriz_costes[i][j] > coste_ikj:
                    matriz_costes[i][j] = coste_ikj
                    matriz_caminos[i][j] = k

    return matriz_costes, matriz_caminos
