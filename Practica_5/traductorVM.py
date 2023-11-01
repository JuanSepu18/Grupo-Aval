import sys
from lineas import linea as line
import line2asm as code

def main():
    lineas = []
    nombre_archivo = sys.argv[1]
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea = line(linea)
            if(linea.tipo == None):
                continue
            lineas.append(linea)

    nombre_archivo_asm = nombre_archivo[:nombre_archivo.find('.vm')] + ".asm"
    with open(nombre_archivo_asm, 'w') as archivo_asm:
        for linea in lineas:
            comando = ""
            #print(linea.line)
            if(linea.tipo == 1):
                comando = code.tipo_1(linea)
            elif(linea.tipo == 2):
                comando = code.tipo_2(linea)
            elif(linea.tipo == 3):
                comando = code.tipo_3(linea)
            archivo_asm.write(comando + '\n')
        archivo_asm.write(code.tipo_1(line("end")))
            
    
    print("Archivo creado satisfactoriamente")
    
    # contador = 0
    # for linea in lineas:
    #     comando = ""
    #     if(linea.tipo == 1):
    #         comando = code.tipo_1(linea)
    #     elif(linea.tipo == 2):
    #         comando = code.tipo_2(linea)
    #     elif(linea.tipo == 3):
    #         comando = code.tipo_3(linea)
        
    #     print(str(contador) + ": " + str(linea.line))
    #     print(comando+"\n")

    #     contador = contador + 1

if __name__ == '__main__':
    main()