# diccionarios😊
los dicionarios son la forma mas comun almacenar datos estructurados de objetos que nos rodea en el mundo al igual que las listas que guardan informacion en `elementos` de igual manera los diccionarios almacena sus datos en `elementos` separados por comas.
la diferencia es que las listas almacenan los elementos por `indice` y `valor`.
y los diccionarios almacenan los elementos `clave:valor`.

**ejemplo:**🤞
```python
vocales:list[str]=['a','e','i','o','u']
# indices           0   1   2   3    4 
# un elemento en una lista esta conformado por dos cositas el indice y su valor.
# para acceder un valor en una lista 
vocales[2] # i
alumno:dict={'nombre':'yaqueli','edad':40}
# un elemnto es un diccionario esta conformado por clave:valor
# para acceder a un diccionario
alumno["nombre"] # yaqueli
```
## acceder a elemento
- **por clave (forma directa)** 😊
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celia@email.com"
}
print(persona)["edad"]) #16
print(persona["email"]) #celi@email.com
```
- **por su metodo (forma mas segura)** 😊
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
    "ciudad":"cabo verde",
    "email":"celia@email.com"
}
print(persona.get("nombre")) #celia
# la diferencia de este metodo es que nos permite manejar errores
print(persona.get("telefono")) #Nome
print(persona.get("telefono","no disponible")) # si la clave telefono no existe no mostra Nome si no el segundo parametro que le pasemos al metodo get.
```
## modificar elementos
- **cambiar un valor existente** 😊
```python
persona:dict={
    "nombre":"celia",
    "edad":16,
}
persona["edad"]=19
# agregar una nueva clave:valor
persona["carrera"]="agro"
# si la clave no existe se crea automaticamente. si existe se actualiza
```
📔## agregar/actualizar multiples elementos 🤞
para esto tenemos que hacer uso de el metodo`update`
se puede agregar si los pares de `clave:valor` no existe y actualizar si el `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":29745628638662
}
# actulizar usando el metodo .update tengo dos maneras de usar este metodo
# 1. diccionarios
tienda.update({"ruc":83274746891647,"telefono":939915259})
# 2. pares clave=valor.
tirnda.update(h_atencion="9-12",gerente="kevin")
```
📔## eliminar elemento 🤞🐼
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":29745628638662
}
el_eliminado=tienda.pop("ruc")
# para limpiar todo el diccionario
tienda.clear()
```