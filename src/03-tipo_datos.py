# 03-tipos_datos.py

"""
📌 Tipos de Datos en Python

Tipos básicos:
- int
- float
- bool
- str

Tipos avanzados:
- list
- tuple
- set
- dict
"""

print("\n--- TIPOS BÁSICOS ---")

# Enteros
num1, num2 = 12, 6
print("Suma:", num1 + num2, type(num1 + num2))
print("Resta:", num1 - num2, type(num1 - num2))
print("Multiplicación:", num1 * num2, type(num1 * num2))
print("División entera:", num1 // num2, type(num1 // num2))
print("Módulo:", num1 % num2, type(num1 % num2))

# Flotantes
celsius = 24.8
fahrenheit = celsius * 9 / 5 + 32
print("\nCelsius:", celsius, "| Fahrenheit:", fahrenheit, type(fahrenheit))

# Booleanos
a, b = 4, 3
print("\na == b:", a == b, type(a == b))

# Strings
nombre, curso = "Oscar", "Python"
print(f"\nEste curso de {curso} fue realizado por {nombre}")

print("\n--- TIPOS AVANZADOS ---")

# Listas
lista = [5, 4.29, 2 + 2j, True, "Mandarina"]
print("Lista:", lista, type(lista))

# Tuplas
tupla = (5, 4.29, 2 + 2j, True, "Manzana")
print("Tupla:", tupla, type(tupla))

# Conjuntos
conjunto = {5, 5.34, 2 + 2j, True, "Manzana"}
print("Conjunto:", conjunto, type(conjunto))

# Diccionarios
diccionario = {
    "nombre": "Oscar Diaz",
    "edad": 34,
    "ciudad": "Bogotá",
    "estatura": 1.76,
}
print("Diccionario:", diccionario, type(diccionario))
print("Nombre:", diccionario['nombre'], type(diccionario['nombre']))
print("Edad:", diccionario['edad'], type(diccionario['edad']))
