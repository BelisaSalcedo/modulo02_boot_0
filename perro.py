class Dog():
    def __init__(self):
        self.nombre=''
        self.edad=None
        self.peso=None
    def ladrar (loquesea):
        if self.peso ==None:
            print ('Soy un fantasma')
        if loquesea.peso >= 8:
            print ('¡GUA GUAUU!')
        else:
            print('Gua guau')

class Perro ():
    def __init__(self, n, e, p): #metodo inicial de todo objeto
        self.nombre=n
        self.edad=e
        self.peso=p
    def ladrar (loquesea):
        if loquesea.peso >= 8:
            print ('¡GUA GUAUU!')
        else:
            print('Gua guau')
    def __str__(self): #metodo especifico para devolver una cadena
        return 'Perro {}, e:{}, p{}'.format(self.nombre,self.edad,self.peso)

class PerroAsistencia(Perro):
    def __init__(self,nombre,edad,peso,amo):
        Perro.__init__(self,nombre,edad,peso)
        self.amo=amo
        self.__trabajando=False
        
    def __str__(self): #metodo especifico para devolver una cadena
        return 'Perro de Asistencia de {}'.format(self.amo)
    
    def pasear(self):
        print('{} ayudo a mi dueño {} a pasear'.format(self.nombre,self.amo))
    
    def ladrar(self):
        if self.__trabajando:
            print('ssshhh no puedo ladrar')
        else:
            Perro.ladrar(self)
    def trabajando(self, valor=None):
        if valor==None:
            return self.__trabajando
        else:
            self.__trabajando=valor
        
    