def sumaTodos (limitTo):
    resultado=0
    for i in range (0,limitTo+1):
        resultado +=i
    return resultado

def sumatodosLosCuadrados (limitTo):
    resultado=0
    for i in range(limitTo+1):
        resultado += i*i
    return resultado
print (sumatodosLosCuadrados(3))
print(sumaTodos(100))

