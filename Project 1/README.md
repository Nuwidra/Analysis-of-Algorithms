# Primer proyecto programado #

IC-3002 Análisis de algoritmos  
Proyecto 1  

Como primer proyecto del curso, desarrollaremos y documentaremos una investigación empírica sobre los algoritmos de ordenamiento estudiados hasta este punto del curso.

## Objetivos formativos ##

* Validar los resultados teóricos de los análisis de complejidad temporal de los distintos algoritmos de ordenamiento estudiados en el curso, a través de la producción de evidencia empírica sobre la ejecución de los algoritmos en una máquina concreta (V).

* Comparar el desempeño de distintos algoritmos de ordenamiento en distintas circunstancias para validar resultados teóricos sobre las situaciones en las cuales se recomienda la utilización de los distintos algoritmos.

## Objetivos del curso ##

* Identificar la medición de la eficiencia de los algoritmos y  la programación de algoritmos utilizando buenas prácticas y estructuración del código en capas.

## Contenidos del curso ##

* Eficiencia, medición y análisis y orden de los Algoritmos
* Complejidad computacional con problemas de búsqueda y ordenamiento
* Divide y conquista

## Especificación ##

Esta investigación estará centrada en las siguientes preguntas.

1. Para cada algoritmo de ordenamiento estudiado hasta el momento en el curso —a saber: ordenamiento por selección, ordenamiento por inserción, ordenamiento burbuja, *quicksort*, y *mergesort*—, si ejecutamos el algoritmo en una máquina concreta, ¿coincide su comportamiento temporal con los resultados predichos teóricamente (incluyendo los distintos casos)?

2. Considerando los algoritmos de ordenamiento por intercambio de adyacentes (selección, inserción, burbuja original, burbuja optimizado), se sabe que presentan complejidad temporal cuadrática en sus casos promedio y peor. A pesar de que su consumo de recurso temporal cae en la misma clase de complejidad, ¿cómo se comparan en cuanto a rendimiento temporal? ¿Hay alguno más eficiente? Si es el caso, ¿cómo se justifica esta diferencia en eficiencia?

3. ¿Cómo se compara el algoritmo *quicksort* con el algoritmo *mergesort* en términos de rendimiento temporal?

4. ¿Cómo se compara el algoritmo divide y conquista más eficiente temporalmente con el algoritmo de ordenamiento por intercambio de adyacentes más eficiente temporalmente? ¿En qué casos es posible recomendar el uso de una categoría de algoritmos de ordenamiento sobre la otra?

### Metodología de la investigación ###

* Desarrollar un plan de investigación que indique cuál será el acercamiento para tratar de resolver cada pregunta. Indicando específicamente para cada pregunta:

  * Cuál es la propuesta de análisis para acercarse a la pregunta.

  * El diseño del experimento computacional que se desarrollará y aplicará para recopilar datos empíricos que nos permitan realizar los análisis propuestos en el punto anterior.

* Aplicar los experimentos y recolectar los datos. Los experimentos deben ser reproducibles.

* Analizar los datos, y sintetizar conclusiones que intenten responder a las preguntas de investigación.

### Documentación de la investigación ###

Para cada pregunta de investigación, se documentará el proceso investigativo en un cuaderno Jupyter (usar `cuaderno-ejemplo` como referencia). Este cuaderno se estructurará con las siguientes secciones:

* Problema: especificación de la pregunta de investigación y planteo de hipótesis.

* Metodología: propuesta de cómo se intentará resolver la pregunta, así como el diseño de los experimentos que se aplicarán. El diseño de experimentos debe contemplar cuántas veces se ejecutará el algoritmo, con qué argumentos, y cómo se recolectarán los tiempos de ejecución.

* Análisis de Resultados: implementación de los algoritmos, implementación del código para extraer datos sobre la ejecución de los algoritmos, graficación y tabulación de los resultados.

* Conclusiones: conclusiones derivadas del análisis, intento de resolución de la pregunta de investigación.

## Metodología del proyecto ##

* El proyecto se trabajará en equipos de cinco personas durante un período de tres semanas.

* Se realizarán dos reuniones de seguimiento del proyecto con el docente, una después de la primera semana, y la otra después de la segunda semana.

* Al finalizar la tercer semana, se realizará una reunión final de presentación y defensa del proyecto con el docente.

* Para la primera reunión de seguimiento se evaluará el avance en el plan de desarrollo.

* Para la segunda reunión de seguimiento se evaluará el avance en la aplicación de experimentos y recolección de datos.

* En la reunión final de defensa se evaluará el producto completo de la investigación.

## Configurar el ambiente de desarrollo ##

Crear un ambiente:

```bash
python3 -m venv .venv
```

Activar el ambiente:

```bash
source ./.venv/bin/activate
```

Instalar las dependencias:

```bash
pip3 install -r requirements.txt
```

Ejecutar el servidor de cuadernos:

```bash
jupyter notebook
```

Se debe abrir la aplicación en el navegador, y desde ahí se pueden crear, modificar y desplegar cuadernos.

## Rúbrica ##

### Plan de investigación ###

* (5) El plan de investigación se presenta completo, incluye propuestas de análisis y diseño de experimentos para cada pregunta. Requiere solamente algunos ajustes menores.
* (3) El plan de investigación se presenta parcialmente, incluye propuestas de análisis y diseño de experimentos para la mayoría de las preguntas. O se presenta completo pero requiere de ajustes mayores.
* (1) El plan de investigación se presenta muy incompleto.

### Experimentos ###

* (5) El código de implementación de los experimentos coincide con lo estipulado en el diseño, se ejecuta correctamente y produce resultados utilizables.
* (3) El código de implementación de los experimentos coincide con lo estipulado en el diseño, sin embargo no se ejecuta correctamente en algunos casos o los resultados producidos son en algunos casos inutilizables.
* (1) El código de implementación de los experimentos no coincide con lo estipulado en el diseño, o la mayoría de experimentos no se ejecuta correctamente o sus resultados son inutilizables.

### Análisis de resultados ###

* (5) Los resultados se presentan clara y correctamente en gráficos y tablas, indicando apropiadamente unidades y magnitudes. Los postulados de análisis tienen clara relación con los datos presentados.
* (3) La mayoría de los resultados se presentan clara y correctamente en gráficos y tablas, la presentación de algunos de los resultados requiere de correcciones menores. La mayoría de los postulados de análisis tienen clara relación con los datos presentados.
* (1) La mayoría de los resultados presentados requieren de correcciones significativas, carecen de claridad y correctitud. La mayoría de los postulados de análisis no tienen relación clara con los datos presentados.

### Conclusiones ###

* (5) Las conclusiones se derivan lógicamente del análisis de resultados. Los resultados se contrastan correctamente con lo esperado según la teoría.
* (3) La mayoría de las conclusiones se derivan lógicamente del análisis de resultados. La mayoría de los resultados se contrastan correctamente con lo esperado según la teoría.
* (1) La mayoría de las conclusiones no se derivan lógicamente del análisis de resultados. O, la mayoría de los resultados no se contrastan correctamente con lo esperado según la teoría.

### Documentación ###

* (5) La documentación presenta todas las secciones solicitadas. Hay atención al detalle en el uso correcto de ortografía, gramática, tipografía matemática y organización de los contenidos.
* (3) La documentación presenta todas las secciones solicitadas. Sin embargo, se identifican correcciones mayores forma en relación con la atención al detalle en el uso correcto de ortografía, gramática, tipografía matemática, u organización de los contenidos.
* (1) La documentación no presenta todas las secciones solicitadas. O las correcciones de forma requeridas son tan importante que se considera alguna sección como ilegible, y por consiguiente no presentada.
