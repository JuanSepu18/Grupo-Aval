# Descripción de la practica de laboratorio 3
La practica de laboratorio No. 3 corresponde al desarrollo e implementación de los proyectos 4 y 5 de nand2tetris, los cuales se encuentran en la carpeta de proyectos de la aplicación. Para el desarrollo de dichos proyectos se emplean el lenguaje de maquina de modo comprensible para su programación, asi como tambien, se emplea la paltaforma Hack y su lenguaje ensamblador.

***

## ¿Cuál es el objetivo de cada uno de esos proyectos con sus palabras y describa que debe hacer para desarrollarlo?

El objetivo es desarrollar las actividades y programas propuestos en los dos proyectos a resolver, esto empleando el lenguaje ensamblador Hack para el desarrollo de el proyecto 4, y su posterior implementación para la construcción de los dispositivos del proyecto 5.

#### Paso 1: Construcción de los chips descritos en el Capítulo 1
- Comenzar construyendo los chips básicos descritos en el Capítulo 1, como compuertas lógicas (NAND, NOT, AND, OR, XOR), multiplexores, demultiplexores y sumadores de bits de medio y completo.
- Utilizar estos chips como bloques de construcción para implementar chips más complejos.

#### Paso 2: Construcción de los chips descritos en el Capítulo 2
- Continuar con la construcción de chips más avanzados descritos en el Capítulo 2, como registros de 16 bits, registros de acceso, contadores, y la Unidad de Control.
- Utilizar los chips construidos en el Capítulo 1 junto con estos nuevos chips para crear componentes más complejos.

#### Paso 3: Construcción de la Unidad Lógica Aritmética (ALU)
- Utilizar los componentes previamente construidos para ensamblar una Unidad Lógica Aritmética (ALU) que sea capaz de realizar operaciones aritméticas y lógicas, como suma, resta, AND, OR, etc.
- Asegurarse de que la ALU tenga las entradas y salidas adecuadas para operar con registros y la futura memoria RAM.

#### Paso 4: Construcción de los chips descritos en el Capítulo 3
- Progresar hacia la construcción de los chips descritos en el Capítulo 3, que incluyen puertas DFF primitivas (flip-flops), registros, y multiplexores de 16 bits.
- Utilizar estos chips para crear una unidad de memoria de acceso aleatorio (RAM) de 16K.

#### Paso 5: Integración y Pruebas
- Ensamblar todos los componentes construidos en los pasos anteriores para crear una computadora Hack completa.
- Realizar pruebas exhaustivas para garantizar que la computadora funcione correctamente y pueda ejecutar programas en lenguaje de máquina de Hack

***

## Descripción de los chips
A continuación se da una breve explicación del proceso de construcción de los chips de los proyectos 2 y 3 de nand2tetris, explicanco los integrados utilizados del proyecto 1.

### HalfAdder: 
Su función principal es sumar dos números binarios de un solo bit y producir dos salidas: una para la suma de los bits y otra para el acarreo (carry) que se genera cuando la suma supera el valor de 1. 
Se construyó mediante un Xor entre las entradas y un And entre las mismas.

### FullAdder: 
circuito lógico digital más avanzado que el Half Adder y se utiliza para sumar tres números binarios de un solo bit: dos bits de entrada y un bit de acarreo (carry) de una operación anterior. Su función principal es producir dos salidas: una para la suma de los tres bits de entrada y otra para el acarreo resultante de la operación.
Se requieren 3 entradas, donde incialmente se emplea un HalfAdder para obtener sumAB, el cual se usa como entrada del siguiente HalfAdder junto con la entrada c. Por ultimo se realiza un Or entre los 2 carrys obtenidos anteriormente.

### Add16: 
Se utilizan múltiples chips Full Adder (como mencionamos anteriormente) conectados en cascada. Cada Full Adder suma un par de bits correspondientes de los dos números de 16 bits y toma en cuenta el acarreo de la suma anterior. El resultado es una suma de 16 bits que puede ser representada en binario.
Inicialmente se emplea un HalfAdder para poder obtene run carry inicial, posteriormente se realiza en cascada 15 Fulldders en los cuales se usa como carry el del anterior.

### Inc16:
incluye una serie de sumadores de un solo bit (Full Adders) conectados en cascada para sumar 1 al número binario de 16 bits de entrada. El primer sumador suma 1 al bit menos significativo (LSB), y si este produce un acarreo, pasa al siguiente sumador, y así sucesivamente, hasta llegar al bit más significativo (MSB).
Mediante un in[16] de entrada, se emplea un Add16, donde se declara todo los bits en 0 y se ejecuta la función principal de sumar 1.

### ALU:
Realiza operaciones aritméticas y lógicas en datos binarios. Su función principal es ejecutar operaciones como suma, resta, AND, OR, NOT, y muchas otras, dependiendo de las necesidades de la instrucción de la CPU.
Para la salide de ZX, se utilizó un Mux16 entre x y b como falso, y para la salida de NX se empleó un Not16 de la salida de ZX para luego ingresarlo en otro Mux16.
Este procedimiento se repitió para las salidas de ZY y NY respectivamente, para luego proceder con las operaciones aritmeticas: Para la suma se usó un Add16 entre la salida de NX y NY, luego para la operación And se usó un And16 entre las salidas de NX y NY.
Luego se seleccionó la funcion (f) medianre un Mux16 entre andXY y suma XY.

### Bit:
Para la construcción de Bit se selecciona entre la salida anterior y la entrada actual mediante un Mux, para posteriormente guardar la selección y generar la salida mediante el DDF (Data Flip Flop).

### Register:
Mediante este se almacenan 16 Bits en la memoria, es por esto que para su construcción en el codigo, se emplearon 16 Bits contrsuidos anteriormente, y de esta forma generar un registro de 1 Bit para cada uno de los 16.

### RAM8: 
Se trata de una memoria de 8x16, es decir, 8 registros de 16 bits cada uno. Teniendo esto en cuenta, se deduce que su construcción se basa en usar 8 Register los cuales son cada uno de 16 bits. 
Inicialmente se pasa el numero a binario del adderss a decimal  mediante un DMux(Way, luego se manda el load de cada registro, creando los 8 Register. Por ultimo seleccionamos un registro para el Mux8Way16.

### RAM64:
Se trata de una memoria de 64 registros, cada uno de 16 bits de ancho, es por esto que para su construcción empleamos 8 RAM8, y de esta forma obtenemos 64 registros.
Inicialmente seleccionamos hacia que ram de 8 mandamos el load mediante un DMux8Way, luego hacemos la asignación del input en la ram de 8, mediante la implementación de 8 RAM8. Finalmente seleccionamos uno de los registros devueltos por la RAM8 mediante un Mux8Way16.

### RAM512: 
El procedidmiento es similar a la construcción de las anteriores RAM, en este caso se trata de una memoria de 512 registros, cada uno de 16 bits de ancho, es por esto que se emplean en su construcción 8 veces RAM64, para un total de 512.

### RAM4k:
El proceidmiento es similar a la construcción de las anteriores RAM, en este caso se trata de una memoria de 4000 registros, cada uno de 16 bits de ancho, es por esto que se emplean en su construcción 8 veces RAM512, para un total de 4000.

### RAM16k:
Se trata de una memoria de 16k registros, cada uno de 16 bits de ancho, es por esto que para su construcción empleamos 4 RAM4k, y de esta forma obtenemos 16k registros.
Inicialmente seleccionamos hacia que ram de 4k mandamos el load mediante un DMux4Way, luego hacemos la asignación del input en la ram de 4k, mediante la implementación de 4 RAM4k. Finalmente seleccionamos uno de los registros devueltos por la RAM4k mediante un Mux4Way16.

### PC:
Primero se crea el incremento de out mediante un Inc16, posteriormente seleccionamos las 3 entradas de los posibles valores mediante un Mux8Way16 para finalmente guardar la selección y generar la salida mediante un Register.
