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

1. **Configuración inicial**: Se define un diccionario que mapea nombres simbólicos (como 'SCREEN', 'KBD', 'SP', 'LCL', etc.) a direcciones de memoria predefinidas. También se asignan direcciones a las localidades de memoria de tipo 'R' (R0, R1, ..., R15).

2. **Análisis de código de ensamblador**:
   - El módulo `parseador` procesa el archivo línea por línea, identificando el tipo de instrucción (A, C o L) y extrayendo información relevante como el valor, el destino, la operación, el salto y las etiquetas.
   - Se eliminan los comentarios y los espacios en blanco, y se limpia la línea para un procesamiento más preciso.

3. **Generación de código de máquina**:
   - El módulo `codificador` traduce los componentes de la instrucción ensambladora a código binario.
   - Se obtiene el código de destino, el código de operación y el código de salto correspondientes para las instrucciones de tipo C.
   - Para las instrucciones de tipo A, se traduce el valor a su representación binaria de 15 bits.

4. **Actualización del diccionario**:
   - Las etiquetas de salto y sus respectivas direcciones se agregan al diccionario para su posterior referencia.

5. **Escritura del archivo de salida**:
   - Se escribe el código de máquina resultante en un archivo con extensión ".hack".

En resumen, el proceso implica inicializar las configuraciones, analizar el código de ensamblador para comprender sus componentes, traducir estos componentes a código de máquina y finalmente escribir el código de máquina resultante en un archivo de salida.

- ### Agregar: 


- ### Asm:


- ### Rect:


- ### Pong: 




