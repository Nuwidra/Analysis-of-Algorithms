def contar_rutas_mas_cortas(C):

    # Caso base de la ruta
    if C[0][0] == 1:
        return 0

    for i in range(len(C)):
        C[i][0] = 1
    for j in range(len(C[2])):
        C[0][j] = 1

    # Comprobación de la ruta
    for k in range(1, len(C)):

        for z in range(1, len(C[k])):

            # Cuando se pasa por el laberinto (caso base de está iteración)
            if C[k][z] == 1:
                C[k][z] = 0

            else:
                C[k][z] = C[k - 1][z] + C[k][z - 1]

    return C[len(C) - 1][len(C[k]) - 1]

    # Colaboración con compañeros (Compartir ideas y propuestas)
    # Está tarea estaba demasiada díficil desde mi pespectiva :(