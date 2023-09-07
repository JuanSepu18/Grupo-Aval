# Descricpión de la practica de laboratorio 1

En esta practica, se realizo el proyecto inicial correspondiente al proyecto 1 de la aplicación interactiva de nand2tetris,
donde el objetivo es construir las compuertas logicas principales (Not, And, Nand, Or, Xor, Mux y Dmux) junto con sus dierentes 
cantidades de entradas.

Una vez descargado el proyecto de nand2teris en el dispositivos, se procedio a emplear la interfaz de nand2tetris para porbar el codigo empleado, el cual, fue modificado por medio de bloc de notas y visual studio, donde se tiene que actializar y volver a cargar el archivo a nand2tetris. Este procedimiento se empleo para todas las compuertas creadas, y a medida que se iban creando, se habilitaban para ser usadas en las siguientes. Por ejemplo: para crear la compuerta de And, se empleo la compuerta Nand, la cual ya se encontraba implementada, y posteriormente se usó la compuerta Not, la cual se creo anteriormente a partir de la Nand.

A continuación se explica el desarollo de cada compuerta logica creada:

## Not:

Para esta compuerta, se empleó la compuerta Nand, donde se ingresó la misma entrada para las 2 requeridas de la Nand, y posteriormente por la misma logica de la Nand, muestra la entrada negada.

![compuerta_not_con_nand](https://github.com/JuanSepu18/Grupo-Aval/assets/129451318/e8708a50-8426-49af-aa3f-2b2cf4614172)


## And:

Para esta compuerta, se empleó la misma compuerta Nand y mediante la compuerta ya realizada anteriormente (Not) se niega la salida, de esta forma obtenemos la compuerta And.

## Or:

Para esta compuerta, mediante las propiedades de la logica se empleó la compuerta Nand entre el Not(a) y Not(b), y de esta forma, el producto de and pasa a ser el + de or.

## Xor:

Para el desarrollo de esta compuerta, primero se indagó cual es la logica de un Xor, donde al ser iguales las entradas, se produce un cero en la salida, y de forma contraria, cuando son diferentes se muestra un 1 como salida. Para su implementación se usó una compuerta Or entre dos And, como se muestra a continuación: Or[And (not(a),b   And(a,not(b))]

![04298](https://github.com/JuanSepu18/Grupo-Aval/assets/129451318/070718b4-44f7-423f-8d3a-3a460875f9df)


## Mux:

Para el desarrollo de esta compuerta, se tiene en cuenta la definicion de un multiplexor, y las variables y aspectos que influyen en él. Se compone de 2 entradas un selector y la salida, cuando el selector es 0, muestra a, y viceversa, cuando es 1, muestra b. Despues de aplicada la logica del mapa de Karnaugh, se llegó a la sieguiente expresión: Or[And(not(sel),a)   And(sel,b)].

![Lab_Digital I-9_html_10141238](https://github.com/JuanSepu18/Grupo-Aval/assets/129451318/a6a86fce-5ab9-4d3f-92d8-cb44fb9471cc)

## DMux:
