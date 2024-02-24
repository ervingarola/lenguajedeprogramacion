# listas 
lista=[1,2,3,"MANZANA ",15.6,True]
print(lista)

# Imprimir elemeto de la lista 
print(lista[0])
#tamaño de lista
tam = len (lista)
print(f"el tamño es {tam}")
#imprimir el ultimo valor 
print(lista[tam-1])

# imprimir los primeros tre elementos 
print(lista[0:3])
# imprimprimir los elementos 4 hasta 6
print(lista[3:7])
#agregar un elemento a la lista 
lista.append("artola")
print(lista)

#imprimir los ultimos tres elementos de la lista
final = len(lista)
inicio= final-3
print(lista[inicio: final +1])
#eliminar manzana

lista.remove("MANZANA")
lista.remove("artola")

#ordenar lsita 
lista.sort()
print(lista)