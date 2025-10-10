"""
Operadores en Python
--------------------
Los operadores son símbolos especiales que permiten realizar operaciones
sobre valores y variables. Se clasifican en:

1. Aritméticos: operaciones matemáticas comunes (+, -, *, /, **, //, %)
2. Asignación: asignan valores y combinan operaciones (=, +=, -=, etc.)
3. Comparación: comparan dos valores (==, !=, >, <, >=, <=)
4. Lógicos: combinan expresiones booleanas (and, or, not)
5. Identidad: comparan objetos en memoria (is, is not)
6. Pertenencia: verifican elementos en secuencias (in, not in)
"""

# ---- Operadores aritméticos ----
print("\n--- Operadores Aritméticos ---")
a, b = 10, 3
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División: {a} / {b} = {a / b}")
print(f"Exponenciación: {a} ** {b} = {a ** b}")
print(f"División entera: {a} // {b} = {a // b}")
print(f"Módulo: {a} % {b} = {a % b}")

# ---- Operadores de asignación ----
print("\n--- Operadores de Asignación ---")
x = 5
print(f"Asignación: x = {x}")
x += 3; print(f"x += 3 → {x}") #esto aumentatará el valor de x en 3
x -= 2; print(f"x -= 2 → {x}") #esto disminuirá el valor de x en 2
x *= 4; print(f"x *= 4 → {x}") #esto multiplicará el valor de x por 4
x /= 3; print(f"x /= 3 → {x}") #esto dividirá el valor de x por 3
x **= 2; print(f"x **= 2 → {x}") #esto elevará el valor de x al cuadrado
x //= 2; print(f"x //= 2 → {x}") #esto realizará una división entera de x entre 2
x %= 3; print(f"x %= 3 → {x}") #esto asignará a x el resto de la división entre x y 3

# ---- Operadores de comparación ----
print("\n--- Operadores de Comparación ---")
a, b = 5, 3
print(f"{a} == {b} → {a == b}")
print(f"{a} != {b} → {a != b}")
print(f"{a} > {b} → {a > b}")
print(f"{a} < {b} → {a < b}")
print(f"{a} >= {b} → {a >= b}")
print(f"{a} <= {b} → {a <= b}")

# ---- Operadores lógicos ----
print("\n--- Operadores Lógicos ---")
a, b = True, False
print(f"{a} and {b} → {a and b}")
print(f"{a} or {b} → {a or b}")
print(f"not {a} → {not a}")

# ---- Operadores de identidad ----
print("\n--- Operadores de Identidad ---")
a, b = 3.56, 3.56
print(f"a = {a}, b = {b}")
print(f"a is b → {a is b}")
print(f"a is not b → {a is not b}")

# ---- Operadores de pertenencia ----
print("\n--- Operadores de Pertenencia ---")
lista = [1, 2, 3, 4, 5]
print(f"3 in lista → {3 in lista}")
print(f"0 in lista → {0 in lista}")
print(f"6 not in lista → {6 not in lista}")
