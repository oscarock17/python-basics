"""
Estructura de Datos: Diccionarios (dict)
----------------------------------------
Los diccionarios en Python son colecciones **desordenadas y mutables**
de pares **clave-valor**. Cada clave es única y se usa para acceder
a su valor asociado. Se definen con llaves `{}` y pares separados
por dos puntos: `clave: valor`.

Ejemplo:
    persona = {"nombre": "José", "edad": 30}
"""

# ==============================================================
# 🔹 CREACIÓN DE DICCIONARIOS
# ==============================================================

# Forma básica
dicc = {"Clave1": 1, "Clave2": 2, "Clave3": 3, "Clave4": 4}
print(f"Diccionario: {dicc}")
print(f"Tipo: {type(dicc)}\n")

# Forma alternativa con dict()
dicc = dict(Clave1=1, Clave2=2, Clave3=3, Clave4=4)
print(f"Diccionario: {dicc}")
print(f"Tipo: {type(dicc)}\n")

# Diccionario vacío
dicc = {}
print(f"Diccionario vacío: {dicc}")
print(f"Tipo: {type(dicc)}\n")

# ==============================================================
# 🔹 CONVERSIÓN DESDE OTRAS ESTRUCTURAS
# ==============================================================

# Lista de listas → Diccionario
lista_de_listas = [["clave1", 1], ["clave2", 2], ["clave3", 3]]
dicc = dict(lista_de_listas)
print(f"Desde lista de listas: {dicc}")

# Lista de tuplas → Diccionario
lista_de_tuplas = [("clave1", 1), ("clave2", 2), ("clave3", 3)]
dicc = dict(lista_de_tuplas)
print(f"Desde lista de tuplas: {dicc}")

# Tupla de tuplas → Diccionario
tupla_de_tuplas = (("clave1", 1), ("clave2", 2), ("clave3", 3))
dicc = dict(tupla_de_tuplas)
print(f"Desde tupla de tuplas: {dicc}\n")

# ==============================================================
# 🔹 ACCESO Y MÉTODOS BÁSICOS
# ==============================================================

dicc = {"nombre": "José Ortega", "edad": 29, "estatura": 1.74}

# Acceder directamente por clave
print(dicc["nombre"])
print(dicc["edad"])
print(dicc["estatura"])

# Acceder de forma segura con get()
print(dicc.get("nombre", "La clave no existe en el diccionario"))

# Obtener claves, valores y elementos
print(f"Claves: {dicc.keys()}")
print(f"Valores: {dicc.values()}")
print(f"Elementos (pares): {dicc.items()}\n")

# ==============================================================
# 🔹 AGREGAR, MODIFICAR Y COMBINAR
# ==============================================================

# Agregar y modificar elementos
dicc["carrera"] = "Ing. Biomédica"
dicc["estatura"] = 1.75
print(f"Diccionario actualizado: {dicc}\n")

# Crear desde listas de claves y valores
claves = ["nombre", "edad", "estatura"]
valores = ["José", 29, 1.74]
dicc = {clave: valor for clave, valor in zip(claves, valores)}
print(f"Diccionario creado dinámicamente: {dicc}\n")

# Combinar diccionarios sin modificar los originales
dicc1 = {"nombre": "José Ortega", "edad": 29, "estatura": 1.74}
dicc2 = {"peso": 93, "carrera": "Ing. Biomédica"}
nuevo_dicc = {**dicc1, **dicc2}
print(f"Combinación sin modificar: {nuevo_dicc}")

# Combinar modificando (update)
dicc1.update(dicc2)
print(f"Combinación modificando: {dicc1}\n")

# ==============================================================
# 🔹 ELIMINAR ELEMENTOS
# ==============================================================

# Eliminar con del
dicc = {"nombre": "José", "edad": 29, "estatura": 1.74}
del dicc["edad"]
print(f"Después de eliminar con del: {dicc}")

# Eliminar con pop()
dicc = {"nombre": "José", "edad": 29, "estatura": 1.74}
eliminado = dicc.pop("edad")
print(f"Elemento eliminado: {eliminado}")
print(f"Diccionario actual: {dicc}")

# Limpiar el diccionario
dicc.clear()
print(f"Diccionario limpio: {dicc}\n")

# ==============================================================
# 🔹 OPERACIONES Y PROPIEDADES
# ==============================================================

dicc = {"nombre": "José", "edad": 29, "estatura": 1.74}

# Verificar pertenencia
print("nombre" in dicc)     # True
print("correo" not in dicc) # True

# Longitud
print(f"Cantidad de claves: {len(dicc)}\n")

# ==============================================================
# 🔹 ITERAR DICCIONARIOS
# ==============================================================

# Solo claves
for clave in dicc.keys():
    print(f"Clave: {clave}")

# Solo valores
for valor in dicc.values():
    print(f"Valor: {valor}")

# Clave y valor
for clave, valor in dicc.items():
    print(f"{clave}: {valor}")
print()

# Copiar diccionario
nuevo_dicc = dicc.copy()
dicc["edad"] = 30
print(f"Diccionario original modificado: {dicc}")
print(f"Copia independiente: {nuevo_dicc}\n")
