#realiza una lista que tenga la funcion lambda para sacar el numero par
mi_lista4 = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,66,73,80,90,100]
mi_lista10 = list(filter(lambda x: x%2==0, mi_lista4)) #que hace la x en este caso?:
print(f"Los numeros pares son:", mi_lista10)

def cuadrado(x):
    return x**2
mi_lista11 = list(map(cuadrado, mi_lista4))
print(f"Los cuadrados de la lista son:", mi_lista11)

def cuadrado2():
    milist2 = [2,3,6,8,10]
    cuadrado = [n**2 for n in milist2]
    return cuadrado
print(cuadrado2())


#cual es la estructura de una list comprehension?
#mi_lista = [i for i in (name_lista)]

#utilizar la funcion lambda en mi_lista4 y haz cuanquier calculo que quieras
mi_lista5 = list(map(lambda x: x**2, mi_lista4))
print(f"Los cuadrados de la lista son:", mi_lista5)

#ahora utiliza la funcion filter para solo mostrar los numeros en orden los numeros con mayor cantidad de 0
mi_lista6 = list(filter(lambda x: x%10==0, mi_lista5)) #que hace la x%10==0 en este caso?:
print(f"Los numeros con mayor cantidad de 0 son:", mi_lista6)


# lista1_5 = [1,2,3,4,5]
#
# lista1_5.append(6) #agrega un elemento al final de la lista
# lista1_5.insert(0,0) #agrega un elemento en la posicion que le indiques
# lista1_5.extend([7,8,9,10]) #agrega varios elementos al final de la lista
# lista1_5.remove(10) #elimina el elemento que le indiques
# lista1_5.pop() #elimina el ultimo elemento de la lista
# lista1_5.pop(0) #elimina el elemento de la posicion que le indiques
# lista1_5.clear() #elimina todos los elementos de la lista
# lista1_5.index(5) #devuelve el indice del elemento que le indiques (en este caso el 5)
# lista1_5.count(5) #devuelve cuantas veces se repite el elemento que le indiques
# lista1_5.sort() #ordena la lista de menor a mayor
# lista1_5.reverse() #ordena la lista de mayor a menor
# lista1_5.copy() #copia la lista
# lista1_5 = lista1_5 + lista1_5 #concatena dos listas
# lista1_5 = lista1_5 * 2 #multiplica los elementos de la lista por el numero que le indiques
# lista1_5 = [i for i in lista1_5] #crea una lista de los elementos de la lista
# lista1_5 = [i for i in lista1_5 if i%2==0] #crea una lista de los elementos pares de la lista
# lista1_5 = [i**2 for i in lista1_5] #crea una lista de los elementos al cuadrado de la lista
# lista1_5 = [i for i in lista1_5 if i%10==0] #crea una lista de los elementos con mayor cantidad de 0 de la lista
# lista1_5 = list(filter(lambda x: x%10==0, lista1_5)) #crea una lista de los elementos con mayor cantidad de 0 de la lista
# lista1_5 = list(map(lambda x: x**2, lista1_5)) #crea una lista de los elementos al cuadrado de la lista

# Ejercicio: Dada una lista de números enteros, escribe una función que:
# 1. Encuentre el número más grande en la lista.
# 2. Encuentre el número más pequeño en la lista.
# 3. Calcule la media de los números en la lista.

# Puedes usar la siguiente lista como ejemplo:
numeros = [4, 2, 9, 7, 5, 1, 8, 3, 6]
numeros.sort()
print(numeros[8])
print(numeros[0])
media = sum(numeros) / len(numeros)
print(media)

# Ejercicio: Dada una lista de números enteros, escribe una función que:
# 1. Encuentre todos los números pares en la lista.
# 2. Encuentre todos los números impares en la lista.
# 3. Calcule la suma de todos los números en la lista.

# Puedes usar la siguiente lista como ejemplo:
numeros2 = [4, 2, 9, 7, 5, 1, 8, 3, 6]
pares = list(filter(lambda x: x%2 == 0, numeros2))
print(pares)
impares = list(filter(lambda x: x%2 !=0, numeros2))
print(impares)
suma = sum(numeros2)
print(suma)


#esto hace lo mismo que arriba, pero menos eficiente
# Encuentra los números pares
#numeros2 = [4, 2, 9, 7, 5, 1, 8, 3, 6]
# pares = []
# for num in numeros2:
#     if num % 2 == 0:
#         pares.append(num)
# print(pares)
#
# # Encuentra los números impares
# impares = []
# for num in numeros2:
#     if num % 2 != 0:
#         impares.append(num)
# print(impares)
#
# # Calcula la suma de todos los números
# suma = 0
# for num in numeros2:
#     suma += num
# print(suma)

list20 = [1,2,3,4,5,6,7,8,9,10]
impares = list(filter(lambda x: x%2!=0, list20))
print(impares)

# Dada la siguiente lista de números:
numeros20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros20 if x%2==0], print(pares)

# Dada la siguiente lista de palabras:
palabras = ['manzana', 'banana', 'cereza', 'durazno', 'frambuesa', 'granada']

six_letter = [x for x in palabras if len(x) > 6]
print(six_letter)

b_word = list(filter(lambda x: x[0]=='b', palabras))
print(b_word)
# 1. Utiliza list comprehension para crear una nueva lista que contenga solo las palabras que tienen más de 6 letras de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo las palabras que comienzan con la letra 'b' de la lista original.

# Dada la siguiente lista de números:
numeros3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
multiplo10 = [x for x in numeros3 if x%10==0]
print(multiplo10)
multiplo20 = list(filter(lambda x: x%20==0, numeros3))
print(multiplo20)

# 1. Utiliza list comprehension para crear una nueva lista que contenga solo los números que son múltiplos de 10 de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo los números que son múltiplos de 20 de la lista original.

numeros4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadra = [x for x in numeros4 if x**2]
print(cuadra)
cubo = list(map(lambda x: x**3, numeros4))
print(cubo)

# 1. Utiliza list comprehension para crear una nueva lista que contenga el cuadrado de cada número de la lista original.
# 2. Utiliza una función lambda y la función map() para crear una nueva lista que contenga el cubo de cada número de la lista original.

palabras3 = ['gato', 'perro', 'elefante', 'jirafa', 'hipopótamo']
lettera = [x for x in palabras3 if x.count("a")]
print(lettera)
fiveletter = list(filter(lambda x: len(x) > 5, palabras3))
print(fiveletter)

# 1. Utiliza list comprehension para crear una nueva lista que contenga solo las palabras que tienen la letra 'a' de la lista original.
# 2. Utiliza una función lambda y la función filter() para crear una nueva lista que contenga solo las palabras que tienen más de 5 letras de la lista original.

from functools import reduce

numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Imprime: 24
