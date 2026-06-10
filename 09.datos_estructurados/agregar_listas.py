## deseamos agragar en una lista vacia los nombres de los paises que participaran en el mundial, desarrolar el programa que haga posible de esta tarea
#primera forma
paises:list[str]=[]
paises.append("peru")
print(paises)
# segunda forma
pais:str=input("ingresa el nombre del pais")
paises.append(paises)
print(paises)
# tercer forma
rango:int=int(input("ingresala cantidad de pais que deseas agregar:"))
for i in range(5):
    nuevos_paises:str=input("ingrese un pais")
    paises.append(nuevos_paises)
print(paises)
