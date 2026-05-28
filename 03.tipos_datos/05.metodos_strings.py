# metodo para convertir un texto en mayuscula 
texto_minuscula:str="hola"
print(texto_minuscula.upper())
# metodo para convertir un texto en minuscula
texto_mayuscula:str="HOLASS"
print(texto_mayuscula.lower())
# metodo para convertir solo la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para convertir la primera letra de cada palabra en mayuscula como un titulo
print(texto.title())

# metodo para quitar espacios 
texto_espacios:str="    osos    "
print(texto_espacios.strip())
# este motodo quita los espacios qu estan a la derecha e izquierda . si deseamos quitar solo los espacios en la izquierda usamos el metodo lstrip() y si deseamos quitar los espacios solo de la derecha usamos strinp()
print(texto_espacio.strip())

# metodo para buscar un caracter o conjunto de caracteres 
# fin retorna el indice donde comienza el texto a buscar si el texto no se encuentra retornara -1
parrafo:str="mi mama me ama yo amo a mi mama gianfranco" 
print(parrafo.find("gianfranco"))
print(parrafo[35:])

# metodo para reemplazar una parte del texto
texto_incorrecto:str="gianfranco es malo"
print(texto_incorrecto.replace("malo","bueno"))

# (metodo) operador binario de existencia
# este operador verifica si cierto texto existe o no dentro de otro retorna True si existe y False si no 
vocales:str="aeiouAEIOU"
print("a" in vocales)


# tarea averiguar que son y cuales son los operadores unarios, binarios y ternarios

# operadores unarios 
son los que trabajan con un solo Valor 
x = 5
print(-x)      # -5

y = True
print(not y)   # False
# operadores binarios 
son los mas usados trabajan con dos variables 
a = 10
b = 3
print(a + b)   # 13
print(a ** b)  # 1000
# operadores termarios
se le llama expresion condicional
# valor_si_verdaredo if condion else valor_si_falso

valor_si_verdadero if condición else valor_si_falso
edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

## realizar un programa que nos pida la contraseña es correcta el usuario podra ingresar caso contrario le dara el mensaje de contraseña incorrecta 

password_user:str=input("ingresa tu contraseña:")
print("bienvenido al sistema" if password_user=="hola1234"else "contraseña incorrecta")
