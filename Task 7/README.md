[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4798684&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 9

Estamos trabajando en un *script* para exportar datos de un sistema de información masivo y almacenarlos en una serie de dispositivos de almacenamiento externo para archivarlos como copias de seguridad. 

Nuestro *script* genera múltiples archivos de datos cada uno posiblemente de distinto tamaño a los demás. Por otro lado, el dispositivo de almacenamiento tiene un límite de capacidad, sabemos que no todos los archivos van a caber en un solo dispositivo.

El problema que queremos resolver es el de seleccionar la mayor cantidad de archivos posibles para ser almacenados en un único dispositivo.

En términos computacionales establecemos el problema:

**Problema**: Dado un conjunto de archivos seleccionar la secuencia de cardinalidad máxima que pueda ser almacenada en un dispositivo de capacidad limitada.

* **Entradas**: Un conjunto de archivos ![`As = {(A_1, t_1), (A_2, t_2), ..., (A_n, t_n)}`](https://latex.codecogs.com/png.latex?%5Cinline%20As%3D%5C%7B%28A_1%2C%20t_1%29%2C%20%28A_2%2C%20t_2%29%2C%20%5Cdots%2C%20%28A_n%2C%20t_n%29%5C%7D) donde cada archivo ![`A_i`](https://latex.codecogs.com/png.latex?A_i) tiene un tamaño ![`t_i`](https://latex.codecogs.com/png.latex?t_i) asociado, y un dispositivo de almacenamiento externo con capacidad ![`D`](https://latex.codecogs.com/png.latex?D), tal que ![`D < sumatoria(t_i)`](https://latex.codecogs.com/png.latex?%5Cinline%20D%20%3C%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20t_i).

* **Salidas**: Una secuencia ![`M = ((A_1, t_1), ..., (A_m, t_m))`](https://latex.codecogs.com/png.latex?%5Cinline%20M%20%3D%20%28%28A_1%2C%20t_1%29%2C%20%5Cdots%2C%20%28A_m%2C%20t_m%29%29) tal que ![`M` es el subconjunto de `As` con cardinalidad máxima](https://latex.codecogs.com/png.latex?%5Cinline%20%7CM%7C%20%3D%20%5Cunderset%7Bm%20%5Cin%20%5Cmathcal%7BP%7D%28As%29%7D%7B%5Cmax%7D%28%7Cm%7C%29) y ![`D >= sumatoria(t_i)` para todos los `t_i` en `M`](https://latex.codecogs.com/png.latex?%5Cinline%20%5Cunderset%7B%28A_i%2C%20t_i%29%20%5Cin%20M%7D%7B%5Csum%20t_i%7D%20%5Cleq%20D).

1. En el archivo `almacenamiento.py`, implemente la función `maximizar(As, D)` con un algoritmo que resuelva el problema planteado utilizando la técnica de programación voraz en complejidad temporal ![`O(n log n)`](https://latex.codecogs.com/png.latex?%5Cmathcal%7BO%7D%28n%5Clog%20n%29).

## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux.

Si no lo ha hecho anteriormente, crear un ambiente virtual para las dependencias

```bash
python3 -m venv .venv
```

Activar el ambiente virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip3 install -r requirements.txt
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con los requerimientos solicitados.
* (3 pts) La producción cumple parcialmente con los requerimientos solicitados.
* (1 pts) La producción, en su mayor parte, no cumple con los requerimientos solicitados.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Diseño del algoritmo (5 pts)

* (5 pts) El código implementa un algoritmo de programación voraz y corre en la complejidad temporal especificada.
* (3 pts) El código implementa un algoritmo de programación voraz  pero no corre en la complejidad temporal especificada.
* (1 pts) El código no implementa un algoritmo de programación voraz.
