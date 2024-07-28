""" Las listas son estructuras de datos que permiten almacenar elementos de manera ordenada. Se definen entre corchetes y sus elementos se separan por comas. Entre las características principales de una lista encontramos que son ordenadas. Los elementos de una lista se mantienen en el orden en el que son declarados. """

juegoDeMesa=["poker","rompecabezas","uno"]
print(juegoDeMesa)

numeros=[5,96,3.3,'nuevo dato',5,96]
print(numeros)
print(numeros[3])
len(juegoDeMesa)#con esta funcion podemos saber la cantidad de elementos que tenemos en una lista
print(numeros[1:3])# con esto le pedimos que me traiga solo los elementos de dichas posiciones 

nuevaLista=[juegoDeMesa,"otro dato",numeros]# combine las 2 listas anteriores en una nueva
print(nuevaLista)

print(nuevaLista[0][1])# asi es como se navega dentro de la lista que ya tiene otra lista adentro, el resultado es "rompecabezas"


juegoDeMesa[0]='jenga'#con esto le decimos que reemplazamos el contenido de una posicion por otro contenido
print(juegoDeMesa)

juegoDeMesa.append("poker")# con esta funcion agrego un nuevo elemento al final de la lista
print(juegoDeMesa)

juegoDeMesa.extend(numeros)# con esta funcion .extend podemos agregar una lista al final de la nuestra agregandola en una sola
print(juegoDeMesa)