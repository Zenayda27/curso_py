# para declarar una variable en python usaremos la convencion snake_case
## reglas
### 1. el nombre de la variable debe indicar que dato se esta almacenado
### 2. las variables no deben contener nimeros ni carcteres especiales(,7,1,?
nombe_curso="lenguaje de prgramacion "
credito_curso=3
horas_semanales_curso=6
# ADVERTENCIA - los variables son mutables 
print(credito_curso) #salida:3
credito_curso=10
print(creditos_curso) #salida;10

#NOTA IMPORTANTE PARA TODO EL CURSO - cada vez que declaremos variables usaremos anotaciones para indicar que tipo de dato se va a almacenar

nombre_alumno:str ="deduardo"
edad_alumno:int = 28
estatura_alumno:float = 1.59
asistencia_alumno:bool = True
amigos_alumno:list = []
direccion_alumno:dict = {"n_calle":"psj belen","numero_casa":230,"barrio":ccayao
}

# Asignacion de un varaible a otra variable
edad_alumno:int=20
edad_docente:int=eded_alumno

## IMPORTANTE NO OLVIDAR
### un decorador en python nos indica que tipo de dato vga alamacenar muestra variables 
### los decoradores que python trae por efecto son:
######### datos primitivos #########
### :int - enteros
### :float - decimales, como flotante
### :str - string texto 
### :bool - datos boleanos true o false

######### datos estructurados #########
# decoradores para datos estructurados 
### :lista - listas
### :dict - diccionarios

## como hacemos uso de las variables 
## para hacer uso del dato alamacenado enuna variable basta con hacer el llamado del nombre del variable
primer_numero:int =30
segundo_numero:int =20
suma: int =  primer_numero +segundo_numero
