# Descripción de la practica de laboratorio 3
La practica de laboratorio No. 3 corresponde al desarrollo e implementación de los proyectos 4 y 5 de nand2tetris, los cuales se encuentran en la carpeta de proyectos de la aplicación. Para el desarrollo de dichos proyectos se emplean el lenguaje de maquina de modo comprensible para su programación, asi como tambien, se emplea la paltaforma Hack y su lenguaje ensamblador.

***

## Pregunta bonus: ¿Por qué el lenguaje de máquina es importante para definir la arquitectura computacional?

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

- ### Mult: 
Las 16 palabras RAM principales (RAM[0]...RAM[15]) se emplean en su desarrollo. Este programa calcula el valor R0*R1 y almacena el resultado en R2. Este cálculo se realiza mediante una secuencia de instrucciones que toma los valores contenidos en R0 y R1, los multiplica y luego guarda el resultado en la ubicación de memoria R2. Esta operación es fundamental en el funcionamiento de la computadora Hack y se utiliza comúnmente para realizar diversas tareas, como cálculos matemáticos y manipulación de datos.
Inicialmente se determina si las posiciones 0 y 1 de la Ram son menores que cero, ya que en dicho caso, se termina el programa y el resultado será cero. Luego se hace uso de un contador para determinar la cantidad de veces que se va a sumar el numero de la ram 0, determinado por la ram 1.
Posteriormente ejecuta las sumas respectivas disminuyendo el contador a medida que se multiplian los numeros, para posteriormente almacenar el resultado en la posición de la ram 2.

- ### Fill: 
Este programa ilustra de manera efectiva cómo se pueden manipular los dispositivos de pantalla y teclado a nivel básico en el contexto de la programación. Mediante un bucle infinito monitorea la entrada del teclado. Cuando se detecta la pulsación de una tecla, el programa procede a oscurecer la pantalla, es decir, pone en negro cada píxel, esto es así mientras se siga presionando.
Inicialmente se almacena la posición en la que screen se encuentra iterando y esta al tanto de presionar una tecla, donde si hay algo en el KBD almacena el color negro, y si no hay nada (cero) almacena el color blanco. Luego salta a mostrar en la pantalla tomando la posicion almacenada y mostrando el color, moviendo la posición +1 para rellenar la pantalla.

## Proyecto 5: Descripción de los chips
A continuación se da una breve explicación del proceso de construcción de los chips del proyecto 5 de nand2tetris, explicando los componentes utilizados y su funcionamiento.

- ### Memory:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

- ### CPU:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

- ### Computer:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.

