# modulos y librerias estandar
# libreria estandar typing tipar datos a listas y diccionarios para hacer mas optimo el codigo
# modulo es una porcion de codigo utilizable, para poder usarlo necesitamos importa la aparte del codigo que deseamos utilizar

# entre codigo estoy importando desde 1 libreria typing la funcion union 
# union me permite tipar una coleccion de tipos que si no sabes el tipo de dato con union le podemos pasar una lista de los posibles tipos de datos que puede tener mi valor. 
from typing import Union
# sin libreria
#alumno:dict[str:str|int]
alumnos:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":74420023,
    "nombre":"yaqueli",
    "edad":20,
    "matricula":True
}
#accerder
## clasica
print(alumno["dni"])
print(alumno["tricula"])
## metodos
print(alumno.get("edad","valor no encontrado"))
# crear/modificar
print(alumno)
alumno["nombre"]="otro" # si existe la clave actualiza el valor
alumno["ruc"]="27985529026" # si no existe la clave lo crea
print(alumno)
# crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
# eliminar
alumno.pop("carrera")
print(f"el elemento eliminado es: {eliminado}")
print(f"mi nuevo diccionario {alumno}")

