# este tipo de dato sirve para alamacenar informacion de tipo texto, texto simple o texto intenso.
# para almacenar un dato de tipo texto la informacion debera estar encerradsa entre comillas ("",'',"""""")
## - comillas dobles ("")
## - comillas simples ('')
## - docstring ("""""",'''''')
nombre_instituto:str ="IESTP-JMA"
nombre_curso:str = 'lenguaje de pro.'
descripcion_curso:str ="""
el curso de "lenguaje de proghramacion",
tiene una duracion de un semestre 
educativo con 6 horas semanales y 
aprender a programar en el lenguaje 
"python"
"""

## los string tienen funciones basicas para poder interactuar con los datos que estamos almacenando
## la estructura de una funcion es la siguiente
## nombre_funcion(argumento)
## *argumento - es un valor que se le pasa a una funcion, funcion que en base a su programacion retornara otro valor distinto al pasado por el argumento
# funcion para mostar informacion por terminal
print("hola mundo") # salida: hola mundo
print("hola","mundo") #salida: hola mundo
# funcion para mostar la cantidad de caracteres que tiene un string-texto
texto:str = "soy yaqueli"
cantidad_caracteres:int = len(texto)
print("cantidad de caracteres:",cantidad_caracteres)

# forma de acceder a un caracter en especial 
## para esto hacemos uso de la notacion de corchete []
## para esto tenemos que entender que python asigna a cada caracteres con un indice de base creo

# ejemplo: celia
# indices 01234
nombre_celia:str ="celia"
print(nombre_celia)
print(nombre_celia[2])

# troceado de texto
## para esto se utiliza la notacion de corchetes con la diferencia que se debe indicar un indice inicial y un indice final del texto a extrar. 
## texto[i_inicial:i_final] 
cocales:str ="aeiou"
print(vocales[1:3])
print(vocales[3:])
print(vocales[:3])

