# Descripción de la práctica de laboratorio 6
La práctica de laboratorio No. 6 corresponde al desarrollo e implementación del proyecto 9 de Nand2Tetris, el cual se encuentra en la carpeta de proyectos de la aplicación. Para el desarrollo de dicho proyecto se implementa Jack, un lenguaje de programación simple similar a Java y basado en objetos, implementando posteriormente las aplicaciones interactivas sugeridas en la descrpición del proyecto.

***

## Lenguaje de alto nivel

Un lenguaje de alto nivel es un lenguaje de programación diseñado para ser comprensible por los humanos y expresar lógica de programación de una manera más natural y cercana al lenguaje humano. A medida que avanzamos en la escala de "alto nivel" a "bajo nivel", la abstracción se reduce y la programación se vuelve más directamente relacionada con la arquitectura y el hardware subyacente de la computadora.

<img width="507" alt="Captura de pantalla 2023-11-16 091840" src="https://github.com/JuanSepu18/Grupo-Aval/assets/129451318/9dddbbf1-ef60-4e68-bae6-2392080155e2">

### Características de los Lenguajes de Alto Nivel:

- Abstracción: Los lenguajes de alto nivel permiten a los programadores escribir instrucciones sin preocuparse demasiado por la complejidad de la máquina subyacente.

- Portabilidad: Los programas escritos en un lenguaje de alto nivel son más portátiles, ya que pueden ejecutarse en diferentes plataformas con pocos o ningún cambio.

- Sintaxis más Clara: Los lenguajes de alto nivel tienden a tener una sintaxis más clara y estructurada, lo que facilita la lectura y escritura del código.

- Gestión Automática de Memoria: Muchos lenguajes de alto nivel manejan automáticamente la asignación y liberación de memoria, aliviando a los programadores de esta tarea


## Bonus: ¿Qué se debe considerar para proponer un nuevo y buen lenguaje de programación, teniendo en cuenta la arquitectura de computador completa? Justifique su respuesta.

Para proponer un nuevo lenguaje de programación se deben considerar varios aspectos, especialmente en relación con la arquitectura de la computadora completa:

- Eficiencia: El nuevo lenguaje debe ser eficiente en términos de ejecución de código. La optimización del rendimiento es esencial para que el lenguaje sea práctico y utilizable en aplicaciones del mundo real.

- Abstracción: Debe proporcionar un buen equilibrio entre abstracción y control. Una abstracción demasiado baja puede hacer que sea difícil para los programadores expresar sus ideas de manera clara, mientras que una abstracción demasiado alta puede afectar el rendimiento.

- Portabilidad: La portabilidad es clave. El lenguaje debe ser diseñado de manera que los programas escritos en él puedan ejecutarse eficientemente en diferentes arquitecturas de computadoras.

- Seguridad: Se debe prestar especial atención a la seguridad para evitar vulnerabilidades y ataques. La gestión segura de la memoria y la prevención de errores comunes deben ser consideraciones fundamentales.

- Herramientas y Ecosistema: Un buen lenguaje debe contar con un sólido conjunto de herramientas de desarrollo y un ecosistema activo de bibliotecas y frameworks para facilitar la implementación de aplicaciones.

- Comunidad: La comunidad que se forme alrededor del lenguaje es esencial. Una comunidad activa y comprometida puede contribuir al crecimiento y mejora continua del lenguaje.


***

## ¿Cuál es el objetivo del proyecto?

En este proyecto de buscó adoptar o inventar una idea de aplicación, en forma de un simple juego de computadora. Los ejemplos realizados fueron Snake y Square, implementando  estas aplicación en Jack, los cuales consisten en una versión básica o parte de un juego simple o una interacción interesante. Para este desarrollo se implementa un editor de texto para la escritura de los programas Jack, el JackCompiler para su compilación y el emulador VM ya utilizado.


***

## Proyecto 9
A continuación se da una breve explicación del proceso de construcción del programa del proyecto 9 de nand2tetris, explicando su funcionamiento basico de forma breve.

### Snake

1. **Main.jack:**
   - Este archivo define la clase principal (`Main`) que contiene el método `main()`, donde se crea una instancia de la   clase `SnakeGame` llamada `game` para posteriormente llamar al método `run()` de la instancia `game` para ejecutar el juego.
   - Después de ejecutar el juego, se llama al método `dispose()` para realizar alguna limpieza o liberación de recursos, devolviendo el control.

2. **RandSeed.jack:**
   - Define la clase `RandSeed` que tiene un método `getSeed()` para obtener una semilla aleatoria.
   - Muestra un mensaje para indicar al usuario que presione una tecla para comenzar, y posteriormente utiliza un bucle para esperar a que el usuario realice dicha acción
   - Incrementa la semilla cada vez que el bucle se ejecuta y reinicia la semilla cuando alcanza un valor límite, para luego limpiar la pantalla y devolver la semilla.

3. **Random.jack:**
   - Define la clase `Random` que tiene un campo estático `seed` y métodos para manipular y generar números aleatorios, en donde se e ncuentra el método `setSeed()`, el cual establece la semilla para la generación de números aleatorios.
   - El método `rand()` genera un número aleatorio en el rango de 0 a 32767 usando una fórmula específica, y el método `randRange()` genera un número aleatorio en un rango específico utilizando la semilla y operaciones de bits.

4. **Snake.jack:**
- Este archivo define la clase `Snake`, representando la serpiente en el juego. Sus atributos incluyen la referencia al juego (`SnakeGame`), la posición de la cabeza, longitud, dirección, y un historial de movimientos. El constructor inicializa la serpiente y dibuja su posición inicial.
- Sus métodos incluyen funciones para gestionar el movimiento, crecimiento, dibujo y verificación de colisiones.

5. **SnakeGame.jack:**
- La clase `SnakeGame` representa el juego, contiene instancias de `Snake` y `SnakeGrid`. `run()` y maneja el bucle principal del juego, procesando la entrada del teclado, moviendo la serpiente y actualizando el estado del juego.
- También gestiona niveles, dibuja y actualiza la interfaz de usuario, y maneja eventos de pausa o finalización del juego.

7. **SnakeGrid.jack:**
Clase `SnakeGrid` que representa la cuadrícula del juego.
- Se utiliza para gestionar la posición de la serpiente y la ubicación de la comida. Sus métodos incluyen funciones para colocar y dibujar la comida, inicializar y gestionar la cuadrícula, y verificar ocupación y colisiones.
- Proporciona métodos para dibujar la interfaz de usuario, como puntuación, nivel y mensajes de estado.


### Square


***

