(Sys.init)

@4
    D=A
@SP
    A=M
    M=D
    @SP
    M=M+1
    
@call_Main.fibonacci_0
    D=A
@SP
    AM=M+1
    A=A-1
    M=D
@LCL
    D=M
@SP
    AM=M+1
    A=A-1
    M=D
@ARG
    D=M
@SP
    AM=M+1
    A=A-1
    M=D
@THIS
    D=M
@SP
    AM=M+1
    A=A-1
    M=D
@SP
    D=M
@5
    D=D-A
@1
    D=D-A
@ARG
    M=D
@SP
    D=M
@LCL
    M=D
@Main.fibonacci
    0;JMP
(call_Main.fibonacci_0)

(WHILE)
    
@WHILE
    0;JMP
    
(END)
@END
    0;JMP
    