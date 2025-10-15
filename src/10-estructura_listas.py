# ------------------------------
# ESTRUCTURAS DE DATOS: LISTAS
# ------------------------------

# Las listas en Python (tipo `list`) son colecciones ordenadas y mutables
# que pueden contener elementos de diferentes tipos de datos.
# Se definen utilizando corchetes [] y permiten agregar, modificar,
# eliminar y acceder a elementos de forma flexible.

print("=== Listas en Python ===")

# ------------------------------
# CREACIÓN DE LISTAS
# ------------------------------
lista = [1, 2, 3, 4, 5]
print(f"La lista es: {lista}")
print(f"El tipo de dato es: {type(lista)}")

# ------------------------------
# CONVERSIÓN ENTRE LISTAS Y CADENAS
# ------------------------------
print("\n--- Conversión entre listas y cadenas ---")

# Cadena -> Lista
cadena = "Hola mundo"
lista = list(cadena)
print(lista)

# Lista -> Cadena (sin espacios)
lista = ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
cadena = "".join(lista)
print(cadena)

# Lista -> Cadena (con separación)
lista = ["Este", "es", "un", "ejemplo"]
cadena = " ".join(lista)
print(cadena)

# Cadena -> Lista (usando split)
cadena = "Este es un ejemplo"
lista = cadena.split()
print(lista)

# ------------------------------
# ACCESO A ELEMENTOS
# ------------------------------
print("\n--- Acceso a elementos ---")
frutas = ["Manzana", "Plátano", "Pera"]
print(frutas[0])  # Primer elemento
print(frutas[1])
print(frutas[2])

# Índices negativos (desde el final)
print(frutas[-1])  # Último elemento
print(frutas[-2])
print(frutas[-3])

# ------------------------------
# SLICING (Trocear listas)
# ------------------------------
print("\n--- Slicing ---")
numeros = [0,1,2,3,4,5,6,7,8,9]
print(numeros[:5])     # Primeros 5 elementos
print(numeros[5:])     # Últimos 5 elementos
print(numeros[-5:])    # Últimos 5 con índice negativo
print(numeros[::2])    # Saltos de 2
print(numeros[::-1])   # Lista invertida

# ------------------------------
# AGREGAR ELEMENTOS
# ------------------------------
print("\n--- Agregar elementos ---")
frutas = ["Manzana", "Plátano", "Pera"]
frutas.append("Uva")  # Agrega al final
print(frutas)

frutas.insert(1, "Kiwi")  # Inserta en posición 1
print(frutas)

# ------------------------------
# CREAR LISTA DESDE CERO
# ------------------------------
print("\n--- Crear lista con append ---")
numeros = []
for i in range(10):
    numeros.append(i)
print(numeros)

# ------------------------------
# REPETIR Y COMBINAR LISTAS
# ------------------------------
print("\n--- Repetir y combinar ---")
frutas = ["Manzana", "Plátano"]
print(frutas * 3)

frutas_rojas = ["Fresa", "Cereza"]
frutas_verdes = ["Kiwi", "Pera"]
todas = frutas_rojas + frutas_verdes
print(todas)

# ------------------------------
# MODIFICAR ELEMENTOS
# ------------------------------
print("\n--- Modificar elementos ---")
frutas = ["Manzana", "Plátano", "Pera"]
frutas[0] = "Uva"
print(frutas)

# Reemplazo de rango
frutas[0:2] = ["Sandía"]
print(frutas)

# ------------------------------
# ELIMINAR ELEMENTOS
# ------------------------------
print("\n--- Eliminar elementos ---")
frutas = ["Manzana", "Plátano", "Pera"]
del frutas[1]
print(frutas)

frutas = ["Manzana", "Plátano", "Plátano", "Pera"]
frutas.remove("Plátano")  # Elimina primera ocurrencia
print(frutas)

frutas.clear()  # Borra todos los elementos
print(frutas)

# ------------------------------
# BÚSQUEDAS Y OPERACIONES
# ------------------------------
print("\n--- Búsqueda y operaciones ---")
frutas = ["Manzana", "Plátano", "Pera", "Plátano"]
print(frutas.index("Plátano"))  # Primer índice
print("Uva" in frutas)          # Verificar existencia
print(frutas.count("Plátano"))  # Contar repeticiones

# ------------------------------
# ORDENAMIENTO
# ------------------------------
print("\n--- Ordenamiento ---")
frutas = ["Uva", "Manzana", "Plátano", "Pera"]
print(sorted(frutas))               # Ordena sin modificar
print(sorted(frutas, reverse=True)) # Orden descendente
frutas.sort()                       # Ordena in place
print(frutas)

# ------------------------------
# ITERACIÓN
# ------------------------------
print("\n--- Iteración ---")
frutas = ["Uva", "Manzana", "Pera"]
for fruta in frutas:
    print(fruta)

print("\nUsando enumerate:")
for i, fruta in enumerate(frutas):
    print(i, fruta)

print("\nIterando sobre múltiples listas:")
frutas1 = ["Fresa", "Mora", "Cereza"]
frutas2 = ["Manzana", "Kiwi", "Pera"]
for f1, f2 in zip(frutas1, frutas2):
    print(f1, f2)

# ------------------------------
# COPIAS Y FUNCIONES ÚTILES
# ------------------------------
print("\n--- Copiar y funciones útiles ---")
numeros = [2, 4, 5, 1, 8]
numeros_copia = numeros.copy()
print(numeros_copia)

print(sum(numeros))   # Suma
print(min(numeros))   # Mínimo
print(len(numeros))   # Longitud

# ------------------------------
# LISTA DE LISTAS (MATRICES)
# ------------------------------
print("\n--- Lista de listas ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
print(matriz[0][0], matriz[1][1], matriz[2][2])
