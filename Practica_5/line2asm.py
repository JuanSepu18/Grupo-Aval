import funciones_dic_1 as f1
import funciones_dic_2 as f2
import funciones_dic_3 as f3

contador_etiquetas = 0

def get_dic_1():
    dic_1 = {
        "add" : f1.Add,
        "sub" : f1.Sub,
        "neg" : f1.Neg,
        "and" : f1.And,
        "or"  : f1.Or,
        "not" : f1.Not,
        "end" : f1.End,
        "eq"  : f1.Eq,
        "gt"  : f1.Gt,
        "lt"  : f1.Lt
    }

    return dic_1

def tipo_1(linea):
    dic_1 = get_dic_1()
    retorno = ""

    if(linea.line[0] == "eq" or linea.line[0] == "gt" or linea.line[0] == "lt"):
        global contador_etiquetas
        retorno = dic_1[linea.line[0]](contador_etiquetas)
        contador_etiquetas = contador_etiquetas+1
    else:
        retorno = dic_1[linea.line[0]]()

    return retorno

def get_dic_2():
    dic_2 = {
        "label" : f2.Label,
        "goto" : f2.Goto,
        "if-goto" : f2.If_got
    }

    return dic_2

def tipo_2(linea):
    dic_2 = get_dic_2()
    retorno = dic_2[linea.line[0]](linea.line[1])

    return retorno

def get_dic_3():
    dic_3 = {
        "push" : f3.Push,
        "pop" : f3.Pop,
        "function" : f3.Function,
        "call" : f3.Call
    }

    return dic_3

def tipo_3(linea):
    dic_3 = get_dic_3()
    retorno = dic_3[linea.line[0]](linea.line[1], linea.line[2])

    return retorno