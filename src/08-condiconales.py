# ------------------------------
# CONDICIONALES EN PYTHON
# ------------------------------

# La sentencia if en Python permite ejecutar un bloque de código
# solo si la condición evaluada es verdadera (True).
# Existen varias variantes:
# - if
# - if ... else
# - if ... elif ... else
# - Uso del operador "morsa" (:=)

print("=== Condicionales en Python ===")

# ------------------------------
# if
# ------------------------------
print("\n--- Ejemplo 1: if simple ---")
numero = float(input("Ingrese un número: "))
if numero > 0:
    print(f"{numero} es positivo")
if numero < 0:
    print(f"{numero} es negativo")
if numero == 0:
    print(f"{numero} es cero")

# ------------------------------
# if ... else
# ------------------------------
print("\n--- Ejemplo 2: if-else ---")
edad = int(input("Ingrese la edad: "))
if edad >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

# ------------------------------
# if ... elif ... else
# ------------------------------
print("\n--- Ejemplo 3: if-elif-else ---")
nota = int(input("Ingrese una nota (0-100): "))
if nota >= 90:
    print("Calificación A")
elif nota >= 80:
    print("Calificación B")
elif nota >= 70:
    print("Calificación C")
elif nota >= 60:
    print("Calificación D")
else:
    print("Calificación F")

# ------------------------------
# Operador "Morsa" (:=)
# ------------------------------
# Introducido en Python 3.8: permite asignar y evaluar en la misma expresión.
print("\n--- Ejemplo 4: operador morsa (:=) ---")

if (num := 10) > 5:
    print(f"{num} es mayor que 5")

cadena = "Hola mundo"
if (longitud := len(cadena)) > 0:
    print(f"Cadena no vacía, longitud = {longitud}")
else:
    print("La cadena está vacía")
