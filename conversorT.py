class Termometro():
    def __init__(self): #constructor en vacio
        self.__unidadM='C'
        self.__temperatura=0

    
    def __str__(self): #impresion
        return '{}º {}' .format(self.__temperatura, self.__unidadM)
    
    def unidadMedida(self, uniM=None):#getter
        if uniM == None:
            return self.__unidadM
        else:
            if uniM=='F' or uniM=='C':
                self._unidadM=uniM
    def temp(self, temperatura=None): #setter
        if temperatura==None:
            return self.__temperatura
        else:
            self.__temperatura=temperatura
            
    def __conversor(self, temperatura, unidad):
        if unidad=='C':
            return'{}º F'.format(temperatura *9/5+32)
        elif unidad=='F':
            return '{}ºC'.format((temperatura-32)*5/9)
        else:
            return 'unidad incorrecta'
            
    def mide(self, uniM=None):
        if uniM==None or uniM==self.__unidadM:
            return self.__str__()
        else:
            if uniM=='F' or uniM=='C':
                return self.__conversor(self.__temperatura, self.__unidadM)
            else:
                return self.__str__()