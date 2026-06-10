lista_vacia:list=[]
print( len(lista_vacia))
# por regla el nombre de la variable no debe tener el tipo de dato que se va almacenar
amores:list[str]=['mama','papa','hermano']

frutas: list[str]=["🍎","🍊","🍇","🍒"]
#posicion o indice
#acceder al tercer elemento
print (frutas[2])
#acceder al 2 elemento por su indice negativo
print(frutas[-3])

## modificar el ultimo elemento con una maranja
frutas[-1]="🍊"
print(frutas)
## sclicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcus']
# si deseamos que los datos extraidos sean persistentes osea se mantengan almacenados durante la ejecucion de mi programa los almaceno en una variable
datos_extraidos:list[str]=ciudades[-2:]
# si solo deseo mostrar y no almacenar el slicing lo realizo en el print
print(ciudades[0:3])
print(datos_extraidos)
## remplazo de elementos por slicing
numeros_pares:list[int]=['1','2','4','6','8','10']
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modificada es: {num_pares}")
