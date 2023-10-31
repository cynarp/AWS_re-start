##EJERCICIO 1 

#LISTA
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
#ACCESO A CONTENIDO DE LA LISTA DE ACUERDO A LA POSICIÓN
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
#MODIFICACIÓN DE LOS VALORES DE UNA LISTA 
myFruitList[2] = "orange"
print(myFruitList)

#EJERCICIO 2
#tuple - lista que no se puede modificar se usan parentesis en lugar de corchetes
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
#acceso a contnido de la tupla por posición
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#EJERCICIO 3
#DEFINICION DE DICCIONARIO - LISTA QUE TIENE NOMBRES ASINADOS (CLAVES)
myFavoriteFruitDictionary = {"Akua" : "apple", "Saanvi" : "banana", "Paulo" : "pineapple"}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#ACCESO AL CONTENIDO DEL DICCIONARIO POR NOMBRE (CORCHETES PARA AGREGAR VALOR)
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])