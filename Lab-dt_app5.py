#EJERCICIO 1
#LISTA DE VARIOS TIPOS
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
myMixedTypeList2 = [423,32, 290578, 1.02, False, True, "My cat is on the bed.", "45"]

#USO DEL FOR
for item in myMixedTypeList2:
    print("{} is of the data type {}".format(item,type(item)))
    
#EL FOR ALMACENA DE FORMA TEMPORAL LOS VALORES     