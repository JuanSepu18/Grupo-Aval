class linea():
    def __init__(self, line):
        self.line = line.strip()
        self.tipo = 1
        self.limpiar()
        self.verificar()
        self.line = self.line.split()
        self.sel_tipo()

    def verificar(self):
        if self.line.startswith('//') or self.line == '':
            self.tipo = None

    def limpiar(self):
        indice = self.line.find('//')

        if(indice == 0):
            self.line = ''
        elif indice != -1:
            self.line = self.line[:indice]

        self.line = self.line.strip()
    
    def sel_tipo(self):
        if(self.tipo is not None):
            if(len(self.line) == 1):
                self.tipo = 1
            elif(len(self.line) == 2):
                self.tipo = 2
            elif (len(self.line) == 3):
                self.tipo = 3
            else:
                self.tipo = None