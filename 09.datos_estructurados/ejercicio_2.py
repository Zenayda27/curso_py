# craer un programa que me permita agregar lista de comprar los siguientes ingredientes (trucha,cebolla,limon,culantro,pinguita de mono,papa,cancha)
ingrediente:list[str]=[]
# desarrollo
for i in range(7):
    ingrediente:str= input("ingrese tu ingrediente: ")
    ingrediente.append (ingrediente)
# datos de salida
print(ingredientes)

## crear un programa que agregue al principio de la lista del grupo de los paises participantes en el mundial
grupo_a:list[str]=[]
grupo_a.insert(0,"rep. checa")
# ["rep. checa"]
grupo_a.insert(0,"corea del sur")
#["corea del sur","rep. checa"]
grupo_a.insert(0,"sudafrica")
#["corea del sur","rep. checa"]
grupo_a.insert(0,"mexico")