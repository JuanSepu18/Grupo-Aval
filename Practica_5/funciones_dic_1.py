def Add():
    codigo = """@SP
    AM=M-1
    D=M
    A=A-1
    M=D+M
    """

    return codigo

def Sub():
    codigo = """@SP
    AM=M-1
    D=M
    A=A-1
    M=M-D
    """

    return codigo

def Neg():
    codigo = """@SP
    A=M
    A=A-1
    M=-M
    """

    return codigo

def And():
    codigo = """@SP
    AM=M-1
    D=M
    A=A-1
    M=D&M
    """

    return codigo

def Or():
    codigo = """@SP
    AM=M-1
    D=M
    A=A-1
    M=D|M
    """

    return codigo

def Not():
    codigo =  """@SP
    A=M
    A=A-1
    M=!M
    """

    return codigo

def End():
    codigo = """(END)
@END
    0;JMP
    """

    return codigo

def text_comparador(tipo_jump, numero):
    label_true = "jump_true_" + str(numero)
    label_false = "jump_false_" + str(numero)

    codigo = """@SP
    AM=M-1
    D=M
@SP
    AM=M-1
    D=M-D
@""" + label_true + """
    D;""" + tipo_jump + """
    D=0
@""" + label_false + """
    0;JMP
(""" + label_true + """)
    D=-1
(""" + label_false + """)
@SP
    A=M
    M=D
@SP
    M=M+1
    """

    return codigo

def Eq(numero):
    tipo_jump = "JEQ"
    return text_comparador(tipo_jump, numero)


def Gt(numero):
    tipo_jump = "JGT"
    return text_comparador(tipo_jump, numero)

def Lt(numero):
    tipo_jump = "JLT"
    return text_comparador(tipo_jump, numero)

def Return():
    Frame = "R13"
    Ret = "R14"

    retorno = """@LCL
    D=M
@""" + Frame + """
    M=D
@""" + Frame + """
    D=M
@5
    D=D-A
    A=D
    D=M
@""" + Ret + """
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
    M=D-1
"""

    offset = 1
    for direc in ["@THAT", "@THIS", "@ARG", "@LCL"]:
        retorno = retorno + """@""" + Frame + """
    D=M
@""" + str(offset) + """
    D=D-A
    A=D
    D=M
    """ + direc + """
    M=D
"""
        offset += 1
    
    retorno = retorno + """@""" + Ret + """
    A=M
    0;JMP"""

    return retorno



#     retorno = """@LCL
#     D=M
# @R13
#     M=D
# @R13
#     M=D
# @5
#     A=D-A
#     D=M
# @R14
#     M=D
# @SP
#     AM=M-1
#     D=M
# @ARG
#     A=M
#     M=D
# @R13
#     D=M
# @1
#     A=D-A
#     D=M
# @THAT
#     M=D
# @R13
#     D=M
# @2
#     A=D-A
#     D=M
# @THIS
#     M=D
# @R13
#     D=M
# @3
#     A=D-A
#     D=M
# @ARG
#     M=D
# @R13
#     D=M
# @4
#     A=D-A
#     D=M
# @LCL
#     M=D
# @R14
#     A=M
#     0;JMP"""

    return retorno