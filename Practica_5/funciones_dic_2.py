def Label(etiqueta):
    codigo = """(""" + etiqueta + """)
    """

    return codigo

def Goto(etiqueta):
    codigo = """@""" + etiqueta + """
    0;JMP
    """

    return codigo

def If_got(etiqueta):
    codigo = """@SP
    AM=M-1
    D=M
@""" + etiqueta + """
    D;JNE
    """
    return codigo