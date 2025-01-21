"""
Las palabras reservadas, son palabras exclusivas del
lenguaje de programación Python, que tienen un significado especial
y no pueden ser utilizadas como identificadores de variables, funciones
"""

# Lista de palabras reservadas
palabras_reservadas = [
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield'
]

#Las palabras reservadas no se deben de usar.Ejemplo:
nombre = "Karol"
print("Mi nombre es:",nombre)

#Concatenacion
nombre_completo = nombre + " " + "Karol"
print(nombre_completo)

#Obtener el total de palabras reservadas
print(len(palabras_reservadas))

#Esto no se debe de hacer
#class = "Programacion estructuradaa" 