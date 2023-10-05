# Descripción de la practica de laboratorio 3
La practica de laboratorio No. 3 corresponde al desarrollo e implementación de los proyectos 4 y 5 de nand2tetris, los cuales se encuentran en la carpeta de proyectos de la aplicación. Para el desarrollo de dichos proyectos se emplean el lenguaje de maquina de modo comprensible para su programación, asi como tambien, se emplea la paltaforma Hack y su lenguaje ensamblador.

***

## ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

***

## ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?

El objetivo es desarrollar las actividades y programas propuestos en los dos proyectos a resolver, esto empleando el lenguaje ensamblador Hack para el desarrollo de el proyecto 4, y su posterior implementación para la construcción de los dispositivos del proyecto 5.

#### Proyecto 4: Construcción de los programas descritos
- Comenzar construyendo los chips básicos descritos en el Capítulo 1, como compuertas lógicas (NAND, NOT, AND, OR, XOR), multiplexores, demultiplexores y sumadores de bits de medio y completo.
- Utilizar estos chips como bloques de construcción para implementar chips más complejos.

#### Proyecto 5: Construcción de los chips descritos
- Continuar con la construcción de chips más avanzados descritos en el Capítulo 2, como registros de 16 bits, registros de acceso, contadores, y la Unidad de Control.
- Utilizar los chips construidos en el Capítulo 1 junto con estos nuevos chips para crear componentes más complejos.

***

## Proyecto 4: Descripción de los programas
A continuación se da una breve explicación del proceso de construcción de los chips de los proyectos 2 y 3 de nand2tetris, explicanco los integrados utilizados del proyecto 1.

### Mult: 
Su función principal es sumar dos números binarios de un solo bit y producir dos salidas: una para la suma de los bits y otra para el acarreo (carry) que se genera cuando la suma supera el valor de 1. 
Se construyó mediante un Xor entre las entradas y un And entre las mismas.

### Fill: 
circuito lógico digital más avanzado que el Half Adder y se utiliza para sumar tres números binarios de un solo bit: dos bits de entrada y un bit de acarreo (carry) de una operación anterior. Su función principal es producir dos salidas: una para la suma de los tres bits de entrada y otra para el acarreo resultante de la operación.
Se requieren 3 entradas, donde incialmente se emplea un HalfAdder para obtener sumAB, el cual se usa como entrada del siguiente HalfAdder junto con la entrada c. Por ultimo se realiza un Or entre los 2 carrys obtenidos anteriormente.

## Proyecto 5: Descripción de los chips
A continuación se da una breve explicación del proceso de construcción de los chips de los proyectos 2 y 3 de nand2tetris, explicanco los integrados utilizados del proyecto 1.

### Memory:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

### CPU:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

### Computer:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

