# utilizar tecnicas para unir string en un solo 
## concatenacion
# para esto usamos el operador de concatenacion +
# caundo este operador se encuentra entre dos textos se convierte en operador concatenacion cuando esta entre dos numeros es el operador adicion o (suma)
nombre:str="noemy" 
apellido:str="noseprofesor"
nombre_completo:str =nombre+" "+apellido
print(nombre_completo)#salida: noemy noseprofesor

## opcion mas optima de concatenacion
print(nombre_completo) #salida: noemy noseprofesor

## opcion mas optima de concatenacion
print(nombre,apellido)

## f-strings (tarea)🏡
# formato string esto sirve para formatear string con variables de python y para sus se requiere dee un f antes de escribir un string, si se desea incluir codigo python en el string se debe encerrar entre llaves {}
nombre:str ="Gianfranco"
edad:int = 14
# mensaje de salidanm diga hola mi nombre es {} y tengo {}
print (f"hola mi nombre es {nombre} y tengo {edad}")

## plantillas de string
nombre_cliente:str=input("ingrese tu nombre") 
ruc_cliente:int=input("ingrese ruc: ")
direccion_cliente:str=input("digite direccion: ")
codigo_producto:str=input("ingrese codigo producto ")
nombre_producto:str=input("ingrese nombre ")
precio_unidad:float=float(input("el precio del producto"))
cantidad_producto:float=float(input("cantodad a comprar: "))
precio_total:float=float= precio_unidad*cantidad_producto

 plantilla:str=f"""
cliente:{nombre_cliente}......ruc: {ruc_cliente}
direcci0n: {direccion_cliente}

codigo producto | nombre producto  | p_unidad  | cantidad
-------------------------------------------------
{codigo_producto}  {nombre_producto} {producto_unidad}  
{cantidad_oroducto}
----------------------------------------------------
el precio total de su compra es de:{precio_total}
"""
print(plantilla)

