contador_funciones = 0

def error_segmento_invalido():
    print("Error: el segmento que se ha pasado es invalido")

def crear_registro(segmento, indice):
    if (segmento == "static"):
        return "16"
    if (segmento == "local"):
        return "LCL"
    if (segmento == "argument"):
        return "ARG"
    if (segmento == "this"):
        return "THIS"
    if (segmento == "that"):
        return "THAT"
    if (segmento == "pointer"):
        return "R" + str(3 + int(indice))
    if (segmento == "temp"):
        return "R" + str(5 + int(indice))

    return "registro" + "." + str(indice)

def Push(segmento, indice):
    registro =  crear_registro(segmento, indice)
    retorno = ""

    if(segmento == "constant"):
        retorno = """@""" + indice + """
    D=A
@SP
    A=M
    M=D
    @SP
    M=M+1
    """
    elif(segmento == "pointer" or segmento == "temp"):
        retorno = """@""" + registro + """
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
    """

    elif(segmento == "static"):
        retorno = """@""" + registro + """
    D=A
@""" + indice + """
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
    """
    
    elif(segmento == "argument" or segmento == "local" or 
         segmento == "this" or segmento == "that"):
       retorno = """@""" + registro + """
    D=M
@""" + indice + """
    A=D+A
    D=M
@SP
    A=M
    M=D
@SP
    M=M+1
    """ 
       
    else:
        raise error_segmento_invalido()
    
    return retorno
        
def Pop(segmento, indice):
    registro =  crear_registro(segmento, indice)
    retorno = ""

    if(segmento == "constant"):
        raise error_segmento_invalido()
    elif(segmento == "static"):
        retorno = """@""" + registro + """
    D=A
@""" + indice +"""
    D=D+A
@R13
    M=D
@SP
    AM=M-1
    D=M
@R13
    A=M
    M=D
    """
        
    elif(segmento == "temp" or segmento == "pointer"):
        retorno = """@SP
    AM=M-1
    D=M
@""" + registro + """
    M=D
    """
        
    elif(segmento == "argument" or segmento == "local" or 
         segmento == "this" or segmento == "that"):
            retorno = """@""" + registro + """
    D=M
@""" + indice +"""
    D=D+A
@R13
    M=D
@SP
    AM=M-1
    D=M
@R13
    A=M
    M=D
    """
    
    else:
        raise error_segmento_invalido()
    
    return retorno
        

def Function(nombre_funcion, cantidad_variables):
    retorno = """(""" + nombre_funcion + """)
"""
    for i in range(int(cantidad_variables), 0, -1):
        retorno = retorno+"""@SP
    AM=M+1
    A=A-1
    M=0
"""
    return retorno

def Call(nombre_funcion, cantidad_argumentos):
    global contador_funciones
    return_address = "call_" + nombre_funcion + "_" + str(contador_funciones)
    retorno = """@""" + return_address + """
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
@""" + str(cantidad_argumentos) + """
    D=D-A
@ARG
    M=D
@SP
    D=M
@LCL
    M=D
@""" + nombre_funcion + """
    0;JMP
(""" + return_address + """)
"""

    contador_funciones = contador_funciones+1

    return retorno
