class Perro ():
    def __init__(self, n, e, p):
        self.nombre=n
        self.edad=e
        self.peso=p
    def ladrar (loquesea):
        if loquesea.peso >= 8:
            print ('¡GUA GUAUU!')
        else:
            print('Gua guau')
    def __str__(self):
        return 'Perro {}, e:{}, p{}'.format(self.nombre,self.edad,self.peso)
    