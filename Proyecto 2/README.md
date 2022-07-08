# IC-3002 Proyecto 2 #

Esqueleto para el proyecto de algoritmos probabilísticos para el curso IC-3002 Análisis de Algoritmos.

Este proyecto requiere python3.

Para instalar las dependencias correr:

```bash
pip3 install -r requirements.txt
```

Para correr todas las pruebas automatizadas:

```bash
pytest
```

Para correr solo algunas pruebas automatizadas, por ejemplo todas las pruebas cuyo nombre inicia con `test_validar`:

```bash
pytest -v -k "test_validar" dominio_tsp_test.py
```

## Diseño del dominio ##

Las soluciones se representan como listas de vértices, cada vértice representado como un número natural, de acuerdo a la estrategia planteada en la lectura de algoritmos probabilísticos. 

La clase abstracta `Dominio` no debe ser implementada, simplemente especifica la interfaz de operaciones que deben ser implementadas.

La clase de `DominioTSP` extiende a `Dominio`, representa el dominio de soluciones al problema del vendedor viajero (TSP). Esta clase se utilizará en el algoritmo genético. 
