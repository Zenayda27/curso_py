# Datos estructurados 
- tenemos 3 tipos de datos primarios (string, numerico, boleno)
- tenemos 2 tipos de datos estructurados (listas, diccionarios)
## Listas
son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener:
- listas de tipo numerica
- listas de tipo texto
- listas de tipo mixto
python nos permite acceder a estas listas a travez de indices, los indices son ascendentes empesando del numero 0.
### Creacion de listas 😊
para crear listas solo hasta encerrar los elementos que deseamos alamcenar con `[]` inmediatamente despues del operador de asignacion `=`
```python
# Creando una lista vacia
listas:list=[]# lista vacia
# lista numerica
# OJON: Los elementos de una lista 
lista_numerica:list[int]=[3,8,4]
listas_num_mixto:list[int|float]=[3.6,7,.7]
# listas de texto
amigos:list[str]=['eduardo','kevin']
# lista mixta
lista_mixta: list=['pedro',20,false,1.67]
```
### Acceder y modificar elementos de una lista 😊
para poder accerder a un elemento de la lista trabajamos con los indices que python se asigna a cada elemento tenemos:
- los indices positivos (comienzan de 0 y van de izquierda a derecha)
-  los indices negativos (comienzan de -1 y van de derecha a izquierda)
con estos indices podemos acceder al valor del elemento y tambien podremos modificarlos.
- por indice (posicion)
- por rango (slicing)
```python
frutas:list[str]=["🍎","🍊","🍇","🍒"]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder por rango
Python: Puedes generar una secuencia usando la función print(frutas[-3]) para bucles. Por ejemplo, range(0, 10) genera números del 

# modificar
frutas[3]="naranja"
- acceder y modificar por rango (slicing)
```python
vocales:str=['a','e','i','o','u']
# acceder a elemento por slicing
# esta tecnica nos permite accede a mas de un elemento en una sola linea de codigo
vocales[0:3]
## reemplazar elementos por slicing 
vocales[0:3]=['A','E','I']
```
### metodos para listas 
un metodo es una accion que puede realizar en una lista, los metodos por lo general se utilizan despues de la variable y se accede metodos a travez de un punto.
los metodos , agrega, modificar y eliminar
```python
# agregar elementos
## append
animales:list[str]=[]
animales.append("leon")
animales.append("gato")
# que el metodo append agrega los elementos en la ultima posicion de nuestra lista
## insert
numeros_pares:list[int]=[4,6,10]
numeros_pares.insert(0,2)
numeros_pares.insert(3,8)
amigo:list[str]=["juan","jose"]
amigo:list[str]=[1,20]
# eliminar elementos 
## eliminar por indice
vocales:list[str]=["a","e","i","o","u"]
del vocales[-1]
## eliminar por valor
vocales:list[str]=["a","e","i","o","u"]
vocales.remove("u")
## usando metodo pop
vocales:list[str]=["a","e","i","o","u"]
vocales.pop()
# en este caso pop elimina por defecto el ultimo elemento
vocales.pop(3)
# en este caso eliminara el elemento que se encuentre en la posicion 3

# buscar
## este metodo permite ubicar a travez del valor el primer elemento (la primera coincidencia) dentro de una lista, y devolvera el indice de ese valor, este metos es index
amantes:list[str]=['chapo','cristian','emerson','victor']
# quiero ubicar si en mi lista de infieles existe victor 
buscar:int=amantes.index("victor")# retorna un indice si existe 3
amantes[buscar]#victor
## busqueda por pertenencia
existe:bool="chapo" in amantes

```

## Diccionarios