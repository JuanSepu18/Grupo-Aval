// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.


//determinar si la ram 0 es menor a cero
@0
D=M;
@terminar
D; JLT

//determinar si la ram 1 es menor a cero
@1
D=M;
@terminar
D; JLT

@2
M=0;

//inicalizando el contador
@contador
M=D;

//donde se va a almacenar la multiplicacion
@multiplicacion
M=0;

(LOOP)

//si contador == 0 hace stop
@contador
D=M

@STOP
D; JEQ

//disminuir contador en uno
@contador
M=M-1;

//sumar
@multiplicacion
D=M;


@0
D=D+M

@multiplicacion
M=D;

@LOOP
0; JMP

(STOP)

//asigando la multiplicacion a la ram 2
@multiplicacion
D=M;

@2
M=D;

(terminar)

(FINAL)
@FINAL
0;JMP