# Descripción de la practica de laboratorio 3
La practica de laboratorio No. 3 corresponde al desarrollo e implementación de los proyectos 4 y 5 de nand2tetris, los cuales se encuentran en la carpeta de proyectos de la aplicación. Para el desarrollo de dichos proyectos se emplean el lenguaje de maquina de modo comprensible para su programación, asi como tambien, se emplea la paltaforma Hack y su lenguaje ensamblador.

***

## ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

El lenguaje de máquina o código máquina es el sistema de códigos directamente interpretable por un circuito microprogramable, como el microprocesador de una computadora o el microcontrolador de un autómata. Este lenguaje está compuesto por un conjunto de instrucciones que determinan acciones a ser tomadas por la máquina.
Es decir, esto es importante ya que es el nivel más bajo de programación que puede entender directamente una máquina. Este lenguaje al ser un conjunto de instrucciones binarias permite la comunicación directa de la CPU con otros componentes de hardware como lo puede ser la memoria ram.
La correcta comprensión de este lenguaje es esencial para poder diseñar de la manera mas eficiente la arquitectura del sistema informático, permitiendo optimizar el rendimiento y la ejecución de programas.

***

## ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?

El objetivo es desarrollar las actividades y programas propuestos en los dos proyectos a resolver, esto empleando el lenguaje ensamblador Hack para el desarrollo de el proyecto 4, y su posterior implementación para la construcción de los dispositivos del proyecto 5.

#### Proyecto 4: Construcción de los programas descritos
- En este proyecto se propone como objetivo la programación de bajo nivel de la maquina, teniendo un uso de la plataforma Hack proporcionada por nand2tetris. Tambien, se otorga una vista de la ejecución del codigo ninario nativo, y su comportamiento mediante la ejecución del lenguaje de maquina.
- Se desarrollan los programas de Mult (programa multiplicador de las entradas) y Fill (programa que rellena la pnatalla de negro al dar click an alguna area), mediante el lenguaje ensamblador Hack.

#### Proyecto 5: Construcción de los chips descritos
- En este proyecto se propone como objetivo la construcción de la plataforma Hack Hardware completa, ya que implementa los chips creados en proyectos anteriores (como por ejemplo AlU y RAM) para la implementación de chips mas complejos, es decir, juntaremos todos los chips y programas creados anteriormente para este proyecto.
- Se desarrollan los chips de Memoria, CPU y Computadora, esto con el objetivo de completar la construcción de la CPU Hack y la plataforma mencionada anteriormente, hasta llegar al chip Computer.

***

## Proyecto 4: Descripción de los programas
A continuación se da una breve explicación del proceso de construcción de los programas del proyecto 4 de nand2tetris, explicando su funcionamiento basico de forma breve.

### Mult: 
Su función principal es sumar dos números binarios de un solo bit y producir dos salidas: una para la suma de los bits y otra para el acarreo (carry) que se genera cuando la suma supera el valor de 1. 
Se construyó mediante un Xor entre las entradas y un And entre las mismas.

### Fill: 
circuito lógico digital más avanzado que el Half Adder y se utiliza para sumar tres números binarios de un solo bit: dos bits de entrada y un bit de acarreo (carry) de una operación anterior. Su función principal es producir dos salidas: una para la suma de los tres bits de entrada y otra para el acarreo resultante de la operación.
Se requieren 3 entradas, donde incialmente se emplea un HalfAdder para obtener sumAB, el cual se usa como entrada del siguiente HalfAdder junto con la entrada c. Por ultimo se realiza un Or entre los 2 carrys obtenidos anteriormente.

## Proyecto 5: Descripción de los chips
A continuación se da una breve explicación del proceso de construcción de los chips del proyecto 5 de nand2tetris, explicando los componentes utilizados y su funcionamiento.

### Memory:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

### CPU:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

### Computer:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

