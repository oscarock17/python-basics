# 04-casting.py

"""
📌 Casting en Python
Conversión de un tipo de dato a otro.
Funciones comunes:
- int(), float(), str(), bool()
- list(), tuple(), set(), dict()
"""

# 1. Cadena → Entero
cadena = "123"
numero_entero = int(cadena)
print("Cadena → Entero:", numero_entero, type(numero_entero))

# 2. Entero → Flotante
numero_entero = 10
numero_flotante = float(numero_entero)
print("Entero → Flotante:", numero_flotante, type(numero_flotante))

# 3. Flotante → Cadena
numero_flotante = 123.456
cadena = str(numero_flotante)
print("Flotante → Cadena:", cadena, type(cadena))

# 4. Número → Booleano
numero = 0.123
booleano = bool(numero)
print("Número → Booleano:", booleano, type(booleano))

# 5. Cadena → Lista
cadena = "Hola"
lista = list(cadena)
print("Cadena → Lista:", lista, type(lista))

# 6. Lista → Tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print("Lista → Tupla:", tupla, type(tupla))

# 7. Lista → Conjunto
lista = [1, 2, 3]
conjunto = set(lista)
print("Lista → Conjunto:", conjunto, type(conjunto))

# 8. Lista de tuplas → Diccionario
lista_de_tuplas = [("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")]
diccionario = dict(lista_de_tuplas)
print("Lista de tuplas → Diccionario:", diccionario, type(diccionario))
