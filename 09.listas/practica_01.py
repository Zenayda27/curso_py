# una ferreteria tiene separada en dos listas los siguientes productos 
"""
1. lista de productos de limpieza (10 productos)
2. lista de materiales de construccion (10 productos)
------------------------------------------------
el dueño desea realizar las siguientes acciones:
1. en su lista de productos de limpieza existe un material de construccion, debes eliminarlos y pasar el producto a lista que corresponde
2. indicar si en la lista de M.C existe cemento
3. en la lista de P.L buscar el producto lejia y cambiar su valor por lejia sapolio.
4. mostrar un mensaje donde se detalle cual es la lista de M.C y la lista de P.C y la lista de P.L formateado
"""
# de productos de limpieza (10 productos)
productos_limpieza:list[str] = ["lejia","detergente","jabon","escoba","cemento","desinfectante","cloro","esponja","trapeador","ambientador"] 
# Lista de materiales de construcción
materiales_construccion:list[str] = ["ladrillo","arena","piedra","fierro","alambre","cemento","madera","yeso","teja","pintura"]

#1. cambiar de lista al cemento
elemento_retirado=productos_limpieza.pop(productos_limpieza,index("cemento"))
materiales_construccion.append(elemento_retirado)

# 2. Verificar si existe cemento en M.C
existe:bool="cemento" in materiales_construccion:
print(f"existe el cemento?: {existe}")
## segunda opcion utilizando un operador ternario
print("cemento si existe" if existe else "cemento no existe")
#3. cambiar lejia por lejia sapolio
productos_limpieza.index("lejia")
productos_limpieza[buscar] = "lejia sapolio"
print(producto_limpieza)

    # 4. Mostrar listas formateadas
mensaje:str=f"""
    mi lista de productos de limpieza despues de las modificaciones queda de la sigiente manera4
    modificacion queda de la siguiente manera 
    {productos_limpieza}
    -------------------------------------------------
    mi lista de materiales de construccion despues de las modificaciones queda de la siguiente manera 
    {materiales_construccion}



