@256
    D=A
@SP
    M=D
@Sys.initRET0
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@LCL
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@ARG
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THIS
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THAT
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    D=M
@LCL
    M=D
@SP
    D=M
@5
    D=D-A
@ARG
    M=D
@Sys.init
    0;JMP
(Sys.initRET0)
(Main.fibonacci)
@ARG
    D=M
@0
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@2
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    M=M-1
    A=M
    D=M
@SP
    M=M-1
@SP
    A=M
    D=M-D
@BOOL0
    D;JLT
@SP
    A=M
    M=0
@ENDBOOL0
    0;JMP
(BOOL0)
@SP
    A=M
    M=-1
(ENDBOOL0)
@SP
    M=M+1
@SP
    M=M-1
    A=M
    D=M
@Main$IF_TRUE
    D;JNE
@Main$IF_FALSE
    0;JMP
(Main$IF_TRUE)
@ARG
    D=M
@0
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@LCL
    D=M
@R13
    M=D
@SP
    M=M-1
    A=M
    D=M
@ARG
    A=M
    M=D
@ARG
    D=M
@SP
    M=D+1
@R13
    D=M
@1
    D=D-A
    A=D
    D=M
@THAT
    M=D
@R13
    D=M
@2
    D=D-A
    A=D
    D=M
@THIS
    M=D
@R13
    D=M
@3
    D=D-A
    A=D
    D=M
@ARG
    M=D
@R13
    D=M
@4
    D=D-A
    A=D
    D=M
@LCL
    M=D
@R13
    D=M
@5
    D=D-A
    A=D
    D=M
@R14
    M=D
@R14
    A=M
    0;JMP
(Main$IF_FALSE)
@ARG
    D=M
@0
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@2
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    M=M-1
    A=M
    D=M
@SP
    M=M-1
@SP
    A=M
    M=M-D
@SP
    M=M+1
@Main.fibonacciRET1
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@LCL
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@ARG
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THIS
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THAT
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    D=M
@LCL
    M=D
@SP
    D=M
@6
    D=D-A
@ARG
    M=D
@Main.fibonacci
    0;JMP
(Main.fibonacciRET1)
@ARG
    D=M
@0
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@1
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    M=M-1
    A=M
    D=M
@SP
    M=M-1
@SP
    A=M
    M=M-D
@SP
    M=M+1
@Main.fibonacciRET2
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@LCL
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@ARG
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THIS
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THAT
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    D=M
@LCL
    M=D
@SP
    D=M
@6
    D=D-A
@ARG
    M=D
@Main.fibonacci
    0;JMP
(Main.fibonacciRET2)
@SP
    M=M-1
    A=M
    D=M
@SP
    M=M-1
@SP
    A=M
    M=M+D
@SP
    M=M+1
@LCL
    D=M
@R13
    M=D
@SP
    M=M-1
    A=M
    D=M
@ARG
    A=M
    M=D
@ARG
    D=M
@SP
    M=D+1
@R13
    D=M
@1
    D=D-A
    A=D
    D=M
@THAT
    M=D
@R13
    D=M
@2
    D=D-A
    A=D
    D=M
@THIS
    M=D
@R13
    D=M
@3
    D=D-A
    A=D
    D=M
@ARG
    M=D
@R13
    D=M
@4
    D=D-A
    A=D
    D=M
@LCL
    M=D
@R13
    D=M
@5
    D=D-A
    A=D
    D=M
@R14
    M=D
@R14
    A=M
    0;JMP
(Sys.init)
@4
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@Main.fibonacciRET3
    D=A
@SP
    A=M
    M=D
@SP
    M=M+1
@LCL
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@ARG
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THIS
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@THAT
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
@SP
    D=M
@LCL
    M=D
@SP
    D=M
@6
    D=D-A
@ARG
    M=D
@Main.fibonacci
    0;JMP
(Main.fibonacciRET3)
(Sys$WHILE)
@Sys$WHILE
    0;JMP
