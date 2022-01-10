from functools import reduce

def doble(x):
    return x+x
lista =[1,3,-1,15,9]

listadobles=map(lambda x: x*2, lista)
listaDobles1=map(doble,lista)

def esPar(x):
    return x%2==0

listaPares=filter (lambda x:x%2==0,lista)
listaPares1=filter (esPar,lista)
#filter comprueba y si es true te lo guarda

sumatorio=reduce(lambda x,y:x+y,lista)
#reduce todo el array en un solo numero en este caso le hemos dicho que los sume todos
sumatorio=reduce(lambda x,y:x+y,range(101))
#queremos realizar un sumatorio de los 100 numeros
sumatorioDobles=reduce(lambda x,y:x+y*2,lista)
