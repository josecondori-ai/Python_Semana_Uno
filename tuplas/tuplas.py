""" Las listas son estructuras de datos que permiten almacenar elementos de manera ordenada. Se definen entre corchetes y sus elementos se separan por comas. Entre las características principales de una lista encontramos que son ordenadas. Los elementos de una lista se mantienen en el orden en el que son declarados. """

comidas=("pizza","pollo",'fideos')
print(comidas)



#podemos no usar los parentesis, python interpreta esto como una tupla

comidasDos="empanadas","cereales","pescado"
print(comidasDos)

#accedemos a travez de los indices

print(comidas[1])

#esto NO SE PUEDE HACER

comidas[0]="tequeños"