PRACTICA 1 JORGE PIRIS RUIZ
========================================================================================
Descripcion de la práctica:

La aplicación desarrollada aplica los 3 algoritmos exigidos en la práctica. Todos
estos algoritmos tienen las implementaciones pedidas:
    - Algoritmo slope intercept completo
    - Algoritmo digital_differential_analyzer
    - Algoritmo bresenham primer octante

Además se adjunta cada uno de los códigos de los algoritmos de manera independiente
(que aplican un caso de ejemplo para unos puntos dados).
Para ejecutar los ficheros de los algoritmos abrir en cada carpeta un terminal y 
hacer uso del comando:
    - python "nombre del algoritmo".py
Para ejecutar la aplicación de la práctica:
    - Necesario instalar librería pygame: pip install pygame
    - Ejecutar: python practica1.py

Descripcion de la aplicación

Se trata de una pestaña reescalable, esto quiere decir que tanto los botones como
las rectas generadas se reescalan con el tamaño de la ventana. 
Existen botones para seleccionar entre los distintos algoritmos y colores, el modo
de visualizar las rectas, etc. El color, algoritmo y modo de visualización seleccionado
se marcan en verde.
Por último se define un boton para limpiar las rectas de la pizarra.

Para pintar una recta basta con clickar en dos puntos de la parte izquierda de la
ventana, una vez seleccionados los puntos se dibujará una recta con el algoritmo y
color seleccionado. La recta dibujada se mostrará con el modo de visualización seleccionado.

Las rectas son aculumables, es decir, una vez dibujada una recta pueden dibujarse más encima
de esta. El modo de visualización, el color, y el algoritmo aplicado puede cambiarse continuamente
sin problema. 

En el caso de seleccionar un punto y cambiar de algoritmo durante la selección, se realizará la recta
con el nuevo algoritmo seleccionado.
Por último, el tamaño de los cuadrados pizarra puede cambiarse modificando el valor de la variable
 BOARD_CELL_SIZE (se recomienda un valor entre 20 y 40 pixeles).
=====================================================================================================
ANOTACIONES

IMPORTANTE: Los pixeles en esta librería sitúan la esquina superior izquierda como (0,0) y la esquina 
inferior derecha como (height,width), por lo que el algoritmo bresenham solo funciona para los casos 
en los que la recta es en dirección inferior izquierda.
El entorno de desarrollo utilizado es vsCode, haciendo uso del paquete python para facilitar el desarrollo
de código.