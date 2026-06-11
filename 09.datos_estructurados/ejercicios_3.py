alumnos:list[str]=['deduardo','noemi','victor','emerson','yo']
print(alumnos)
# iliminar por indice
alumnos.remove('yo')
print(alumnos)
# eliminar el ultimo valor por efecto
alumnos.pop()
print(alumnos)
# popo tambien elimina elementos por indice
### el metodo pop tiene la caracteristica de recuperar el elemento eliminado eso quiere decir que podemos almacenarlo una varible
alumnos.pop(1)
print(f"mi lista de desaprobados sera: {alumnos}")

# tengo una lista de marcas de veiculo(toyota,nissan,datsun,daewod,simo mack,mazda,honda), crear un programa que realize lo siguienteee
"""
1. eliminar el 5 elemento
2. en su lugar egregar la marca mitsubishi
3. buscar nissan y mostar su valor por terminal
4. mostrar si existe honda en mi lista de vehiculos 
"""
# Lista de vehículos
vehiculos = ["toyota", "nissan", "datsun", "daewod", "simo marck", "mazda", "honda"]

# Eliminar el 5to elemento (posición 4)
vehiculos.pop(4)

# Agregar Mitsubishi en su lugar
vehiculos.insert(4, "mitsubishi")

# Buscar Nissan y mostrar su posición
if "nissan" in vehiculos:
    print("Nissan se encuentra en la posición:", vehiculos.index("nissan"))

# Verificar si Honda existe
if "honda" in vehiculos:
    print("Honda sí existe en la lista.")
else:
    print("Honda no existe en la lista.")

# Mostrar lista final
print("Lista final de vehículos:", vehiculos)