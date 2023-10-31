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
    elif(segmento == "static" or segmento == "temp" or 
         segmento == "pointer"):
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
        
    elif(segmento == "argument" or segmento == "local" or 
         segmento == "this" or segmento == "that" or 
         segmento == "temp" or segmento == "pointer"):
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
        

def Function(segmento, indice):
    pass

def Call(segmento, indice):
    pass