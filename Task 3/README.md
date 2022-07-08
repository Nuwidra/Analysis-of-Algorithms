[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=4280638&assignment_repo_type=AssignmentRepo)
# IC-3002 Tarea corta 3

Considere la siguiente función

![equation](https://latex.codecogs.com/png.latex?f%28n%29%20%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Csum_%7Bj%3D1%7D%5E%7Bi%7D%20%5Csum_%7Bk%3Dj%7D%5E%7Bi&plus;j%7D1)

Con base en esta serie, resuelva el siguiente problema computacional:

**Problema**: Calcular el valor de `f(n)`.
* **Entradas**: El número máximo de iteraciones de la serie a calcular ![n perteneciente a los naturales](https://latex.codecogs.com/png.latex?n%20%5Cin%20%5Cmathbb%7BN%7D).
* **Salidas**: El valor de ![equation](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%5Csum_%7Bj%3D1%7D%5E%7Bi%7D%20%5Csum_%7Bk%3Dj%7D%5E%7Bi&plus;j%7D1) para el ![n](https://latex.codecogs.com/png.latex?n) dado.

En el archivo `sumatoria.py`:

1. Implemente la función `sumatoria_cubica` con un algoritmo que resuelva el problema en complejidad temporal cúbica ![O(n^3)](https://latex.codecogs.com/png.latex?T%28n%29%20%3D%20%5Cmathcal%7BO%7D%28n%5E3%29).
2. Implemente la función `sumatoria_constante` con un algoritmo que resuelva el problema en complejidad temporal constante ![O(1)](https://latex.codecogs.com/png.latex?T%28n%29%20%3D%20%5Cmathcal%7BO%7D%281%29).

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

## Rúbrica (15 pts)

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con la especificación del problema.
* (3 pts) La producción cumple parcialmente con la especificación del problema.
* (1 pts) La producción, en su mayor parte, no cumple con la especificación del problema.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa exitosamente la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa exitosamente la mayoría de las pruebas automatizadas.

### Análisis y diseño (5 pts)

* (5 pts) El código cumple totalmente con los requerimientos de complejidad especificados.
* (3 pts) El código cumple con la mayoría de los requerimientos de complejidad especificados.
* (1 pts) El código no cumple con la mayoría de los requerimientos de complejidad especificados.
