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
frutas:list[str]=[🍎,🍊,🍇,🍒]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder por rango
Python: Puedes generar una secuencia usando la función range() para bucles. Por ejemplo, range(0, 10) genera números del 
 al 



## Diccionarios