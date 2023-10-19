# Descripción de la practica de laboratorio 4
La practica de laboratorio No. 4 corresponde al desarrollo e implementación del proyecto 6 de nand2tetris, el cual se encuentra en la carpeta de proyectos de la aplicación. Para el desarrollo de dicho proyecto se emplean el lenguaje de maquina de modo comprensible para su programación, asi como tambien, se emplea la paltaforma Hack y su lenguaje ensamblador.

***

## Pregunta: Teniendo en cuenta las caracteristicas del ensamblador, ¿Cuál es la principal limitante que observan? Justifique su respuesta.
El ensamblador es un lenguaje de programación de bajo nivel que se utiliza para programar directamente la arquitectura de una computadora. Una de las limitantes principales es que es altamente dependiente de la arquitectura del procesador. Esto significa que el código ensamblador escrito para un procesador específico no es portátil y no se puede ejecutar en otro procesador sin modificaciones significativas. Cada arquitectura de procesador tiene su propio conjunto de instrucciones y registros, lo que hace que el código ensamblador sea altamente específico para esa arquitectura. Esto dificulta la portabilidad y la reutilización del código entre diferentes tipos de procesadores.


***

## ¿Cuál es el objetivo del proyecto?

- En este proyecto se propone como objetivo la escritura de un programa de tipo ensamblador que proporcione la función de traducir programas escritos en el lenguaje usado anteriormente (lenguaje ensamblador simbólico Hack) al tipo binario, de modo que se pueda ejecutar en la plataforma Hack.

***

## Proyecto 6: El Ensamblador
A continuación se da una breve explicación del proceso de construcción del programa del proyecto 6 de nand2tetris, explicando su funcionamiento basico de forma breve.

El proceso general de conversión de un código de ensamblador a un código de máquina implica los siguientes pasos:

### 1. Configuración inicial: 
Se define un diccionario que mapea nombres simbólicos (como 'SCREEN', 'KBD', 'SP', 'LCL', etc.) a direcciones de memoria predefinidas. También se asignan direcciones a las localidades de memoria de tipo 'R' (R0, R1, ..., R15), ya que el diccionario también inicializa las localidades de memoria de tipo "R" (registros generales) con valores ascendentes del 0 al 15.

En este caso específico, el código proporcionado en Python incluye la creación de un diccionario que mapea ciertos nombres simbólicos a direcciones de memoria predefinidas. Este diccionario se utiliza más adelante en el proceso de conversión para asignar direcciones de memoria específicas a símbolos que se encuentran en el código de ensamblador.


### 2. Ensamblador:
Se trada del análisis del código de ensamblador, se realiza principalmente mediante el uso del módulo parseador. Aquí se describen los aspectos clave de este proceso en detalle:

**- Inicialización de la clase parseo**: Se inicializa un objeto de la clase parseo para cada línea del archivo de código de ensamblador. El constructor de la clase elimina los espacios en blanco y otros caracteres innecesarios, y establece el tipo de instrucción como nulo al principio.

**- Verificación del tipo de instrucción**: Mediante el método verificar, se identifica el tipo de instrucción en función de su estructura. Se verifica si la línea es un comentario, una instrucción A ( empezando con "@" ), una etiqueta ( empezando con "(" ), o una instrucción C. El resultado se almacena en el atributo tipo del objeto.

**- Limpieza de la línea**: El método limpiar elimina los comentarios y espacios en blanco de la línea para facilitar el análisis posterior. Esto implica encontrar la posición del comentario (si existe) y truncar la línea en consecuencia.

**- Métodos de obtención de componentes de instrucciones específicas**: Los métodos como get_valor, get_destino, get_operacion, get_salto y get_etiqueta se utilizan para extraer componentes específicos de la instrucción, como el valor, el destino, la operación, el salto y la etiqueta respectivamente. Estos métodos trabajan en función del tipo de instrucción y devuelven los valores correspondientes según la lógica definida.


### 3. Generación de código de máquina:
El módulo `codificador` traduce los componentes de la instrucción ensambladora a código binario., posteriormente se obtiene el código de destino, el código de operación y el código de salto correspondientes para las instrucciones de tipo C. Para las instrucciones de tipo A, se traduce el valor a su representación binaria de 15 bits.
A continuación se explican las funciones de los metodos mas detalladamente:

**`codigo_destino`**: Este método toma el destino de una instrucción de tipo C y devuelve su representación en código binario, según el diccionario de destinos predefinidos.

**`codigo_operacion`**: Este método toma la operación de una instrucción de tipo C y la convierte en su representación en código binario correspondiente, según el diccionario de operaciones predefinidas. Aquí se eliminan los espacios en blanco de la operación antes de buscarla en el diccionario.

**`codigo_salto`**: Similar a `codigo_destino` y `codigo_operacion`, este método toma el salto de una instrucción de tipo C y lo convierte en su representación en código binario correspondiente, según el diccionario de saltos predefinidos.

**`codigo_valor`**: Este método se utiliza para convertir un valor, ya sea un número o una variable, en su representación binaria de 15 bits. Si la variable no existe en el diccionario, se le asigna un valor y se agrega al diccionario.

**`agregar_al_diccionario`**: Este método se encarga de agregar las etiquetas y sus direcciones correspondientes al diccionario.

### 4. Actualización del diccionario:
El paso 4 implica la actualización del diccionario con la información de las etiquetas y sus respectivas direcciones. Aquí se describen los detalles de este proceso. 
El método `agregar_al_diccionario` itera a través de cada línea previamente procesada y analizada para determinar si se trata de una etiqueta. Si la línea no es una etiqueta, se incrementa un contador para rastrear las instrucciones no relacionadas con etiquetas. 

Si se encuentra una línea que es una etiqueta, se agrega al diccionario la información de la etiqueta y su dirección correspondiente, que se establece en función del contador de instrucciones.


### 5. Escritura del archivo de salida:
Se genera el nombre del archivo de salida en función del nombre del archivo de entrada proporcionado, reemplazazando la extensión ".asm" por ".hack".

Dependiendo del tipo de instrucción (A o C), se escribe la cadena de código de máquina correspondiente en el archivo de salida, junto con un carácter de nueva línea para cada línea de código de máquina.

***

Una vez obtenido el proyecto de ensamblador completo, se procede a realizar las pruebas con los programas asm respectivos, como el pong y los demas a usar mediante el programa de nand2tetris.

