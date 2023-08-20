import string

#ordena usando burbuja una lista numeros

def burbuja(array):
    for i in range (len(array)):
        for a in range(len(array)-1):
            if array[a]>array[a+1]:
                z=array[a+1]
                array[a+1]=array[a]
                array[a]=z
    print (f"Lista Ordenada: {array}")
    return array

#Data input
try:
    print("introduzca una lista de numeros separados por ',' para ordenar")
    string = input()
except EOFError:
    string = "5,1,4,2,8"

oldarray = string.split(",")
array1=[]


try:
    for a in oldarray:
        array1.append(int(a))
    burbuja(array1)

except ValueError:
    print("introduce bien numeros enteros separados por coma")

