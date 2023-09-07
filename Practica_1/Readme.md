#Descricpión de la practica de laboratorio 1

En esta practica, se realizo el proyecto inicial correspondiente al proyecto 1 de la aplicación interactiva de nand2tetris,
donde el objetivo es construir las compuertas logicas principales (Not, And, Nand, Or, Xor, Mux y Dmux) junto con sus dierentes 
cantidades de entradas.

A continuación se explica el desarollo de cada compuerta logica creada:

##Not:

Se hizo a base de nand, con la misma entrada

##And:

Se usa la nand normal, y se niega el resultado

##Or:

Se uso la nand de un not(a) y not(b)

##Xor:

Cero cuando son iguales, 1 diferentes; a’b+ab’ es decir, un or[And (not(a),b   And(a,not(b)))

##Mux:

La salida es a, cuando el selector es cero,    es b cuando el selector es 1  
Or[  And(not(select),a)  ]

