"""
==========================
    ESTRUCTURAS: CONJUNTOS
==========================

📘 Descripción:
Los conjuntos en Python (`set`) son **colecciones desordenadas, mutables y sin elementos duplicados**.
Los elementos deben ser **inmutables** (por ejemplo: números, cadenas o tuplas).

📌 Características:
- Se definen con llaves: { ... }
- No permiten elementos duplicados.
- No tienen índice (no son ordenados).
- Soportan operaciones matemáticas como:
  Unión ( ∪ ), Intersección ( ∩ ), Diferencia ( − ), y Diferencia simétrica (Δ).

👉 Existen dos tipos:
- `set`: conjunto mutable.
- `frozenset`: conjunto inmutable.
"""

# -------------------------------
# 1️⃣ Creación de conjuntos
# -------------------------------
conjunto = {1, 2, 3, 4, 5}
print(f"Conjunto: {conjunto}")
print(f"Tipo: {type(conjunto)}")

# Conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio, type(conjunto_vacio))

# Conjunto inmutable
conjunto_inmutable = frozenset({1, 2, 3, 4, 5})
print(conjunto_inmutable, type(conjunto_inmutable))

# -------------------------------
# 2️⃣ Conversión entre tipos
# -------------------------------
cadena = "Hola mundo"
conjunto_desde_cadena = set(cadena)
print(conjunto_desde_cadena)

# Conjunto → Cadena
conjunto = {'H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'k'}
cadena = "".join(conjunto)
print(cadena)

# Visualizar elementos únicos (elimina duplicados)
frutas = {"Manzana", "Fresa", "Plátano", "Manzana", "Fresa", "Sandía"}
print(",".join(frutas))

# -------------------------------
# 3️⃣ Operaciones básicas
# -------------------------------
# Agregar elementos
frutas = {"Manzana", "Uva", "Pera"}
frutas.add("Sandía")
print(frutas)

# Crear conjunto dinámicamente
numeros = set()
for i in range(10):
    numeros.add(i)
print(numeros)

# -------------------------------
# 4️⃣ Operaciones entre conjuntos
# -------------------------------
frutas1 = {"Manzana", "Pera", "Plátano"}
frutas2 = {"Uva", "Manzana", "Pera", "Sandía"}

# Unión (A ∪ B)
print(frutas1 | frutas2)
print(frutas1.union(frutas2))

# Intersección (A ∩ B)
print(frutas1 & frutas2)
print(frutas1.intersection(frutas2))

# Diferencia (A − B)
print(frutas1 - frutas2)
print(frutas1.difference(frutas2))

# Diferencia (B − A)
print(frutas2 - frutas1)
print(frutas2.difference(frutas1))

# -------------------------------
# 5️⃣ Eliminación de elementos
# -------------------------------
frutas = {"Manzana", "Pera", "Uva"}
frutas.remove("Pera")  # lanza error si no existe
print(frutas)

# Eliminar varios usando diferencia
frutas -= {"Pera", "Uva"}  # descarta ambos si existen
print(frutas)

# -------------------------------
# 6️⃣ Pertenencia e iteración
# -------------------------------
frutas = {"Manzana", "Pera", "Uva"}
print("Manzana" in frutas)
print("Mango" not in frutas)

# Iterar sobre elementos
for fruta in {"Uva", "Manzana", "Sandía", "Pera"}:
    print(fruta)

# Iterar sobre múltiples conjuntos
frutas1 = {"Uva", "Manzana", "Sandía", "Pera"}
frutas2 = {"Fresa", "Plátano", "Durazno", "Naranja"}
for f1, f2 in zip(frutas1, frutas2):
    print(f"{f1} - {f2}")

# -------------------------------
# 7️⃣ Copias y propiedades numéricas
# -------------------------------
frutas = {"Uva", "Manzana", "Sandía", "Pera"}
frutas_copia = frutas.copy()
print(frutas is frutas_copia)  # False → son objetos distintos

numeros = {4, 1, 8, 7, 9}
print("Suma:", sum(numeros))
print("Mínimo:", min(numeros))
print("Máximo:", max(numeros))
print("Longitud:", len(numeros))
