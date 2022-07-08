[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4171016&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 1

La constante de Euler `e` es uno de los números irracionales más importantes. Precisamente por su naturaleza irracional, este número no se puede computar exactamente, pero si es posible calcular aproximaciones a su valor.

La siguiente serie se puede utilizar para calcular una aproximación a `e`:

[//]: # (e \approx \sum_{i=0}^{\infty} \frac{1}{i!} = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots)

![equation](https://latex.codecogs.com/png.latex?e%20%5Capprox%20%5Csum_%7Bi%3D0%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7B1%7D%7Bi%21%7D%20%3D%201%20&plus;%201%20&plus;%20%5Cfrac%7B1%7D%7B2%21%7D%20&plus;%20%5Cfrac%7B1%7D%7B3%21%7D%20&plus;%20%5Ccdots)

Con base en esta serie infinita, resuelva el siguiente problema computacional:

**Problema**: Calcular una aproximación a `e`.
* **Entradas**: El número máximo de iteraciones de la serie a calcular ![n perteneciente a los naturales](https://latex.codecogs.com/png.latex?n%20%5Cin%20%5Cmathbb%7BN%7D).
* **Salidas**: El valor de ![la sumatoria desde 0 hasta n de 1/i!](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20%5Cfrac%7B1%7D%7Bi%21%7D)

En el archivo `euler.py`:

1. Implemente la función `e_cuadratica` con un algoritmo que resuelva el problema en complejidad temporal cuadrática.
2. Implemente la función `e_lineal` con un algoritmo que resuelva el problema en complejidad temporal lineal.

## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux. Las siguientes instrucciones asumen que ud está dentro del directorio del proyecto.

Si no lo ha hecho anteriormente, instalar `gnuplot`

```bash
sudo apt update && sudo apt install gnuplot
```

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

```bash
pip3 install gnuplotlib
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con la especificación del problema.
* (3 pts) La producción cumple parcialmente con la especificación del problema.
* (1 pts) La producción, en su mayor parte, no cumple con la especificación del problema.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Análisis y diseño (5 pts)

* (5 pts) El código cumple totalmente con los requerimientos de complejidad especificados.
* (3 pts) El código cumple con la mayoría de los requerimientos de complejidad especificados.
* (1 pts) El código no cumple con la mayoría de los requerimientos de complejidad especificados.
