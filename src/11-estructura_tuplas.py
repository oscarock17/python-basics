"""
==========================
    ESTRUCTURAS: TUPLAS
==========================

📘 Descripción:
Las tuplas en Python (`tuple`) son colecciones **ordenadas e inmutables**.
A diferencia de las listas, no se pueden modificar después de su creación.

📌 Características:
- Permiten almacenar datos de distintos tipos.
- Se definen con paréntesis: ( ... )
- Son más rápidas y seguras que las listas cuando no se requiere modificar los datos.
"""

# -------------------------------
# 1️⃣ Creación de tuplas
# -------------------------------
tupla = (1, 2, 3, 4, 5)
print(f"La tupla es: {tupla}")
print(f"El tipo de la tupla es: {type(tupla)}")

# Tupla con distintos tipos de datos
tupla_mixta = (5, 4.67, "José", False)
print(tupla_mixta)

# Tuplas vacías
tupla_vacia_1 = tuple()
tupla_vacia_2 = ()
print(tupla_vacia_1, tupla_vacia_2)

# Tupla con un solo elemento (¡importante la coma!)
tupla_un_elemento = (8,)
print(tupla_un_elemento, type(tupla_un_elemento))

# -------------------------------
# 2️⃣ Conversión entre tipos
# -------------------------------
cadena = "Hola mundo"
tupla_desde_cadena = tuple(cadena)
print(tupla_desde_cadena)

# Tupla → Cadena (sin separador)
tupla_letras = ('H', 'o', 'l', 'a')
cadena = "".join(tupla_letras)
print(cadena)

# Tupla → Cadena (con separador)
frutas = ("Manzana", "Uva", "Pera")
cadena = ",".join(frutas)
print(cadena)

# -------------------------------
# 3️⃣ Acceso a elementos y slicing
# -------------------------------
frutas = ("Manzana", "Plátano", "Pera")
print(frutas[0], frutas[1], frutas[2])
print(frutas[-1], frutas[-2], frutas[-3])  # Acceso inverso

# Slicing
numeros = (0,1,2,3,4,5,6,7,8,9)
print(numeros[0:5])   # primeros 5
print(numeros[-5:])   # últimos 5

# -------------------------------
# 4️⃣ Desempaquetado de tuplas
# -------------------------------
frutas = ("Manzana", "Plátano", "Pera")
f1, f2, f3 = frutas
print(f1, f2, f3)

# Desempaquetado extendido (*)
frutas = ("Manzana", "Plátano", "Pera", "Uva", "Sandía", "Fresa")
f1, *f2, f3 = frutas
print(f1, f2, f3)

# Intercambio de valores
fruta1, fruta2 = "Manzana", "Pera"
print(f"Antes: {fruta1}, {fruta2}")
fruta1, fruta2 = fruta2, fruta1
print(f"Después: {fruta1}, {fruta2}")

# -------------------------------
# 5️⃣ Operaciones comunes
# -------------------------------
numeros = (0,1,2,3,4,5,6,7,8,9)
print("Tupla invertida:", numeros[::-1])
print("Tupla invertida (reversed):", tuple(reversed(numeros)))

# Buscar elementos
frutas = ("Manzana", "Plátano", "Pera")
indice = frutas.index("Plátano")
print(f"Índice de 'Plátano': {indice}")

# Pertenencia
print("Manzana" in frutas)
print("Mango" not in frutas)

# Contar ocurrencias
frutas = ("Manzana", "Manzana", "Pera", "Plátano", "Pera", "Pera")
print("Número de 'Pera':", frutas.count("Pera"))

# Ordenar tuplas (retorna lista)
frutas = ("Fresa", "Uva", "Manzana", "Plátano", "Sandía", "Pera")
print(sorted(frutas))
print(sorted(frutas, reverse=True))

# -------------------------------
# 6️⃣ Iteración
# -------------------------------
frutas = ("Uva", "Manzana", "Pera", "Sandía")
for fruta in frutas:
    print(fruta)

# Enumerar
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# Iterar sobre múltiples tuplas
frutas1 = ("Sandía", "Pera", "Plátano")
frutas2 = ("Uva", "Manzana", "Fresa")
for f1, f2 in zip(frutas1, frutas2):
    print(f"{f1} - {f2}")

# -------------------------------
# 7️⃣ Otras operaciones útiles
# -------------------------------
numeros = (1,7,4,9,2)
print("Suma:", sum(numeros))
print("Mínimo:", min(numeros))
print("Máximo:", max(numeros))
print("Longitud:", len(numeros))

# Copia de una tupla
frutas = ("Sandía", "Pera", "Plátano")
frutas_copia = frutas
print(frutas_copia)

# Tupla de tuplas
tupla_de_tuplas = ((1,2,3),(4,5,6),(7,8,9))
print(tupla_de_tuplas)
print(tupla_de_tuplas[0])
