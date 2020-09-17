

numeros=[]#Crea la lista llamada numeros
cantidad=int(input("Indique la cantidad de números que ingresará: " ))
while cantidad>0:
    num=int(input("Ingrese un número: "))
    numeros.append(num)
    cantidad=cantidad-1
long=len(numeros)-1
cercano=max(numeros)**10
print("La lista de números es:",numeros)
while long>1:#Mientras que el largo de la lista sea mayor a 1, se analiza cual es el numero mas cercano al primero
    if abs(numeros[1]-numeros[0])<cercano:
        cercano=numeros[1]
    del numeros[1]
    long=long-1
print("El número más cercano al primer número es:",cercano)