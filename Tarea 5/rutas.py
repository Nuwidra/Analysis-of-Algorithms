def encontrar_ruta(C):

  matriz = crear_la_matriz(C)
  filas = 0
  columnas = 0

  matriz[filas][columnas] = 1

  # La verificación de la matriz
  matriz = auxiliar_encontrar_ruta(C, filas, columnas, matriz)
  
  # Se hace la verificación de cuando esté al final de la matriz dada
  if matriz[len(C)-1][len(C[0])-1] == 1:
    return matriz

  return []

def auxiliar_encontrar_ruta(C, filas, columnas, matriz):

  # Para cuando: 
  if (filas == len(C)-1) and (columnas == len(C[0])-1):
    return matriz

  # POSIBLES MOVIMIENTOS
  if columnas == 0 and filas == 0:
    if C[filas][columnas+1] == 0 and matriz[filas][columnas+1] == 0:
      columnas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

    elif C[filas+1][columnas] == 0 and matriz[filas+1][columnas] == 0:
      filas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

  # Cuando llega a la última columna
  # Puede bajar de fila o pasar al número de la izquierda
  elif columnas == (len(C[0])-1):
    if C[filas+1][columnas] == 0 and matriz[filas+1][columnas] == 0:
      filas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)
    elif C[filas][columnas-1] == 0 and matriz[filas][columnas-1] == 0:
      columnas -= 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

  # MOVIMIENTOS CUANDO NO ESTÁ EN EL BORDE
  elif columnas < (len(C[0])-1) and filas < (len(C)-1):
    
    # Para seguir con al siguiente columna
    if C[filas][columnas+1] == 0 and matriz[filas][columnas+1] == 0:
      columnas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

    # Para seguir con la siguiente fila
    if  C[filas+1][columnas] == 0 and matriz[filas+1][columnas] == 0:
      filas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)
  
    # Para subir de columna, o sea de derecha a izquierda (devolverse)
    elif C[filas][columnas-1] == 0 and matriz[filas][columnas-1] == 0:
      columnas -= 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

    # Para subir de fila, o sea de abajo a arriba (devolverse)
    elif C[filas-1][columnas] == 0 and matriz[filas][columnas] == 0:
      filas -= 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

  #Este es en caso de que 'y' esten dentro del rango general de movimientos por lo que se prueban todos los posibles movimientos excepto bajar
  elif columnas < (len(C[0])-1):

    # Derecha
    if C[filas][columnas+1] == 0 and matriz[filas][columnas+1] == 0:
      columnas += 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)

    # Izquierda
    elif C[filas][columnas-1] == 0 and matriz[filas][columnas-1] == 0:
      columnas -= 1

      # Como la bandera que va poniendo por donde pasa
      matriz[filas][columnas] = 1
      return auxiliar_encontrar_ruta (C, filas, columnas, matriz)
 
  matriz[filas][columnas] = 0
  return matriz

def crear_la_matriz (C):
  matriz = []
  for i in range(len(C)):
      matriz.append([])
      for j in range(len(C[0])):
          matriz[i].append(0)
  return matriz