# Descripción de la practica de laboratorio 5
La practica de laboratorio No. 5 corresponde al desarrollo e implementación de los proyectos 7 y 8 de nand2tetris, los cuales se encuentra en la carpeta de proyectos de la aplicación. Para el desarrollo de dichos proyectos se emplea el idioma de programación que se utiliza para implementar el traductor VM, junto con el emulador de CPU suministrado en las herramientas de los proyectos.

***

## Pregunta: Teniendo en cuenta el marco de estas dos prácticas que son las máquinas virtuales. ¿Cuál cree que es el futuro de las máquinas virtuales?

El futuro de las vm es prometedor y se proyecta que desempeñaran un papel importante en el desarrollo y la computación. Estas son algunas áreas clave que pueden definir el futuro de las máquinas virtuales:

-	Computación en la nube: Las máquinas virtuales son fundamentales en la infraestructura de la nube. Proveedores como Amazon y Google Cloud utilizan máquinas virtuales para ofrecer servicios escalables, flexibles y confiables a los usuarios.
  
- Virtualización de aplicaciones y contenedores: La virtualización no solo se limita a máquinas completas; también incluye la virtualización de aplicaciones y el uso de contenedores. Tecnologías como Docker han aumentado la popularidad de la virtualización a nivel de aplicación, permitiendo entornos más ligeros y ágiles.
  
- Seguridad y aislamiento: Las máquinas virtuales han sido utilizadas para proporcionar aislamiento entre sistemas y mejorar la seguridad.
  
- Eficiencia y rendimiento: El desarrollo continuo de técnicas de virtualización y la optimización de rendimiento seguirá siendo un área de enfoque. Mejorar la eficiencia y reducir la sobrecarga de recursos será crucial para garantizar la adopción y el éxito continuo de las máquinas virtuales.


***

## ¿Cuál es el objetivo de los proyectos?

- El objetivo del proyecto 7 es desarrollar un traductor VM básico que se centre en implementar los comandos de aritmética de pila y acceso a la memoria del lenguaje VM. Este traductor básico servirá como punto de partida para la construcción de un traductor VM a gran escala en el Proyecto 8. El enfoque se centra en la implementación de funcionalidades esenciales que sentarán las bases para una versión más completa y robusta en etapas posteriores del proyecto.
- Despues se ataca el proyecto 8, donde el objetivo es expandir el traductor VM básico desarrollado en el Proyecto 7 en un traductor VM a gran escala. En el Proyecto 7, nos enfocamos en manejar los comandos de aritmética de pila y acceso a memoria del lenguaje VM. Ahora, nos dirigimos a abordar los comandos de ramificación y llamadas a funciones del lenguaje VM, lo que implicará una implementación más completa y sofisticada para permitir un manejo eficiente de estas funcionalidades más avanzadas.

***

## Proyecto 7 y 8: Máquina Virtual
A continuación se da una breve explicación del proceso de construcción del programa del proyecto 7 y 8 de nand2tetris, explicando su funcionamiento basico de forma breve.


### 1. Traductor VM: 
El archivo `traductorVM.py` es esencial en el proceso de traducción del código de máquina virtual a código ensamblador Hack. Aquí está una descripción detallada de cada sección:

1. **`import` y `def main()`:**
El código comienza importando los módulos necesarios y definiendo la función principal `main()`, que se encarga de la ejecución principal del programa.

2. **Lectura de Archivo y Procesamiento de Líneas:**
El programa comienza abriendo y leyendo el archivo de código de máquina virtual. Luego, cada línea se procesa utilizando la clase `linea` del módulo `lineas.py`. Se eliminan los comentarios y espacios en blanco, y las líneas se clasifican en tres tipos según su longitud y contenido.

3. **Generación de Archivo de Ensamblador:**
Después de procesar todas las líneas del archivo de entrada, el programa genera un nuevo archivo con extensión `.asm`, que contendrá el código ensamblador Hack equivalente. Utiliza las funciones del módulo `line2asm.py` para traducir cada instrucción de máquina virtual a código ensamblador.

4. **Ejecución de la Traducción y Finalización del Archivo:**
El programa recorre cada línea procesada y utiliza las funciones adecuadas para traducir las instrucciones de máquina virtual a código ensamblador Hack. Finalmente, escribe las líneas traducidas en el archivo `.asm`. Además, al final del archivo, se escribe una instrucción `end` para marcar el final del programa.

5. **`if __name__ == '__main__':` y Llamada a la Función Principal:**
La sección final del código verifica si el script se está ejecutando como el programa principal y, si es así, llama a la función `main()` para comenzar el proceso de traducción.

`traductorVM.py`, funciona como el controlador principal que coordina la traducción del código de máquina virtual a código ensamblador Hack, utilizando funciones y clases definidas en otros archivos para procesar y traducir las líneas de código de manera efectiva.


### 2. Objeto para lineas

El archivo `lineas.py`, es un archivo que implementa una clase llamada `linea` que se utiliza para procesar las líneas de código leídas desde un archivo. La clase `linea` realiza varias operaciones esenciales:

1. **Inicialización:** En el método `__init__`, se procesa la línea, se elimina el contenido de los comentarios y se clasifica en función de su longitud.
2. **Verificación de comentarios:** El método `verificar` se utiliza para descartar las líneas que contienen únicamente comentarios o están en blanco.
3. **Eliminación de espacios en blanco:** El método `limpiar` se encarga de eliminar los espacios en blanco innecesarios alrededor de la línea.
4. **Selección del tipo de línea:** El método `sel_tipo` determina el tipo de la línea en función de su longitud y contenido.

El archivo `lineas.py` proporciona una forma eficiente de procesar y clasificar las líneas de código leídas desde un archivo de código de máquina virtual, lo que facilita la traducción posterior a instrucciones en lenguaje ensamblador Hack.


### 3. Traductor de lineas a ASM

El archivo `line2asm.py`, contiene funciones que se utilizan para convertir las instrucciones del lenguaje de máquina virtual a instrucciones en lenguaje ensamblador Hack. El archivo se compone de las siguientes funciones clave:

1. **Obtención de Diccionarios:** El archivo define funciones que obtienen diccionarios específicos para mapear las instrucciones del lenguaje de máquina virtual a instrucciones en lenguaje ensamblador Hack.

2. **Tipos de Instrucciones:** El archivo define tres tipos de funciones de traducción que corresponden a instrucciones de una, dos o tres palabras, respectivamente. Estas funciones seleccionan la operación adecuada a realizar en el código ensamblador Hack según el tipo de instrucción de la línea de código de máquina virtual.

`line2asm.py` desempeña un papel esencial en la traducción del código de máquina virtual al código ensamblador Hack, utilizando diccionarios y funciones especializadas para garantizar una traducción precisa y eficiente de las instrucciones de máquina virtual.

***
