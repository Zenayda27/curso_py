# librerias estandar de python
- cuales son 
import sys
import pprint

# Lista todos los módulos estándar disponibles
standard_libs = sorted([name for name, module in sys.modules.items() if module and hasattr(module, '__file__') and module.__file__.startswith(sys.prefix)])
pprint.pprint(standard_libs)

- cuales son los mas usados 
import os
import json
from datetime import datetime
from collections import Counter

# Usando os
print(os.listdir())  # Lista archivos en el directorio actual

# Usando json
data = {"nombre": "Ana", "edad": 30}
json_str = json.dumps(data)
print(json_str)

# Usando datetime
print(datetime.now())

# Usando collections
palabras = ["hola", "mundo", "hola", "python"]
print(Counter(palabras))  # Cuenta repeticiones: {'hola': 2, 'mundo': 1, 'python': 1}

- y las formas de incluirlas en nuestros archivos de python 
import re

texto = "Mi número de teléfono es 987-654-3210."
patron = r"\d{3}-\d{3}-\d{4}"  # Busca un número de teléfono en formato XXX-XXX-XXXX
resultado = re.search(patron, texto)

if resultado:
    print("Número encontrado:", resultado.group())  # Salida: 987-654-3210
else:
    print("No se encontró el patrón.")

# modulos en python

"""Módulo para manejar fechas."""
from datetime import datetime

def fecha_actual():
    """Devuelve la fecha actual en formato YYYY-MM-DD."""
    return datetime.now().strftime("%Y-%m-%d")

def es_anio_bisiesto(anio):
    """Devuelve True si el año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)